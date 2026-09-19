from pathlib import Path
import sys, py_compile

root=Path(__file__).parent
backend=root/"backend"
sys.path.insert(0,str(backend))

for p in backend.glob("*.py"):
    py_compile.compile(str(p),doraise=True)

from universal_modes import resolve
from universal_router import route
from model_router import choose
from manager_intelligence import build_brief
from privacy import policy
from observability import record, snapshot

assert resolve("personal")=="personal"
assert resolve("developer")=="developer"
assert resolve("research")=="researcher"
assert route("student")["mode"]=="student"
assert choose("auto")[0]=="luna"
assert choose("deep")[0]=="terra"
assert choose("expert")[0]=="astra"
assert build_brief()["title"]=="Omi Executive Brief"
assert policy()["user_delete_supported"] is True
record("/health",1.0)
assert snapshot()["requests"] >= 1
print("OMI SMOKE TEST: PASS")
