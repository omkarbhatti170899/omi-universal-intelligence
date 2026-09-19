# Omi — Independent Self-Hosting

This stack does not require Floot or AppDeploy. It is packaged as a normal Docker service.

## Local
1. Copy `.env.production.example` to `.env.production`.
2. Keep `OMI_PROVIDER=mock` for a no-key local demo, or configure your approved provider server-side.
3. Run `docker compose up --build -d`.
4. Open `http://localhost:8000`.
5. Check `http://localhost:8000/health`, `/ready`, `/metrics`, and `/capabilities`.

## Server
Run the same compose stack on any Docker-capable VPS, VM, dedicated server, or private cloud. Put TLS/reverse proxy in front of port 8000 and keep `.env.production` outside source control.

## Independence
Omi owns its application/runtime layer. Hosting is replaceable. Model providers remain external unless Omi is later configured to use self-hosted models.
