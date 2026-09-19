import json, os, re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
from pathlib import Path
from planner import plan
from orchestrator import run as orchestrate
from providers import ProviderError
from live_pipeline import execute as live_execute
from security import create_user, login, user_from_token, remember, memories, can_use_tool
from research import fetch, extract_text, ResearchError
from manager_intelligence import build_brief, roi_template
from universal_modes import all_modes
from localization import profile
from capabilities import get_capabilities
from universal_router import route as universal_route
from observability import request_id, record, snapshot
from privacy import policy
from config import MAX_QUESTION
from limits import allow
from audit import event
from agent import execute as execute_agent

def verify(question, brief, answer, sources):
    q={w for w in re.findall(r"[a-zA-Z0-9]+",question.lower()) if len(w)>3}
    a={w for w in re.findall(r"[a-zA-Z0-9]+",answer.lower()) if len(w)>3}
    overlap=len(q&a)/max(1,len(q))
    checks={"request_present":bool(question.strip()),"brief_present":bool(brief.strip()),
            "answer_present":bool(answer.strip()),"request_alignment":overlap>=0.02,
            "sources_consistent":all(s.get("url") for s in sources),
            "no_unverified_certainty":not any(x in answer.lower() for x in ["guaranteed fact","definitely true without evidence"])}
    return {"passed":all(checks.values()),"checks":checks,
            "notes":[] if all(checks.values()) else ["Review one or more response-integrity checks."]}

def security_headers():
    return {"X-Content-Type-Options":"nosniff","X-Frame-Options":"DENY",
            "Referrer-Policy":"strict-origin-when-cross-origin",
            "Content-Security-Policy":"default-src 'self'; connect-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; img-src 'self' data:",
            "Cache-Control":"no-store"}

class Handler(BaseHTTPRequestHandler):
    server_version="Omi/1.0"
    def _send(self,status,payload,content_type="application/json"):
        raw=json.dumps(payload).encode()
        self.send_response(status); self.send_header("Content-Type",content_type)
        for k,v in security_headers().items(): self.send_header(k,v)
        self.send_header("Access-Control-Allow-Origin",os.getenv("OMI_CORS_ORIGIN","http://127.0.0.1:8000"))
        self.send_header("Access-Control-Allow-Headers","Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods","GET, POST, OPTIONS")
        self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def _body(self):
        n=int(self.headers.get("Content-Length","0"))
        if n>2_000_000: raise ValueError("Request body too large")
        return json.loads(self.rfile.read(n) or b"{}")
    def do_OPTIONS(self): self._send(204,{})
    def do_GET(self):
        path=urlparse(self.path).path
        if path in {"/","/index.html"}:
            fp=Path(__file__).resolve().parent.parent/"web"/"index.html"
            data=fp.read_bytes(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8")
            for k,v in security_headers().items(): self.send_header(k,v)
            self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data); return
        if path=="/health": self._send(200,{"ok":True,"service":"omi","provider":os.getenv("OMI_PROVIDER","mock")}); return
        if path=="/metrics":
            self._send(200,snapshot()); return
        if path=="/privacy":
            self._send(200,policy()); return
        if path=="/modes":
            self._send(200,{"modes":all_modes()}); return
        if path=="/capabilities":
            self._send(200,{"capabilities":get_capabilities()}); return
        if path=="/localization":
            self._send(200,profile()); return
        if path=="/route":
            self._send(200,universal_route()); return
        if path=="/manager/brief":
            self._send(200,build_brief({"provider":os.getenv("OMI_PROVIDER","mock")},[])); return
        if path=="/manager/roi":
            self._send(200,roi_template({})); return
        if path=="/ready": self._send(200,{"ready":True,"service":"omi","provider_configured": bool(os.getenv("OMI_PROVIDER","mock"))}); return
        if path=="/memory/list":
            uid=user_from_token(self.headers.get("Authorization","").replace("Bearer ",""))
            if not uid: self._send(401,{"error":"Authentication required"}); return
            self._send(200,{"memories":memories(uid)}); return
        self._send(404,{"error":"Not found"})
    def do_POST(self):
        if not allow(self.client_address[0]): self._send(429,{"error":"Rate limit exceeded"}); return
        path=urlparse(self.path).path
        try: body=self._body()
        except Exception as e: self._send(400,{"error":str(e)}); return
        if path in {"/auth/register","/auth/login"}:
            try:
                email=str(body.get("email","")).strip(); password=str(body.get("password",""))
                if path.endswith("register"):
                    uid=create_user(email,password)
                    token=login(email,password)
                else:
                    token=login(email,password); uid=user_from_token(token) if token else None
                if not token: self._send(401,{"error":"Invalid credentials"}); return
                self._send(200,{"token":token,"user_id":uid}); return
            except ValueError as e: self._send(400,{"error":str(e)}); return
            except Exception: self._send(409,{"error":"Account creation failed"}); return
        if path=="/memory":
            uid=user_from_token(self.headers.get("Authorization","").replace("Bearer ",""))
            if not uid: self._send(401,{"error":"Authentication required"}); return
            content=str(body.get("content","")).strip()
            if not content: self._send(400,{"error":"Memory content required"}); return
            remember(uid,content); self._send(200,{"ok":True}); return
        if path=="/research":
            uid=user_from_token(self.headers.get("Authorization","").replace("Bearer ",""))
            if not uid or not can_use_tool(uid,"research"): self._send(401,{"error":"Authentication required"}); return
            try:
                url=str(body.get("url","")).strip(); result=fetch(url)
                self._send(200,{"source":{"url":result["url"],"status":result["status"],"content_type":result["content_type"],"text":extract_text(result["body"])[:12000]}})
            except ResearchError as e: self._send(403,{"error":"Research blocked","detail":str(e)})
            return
        if path!="/ask": self._send(404,{"error":"Not found"}); return
        question=str(body.get("question","")).strip(); mode=str(body.get("mode","auto")).lower()
        if not question: self._send(400,{"error":"Question is required"}); return
        if len(question)>MAX_QUESTION: self._send(413,{"error":"Question exceeds Omi's size limit"}); return
        if mode not in {"auto","fast","deep","research"}: self._send(400,{"error":"Invalid mode"}); return
        uid=user_from_token(self.headers.get("Authorization","").replace("Bearer ",""))
        session_id=uid or ("guest:"+self.client_address[0])
        try:
            p=plan(question,mode)
            execute_agent(question,mode,uid)
            if body.get("research_url"):
                result,source=orchestrate(question,p["route"],uid,body.get("research_url"),context=[])
            else:
                live=live_execute(question,session_id,mode)
                result,source=live["result"],None
            brief=f"Omi routed this request through {result['provider']} using the {p['route']} execution path."
            sources=[source] if source else []
            verification=verify(question,brief,result["text"],sources)
            event("ask",uid,route=p["route"],provider=result.get("provider"),outcome="verified" if verification["passed"] else "review")
            self._send(200,{"brief_description":brief,"answer":result["text"],"route":p["route"],
                            "intent":p["task_types"],"sources":sources,
                            "provider":{"provider":result.get("provider"),"model":result.get("model")},
                            "verification":verification,"trace_id":"local-"+str(abs(hash((session_id,question))))})
        except ResearchError as e: self._send(403,{"error":"Research blocked","detail":str(e)})
        except ProviderError as e: self._send(503,{"error":"AI provider unavailable","detail":str(e)})
        except Exception as e:
            event("ask",uid,route=mode,outcome="error")
            self._send(500,{"error":"Omi runtime error","detail":str(e)})

def run_server(host=None,port=None):
    host=host or os.getenv("OMI_HOST","127.0.0.1"); port=int(port or os.getenv("PORT","8000"))
    httpd=ThreadingHTTPServer((host,port),Handler); print(f"Omi running at http://{host}:{port}",flush=True)
    try: httpd.serve_forever()
    finally: httpd.server_close()

if __name__=="__main__": run_server()
