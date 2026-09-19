# Omi Security Baseline v4

- Passwords are salted and hashed with PBKDF2-HMAC-SHA256.
- Sessions use random bearer tokens stored only as SHA-256 hashes in SQLite.
- Sessions expire.
- Memory is isolated by user ID.
- Tool policy is default-deny; only explicitly approved tools can execute.
- Provider credentials remain environment-only.
- SQLite uses WAL for safer concurrent local access.

Before public launch: use HTTPS, rotate secrets, set a strong `OMI_SESSION_SECRET`,
add CSRF protection where cookie auth is introduced, add account recovery, rate limits,
structured audit logs, secret-manager integration, database backups, and a professional
security review.
