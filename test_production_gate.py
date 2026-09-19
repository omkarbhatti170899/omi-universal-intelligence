import sys, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/"backend"))
from observability import record,snapshot
from privacy import policy
record("/ask",12.5); record("/health",2.0,error=True)
m=snapshot()
assert m["requests"]==2 and m["ask_requests"]==1 and m["errors"]==1
assert m["avg_latency_ms"]>0
assert policy()["user_delete_supported"] is True
print("PRODUCTION HARDENING: PASS")
