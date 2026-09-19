# Omi Universal AI — Independent Runtime

A portable, provider-neutral Omi runtime that does not require AppDeploy or Floot.

## Run locally

```bash
python backend/server.py
```

Then open `frontend/index.html` in a browser. For production, serve `frontend/` from any static web server and point `OMI_API_URL` at the backend.

## Environment

Optional provider credentials can be added later. The core ships without hard-coded provider keys.

- `OMI_HOST` — default `0.0.0.0`
- `OMI_PORT` — default `8787`
- `OMI_PROVIDER` — default `mock`
- `OMI_API_KEY` — provider key, if a provider adapter is configured

## Architecture

Request → intent → route → tools/research → draft → verification → response.

The provider interface is intentionally abstract so Omi can connect to approved AI providers without coupling the product to one vendor.

## IP / originality guardrails

Omi uses independently authored UI, code and branding. Do not add third-party proprietary code, logos, prompts, assets, or distinctive trade dress. Review third-party licenses and trademark/IP status before commercial launch.

This package is an engineering baseline, not legal advice.

## Verification Intelligence v2

The post-generation verifier now checks request alignment and unsupported-certainty markers in addition to presence, source metadata, and live-claim integrity.
