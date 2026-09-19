# Omi v12 — Real Provider Adapter

Omi now includes a server-side OpenAI Responses API adapter.

Default remains `OMI_PROVIDER=mock`, so tests and local development do not spend API
credits. To enable live generation, set:
- `OMI_PROVIDER=openai`
- `OMI_AI_API_KEY` as a deployment secret
- optionally `OMI_AI_MODEL` (default `gpt-5.6-luna`)
- optionally `OMI_AI_BASE_URL`

No credential is stored in the repository or sent to the browser.
