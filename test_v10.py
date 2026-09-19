import os, sys, tempfile, threading, urllib.request, json
os.environ["OMI_PROVIDER"]="mock"
os.environ["OMI_DB"]=tempfile.mktemp(suffix=".db")
os.environ["OMI_AUDIT_LOG"]=tempfile.mktemp(suffix=".jsonl")
sys.path.insert(0,"backend")
from providers import get_provider
assert get_provider().name=="mock"
from security import create_user, login, user_from_token
uid=create_user("test@example.com","strongpass123"); tok=login("test@example.com","strongpass123")
assert uid and tok and user_from_token(tok)==uid
from server import Handler
from http.server import ThreadingHTTPServer
srv=ThreadingHTTPServer(("127.0.0.1",0),Handler)
thread=threading.Thread(target=srv.serve_forever,daemon=True); thread.start()
base=f"http://127.0.0.1:{srv.server_address[1]}"
def req(path, payload=None, headers=None):
    data=None if payload is None else json.dumps(payload).encode()
    r=urllib.request.urlopen(urllib.request.Request(base+path,data=data,headers=headers or {},method="POST" if data else "GET"),timeout=3)
    return json.loads(r.read())
assert req("/health")["ok"] is True
out=req("/ask",{"question":"Hello Omi","mode":"auto"})
assert out["provider"]["provider"]=="mock" and out["answer"]
r=urllib.request.urlopen(urllib.request.Request(base+"/memory/list",headers={"Authorization":"Bearer "+tok}),timeout=3)
assert "memories" in json.loads(r.read())
srv.shutdown(); srv.server_close()
print("V10 END-TO-END: PASS")
