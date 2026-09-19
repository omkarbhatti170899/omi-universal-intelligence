import sys
sys.path.insert(0, "backend")
import server
for mode in ["auto","fast","deep","research"]:
    intent=server.intent_for("Explain Omi verification briefly.")
    route=server.route_for(intent,mode)
    brief,answer=server.draft("Explain Omi verification.",route)
    result=server.verify("Explain Omi verification.",brief,answer,[])
    assert brief and answer and isinstance(result["passed"],bool)
    assert "request_alignment" in result["checks"]
print("Core verification smoke test: PASS")
