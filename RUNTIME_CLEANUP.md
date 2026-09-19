# Omi Independent v8 — Runtime Fixed

The import-time server launch found in v7 has been removed. `server.py` now starts
only through its explicit `__main__` entrypoint or the top-level `run_omi.py` launcher.

Validation:
- Python compilation passes.
- `server` imports without starting a blocking HTTP server.
- Frontend/API contract remains present.
- No AppDeploy or Floot runtime dependency is introduced.
