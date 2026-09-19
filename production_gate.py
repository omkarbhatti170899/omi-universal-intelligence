from pathlib import Path
import os, sys, py_compile
root=Path(__file__).parent
backend=root/"backend"
required=["server.py","providers.py","model_router.py","universal_router.py","observability.py","privacy.py"]
missing=[x for x in required if not (backend/x).exists()]
for p in backend.glob("*.py"): py_compile.compile(str(p),doraise=True)
assert not missing, missing
assert (root/"web/index.html").exists()
assert (root/".env.example").exists()
print("PRODUCTION GATE: PASS")
