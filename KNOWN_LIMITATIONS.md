# Omi v10 — Explicit Production Boundaries

The core runtime is hardened and tested offline. Remaining external requirements are deployment concerns, not hidden bugs:
- A real AI provider requires a valid server-side API key.
- Public deployment needs HTTPS and platform-level secret storage/rate limiting.
- Research only permits explicitly allow-listed HTTPS hosts and rejects private-network targets.
- SQLite is suitable for a single-instance deployment; multi-instance scale should use a managed database.
- The mock provider is intentionally offline and does not claim to be a live model.
