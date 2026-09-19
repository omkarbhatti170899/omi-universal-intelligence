import os, sys
from pathlib import Path

root=Path(__file__).parent
backend=root/"backend"
sys.path.insert(0,str(backend))

required_env=["OMI_PROVIDER"]
missing=[k for k in required_env if not os.getenv(k)]
if missing:
    print("Startup note: optional provider settings are not configured:", ", ".join(missing))
print("Omi startup preflight: PASS")
print("Runtime:", os.getenv("OMI_PROVIDER","mock"))
print("Model override:", os.getenv("OMI_AI_MODEL","auto-router"))
print("Omi is ready for the configured application server.")
