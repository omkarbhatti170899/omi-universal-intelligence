import os, re, socket, ipaddress, urllib.parse, urllib.request

MAX_BYTES=int(os.getenv("OMI_RESEARCH_MAX_BYTES","1000000"))
TIMEOUT=int(os.getenv("OMI_RESEARCH_TIMEOUT","10"))
ALLOWED_HOSTS={x.strip().lower() for x in os.getenv("OMI_RESEARCH_ALLOWED_HOSTS","").split(",") if x.strip()}

class ResearchError(RuntimeError): pass

def _allowed(host):
    return bool(ALLOWED_HOSTS) and host.lower() in ALLOWED_HOSTS

def _public(host):
    try:
        infos=socket.getaddrinfo(host,None)
        for item in infos:
            ip=ipaddress.ip_address(item[4][0])
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
                return False
        return True
    except Exception:
        return False

def fetch(url):
    u=urllib.parse.urlparse(url)
    host=(u.hostname or "").lower()
    if u.scheme!="https" or not host or not _allowed(host):
        raise ResearchError("URL is not allowed by Omi's research policy")
    if not _public(host):
        raise ResearchError("Research target resolves to a non-public network")
    req=urllib.request.Request(url,headers={"User-Agent":"Omi-Research/1.0"})
    try:
        with urllib.request.urlopen(req,timeout=TIMEOUT) as r:
            data=r.read(MAX_BYTES+1)
            if len(data)>MAX_BYTES: raise ResearchError("Response exceeds Omi research size limit")
            return {"url":url,"status":r.status,"content_type":r.headers.get("Content-Type",""),"body":data.decode("utf-8","replace")}
    except ResearchError: raise
    except Exception as e: raise ResearchError("Research request failed") from e

def extract_text(html):
    text=re.sub(r"<script[^>]*>.*?</script>"," ",html,flags=re.I|re.S)
    text=re.sub(r"<style[^>]*>.*?</style>"," ",text,flags=re.I|re.S)
    text=re.sub(r"<[^>]+>"," ",text)
    return re.sub(r"\s+"," ",text).strip()
