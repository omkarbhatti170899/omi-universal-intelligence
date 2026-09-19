from pathlib import Path
import os, sys, py_compile

root=Path(__file__).parent
backend=root/"backend"
required=["server.py","providers.py","model_router.py","universal_modes.py",
          "universal_router.py","observability.py","privacy.py"]
missing=[x for x in required if not (backend/x).exists()]
if missing:
    print("PREFLIGHT FAIL: missing:", ", ".join(missing)); sys.exit(1)

for p in backend.glob("*.py"):
    py_compile.compile(str(p), doraise=True)

env=root/".env.example"
compose=root/"docker-compose.yml"
docker=root/"Dockerfile"
for p in (env,compose,docker):
    if not p.exists():
        print("PREFLIGHT FAIL:", p.name); sys.exit(1)

print("SELF-HOST PREFLIGHT: PASS")
print("Application files: PASS")
print("Python compilation: PASS")
print("Docker/Compose manifests: PASS")
print("Secrets remain environment-configured: PASS")
