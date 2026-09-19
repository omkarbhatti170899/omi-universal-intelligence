# Omi v19 — Self-Host Quickstart

1. Copy `.env.example` to `.env`.
2. Put provider credentials only in `.env` or your secret manager.
3. Set the desired model IDs for Luna/Terra/Astra.
4. Run `docker compose up -d --build`.
5. Open the configured Omi web port.
6. Check `/health` and `/metrics`.
7. Run the included preflight before public exposure.

For production, put Omi behind HTTPS/reverse proxy, restrict database/storage access,
use a real secret manager, and enable backups and monitoring.

Omi remains independent of Floot and AppDeploy.
