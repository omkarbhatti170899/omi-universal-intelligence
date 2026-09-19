import json, os, subprocess, sys, time, urllib.request

ROOT=os.path.dirname(os.path.dirname(__file__))
p=subprocess.Popen([sys.executable, os.path.join(ROOT,"backend","server.py")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    time.sleep(.25)
    health=json.load(urllib.request.urlopen("http://127.0.0.1:8787/health"))
    assert health["ok"] is True
    for mode in ["auto","fast","deep","research"]:
        req=urllib.request.Request(
            "http://127.0.0.1:8787/ask",
            data=json.dumps({"question":"Explain Omi verification briefly.","mode":mode}).encode(),
            headers={"Content-Type":"application/json"})
        d=json.load(urllib.request.urlopen(req))
        assert d["route"]
        assert d["brief_description"]
        assert d["answer"]
        assert "verification" in d
    print("Omi tests: PASS")
finally:
    p.terminate()
    p.wait(timeout=3)
