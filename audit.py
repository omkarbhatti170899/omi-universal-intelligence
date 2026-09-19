import json, os, time
from pathlib import Path
LOG=Path(os.getenv("OMI_AUDIT_LOG","omi_audit.jsonl"))
def event(kind, user_id=None, route=None, provider=None, outcome="ok", meta=None):
    rec={"ts":int(time.time()),"kind":kind,"user_id":user_id,"route":route,
         "provider":provider,"outcome":outcome,"meta":meta or {}}
    with LOG.open("a",encoding="utf-8") as f:
        f.write(json.dumps(rec,separators=(",",":"))+"\n")
