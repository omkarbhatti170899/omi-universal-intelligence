# Omi Production Checklist v6

Implemented:
- Provider abstraction
- Authentication/session foundation
- Per-user memory
- Default-deny tools
- Constrained HTTPS research
- Request size limit
- Per-client rate limiting
- Environment-based configuration
- No credentials in source
- Docker portability

Before public launch:
- HTTPS/TLS termination
- Production secret manager
- Managed PostgreSQL (or equivalent)
- Redis/distributed rate limiting
- Email verification/recovery
- CSRF strategy if cookie sessions are introduced
- SSRF DNS/IP-range validation in research proxy
- Structured audit logs
- Backups and restore drills
- Dependency/SBOM scanning
- External security and IP/trademark review
