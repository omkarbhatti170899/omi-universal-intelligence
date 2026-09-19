# Omi Production Runbook

## Local
Run `python run_omi.py`, then open `http://127.0.0.1:8000/`.

## Container
Build and run the included Docker image. The image listens on port 8000 and includes a
container health check against `/health`.

## Public deployment baseline
Use HTTPS at the platform/reverse-proxy layer, keep provider credentials in secrets,
and place authentication/rate limiting at the edge before exposing the service publicly.

## Smoke checks
- `GET /health` returns JSON with `status: ok`.
- `/` loads the Omi workspace.
- `/ask` accepts a valid question and returns route/provider/verification metadata.
- No real secrets exist in source control.

Actual cloud deployment requires a target platform account and credentials; this artifact
is prepared to be deployed independently of AppDeploy and Floot.
