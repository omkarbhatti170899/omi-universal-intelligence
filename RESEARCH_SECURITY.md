# Omi Research & Tool Security v5

Omi now has a constrained HTTPS research primitive.

Safety boundaries:
- HTTPS only.
- Host allowlist via `OMI_RESEARCH_ALLOWED_HOSTS`.
- Response-size limit.
- Request timeout.
- No shell/OS execution.
- Authentication required.
- Tool access remains default-deny.
- Retrieved text is treated as untrusted data.

For production, add SSRF defenses (DNS rebinding/IP-range checks), robots/terms compliance,
content-type filtering, per-user quotas, audit logging, and a dedicated sandbox/proxy.
