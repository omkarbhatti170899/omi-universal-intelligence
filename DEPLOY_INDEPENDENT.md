# Omi Independent Deployment

## Fast local production-like run
1. Install Docker.
2. Copy `.env.example` to `.env`.
3. Keep `OMI_PROVIDER=mock` for a no-credential smoke test.
4. Run `docker compose up --build`.
5. Open `http://localhost:8000`.

## Public hosting
Use any container host that accepts a Docker image (for example a VPS, managed container
service, or Kubernetes). Point HTTPS/TLS at the host and forward traffic to port 8000.

Required environment:
- `OMI_HOST=0.0.0.0`
- `PORT=<platform port>`
- `OMI_PROVIDER=<approved provider>`

Provider API keys must be configured as server-side secrets by the hosting platform.
Never place them in the frontend.

Omi has no required AppDeploy or Floot runtime dependency.
