# Omi v20 — Deployment Ready Baseline

This release focuses on making the independent Omi package easy to validate before
being exposed to users.

## Validation flow
1. Run `python self_host_preflight.py`
2. Run `python smoke_test.py`
3. Configure `.env`
4. Build/start with Docker Compose on a host that has Docker
5. Check `/health`
6. Check `/metrics`
7. Perform a live provider request
8. Only then expose the service publicly

The package does not contain provider secrets and does not require Floot or AppDeploy.
