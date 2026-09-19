# Omi v13 — Live Intelligence Pipeline

The `/ask` path now uses the integrated pipeline for normal requests:

Planner → conversation context → configured provider → response → verification.

Research requests continue through the separate research path with its existing security
controls. The default provider remains mock, so the integration tests do not consume API
credits. Set `OMI_PROVIDER=openai` and a server-side `OMI_AI_API_KEY` to activate the
OpenAI Responses API adapter. GPT-5.6 Luna is the configured default model in v12.
