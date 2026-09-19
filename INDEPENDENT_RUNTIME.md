# Independent Omi Runtime

Omi is now structured as a provider-neutral application.

## Execution
1. Receive request
2. Detect intent
3. Select AUTO/FAST/DEEP/RESEARCH route
4. Generate through an approved provider adapter
5. Run verification checks
6. Return brief description + answer + metadata

## Provider configuration
Set `OMI_PROVIDER=mock`, `openai`, or `gemini`.
Keep API keys in environment variables; never commit them.

## Portability
The project contains no AppDeploy or Floot runtime dependency. It can be run locally,
inside Docker, on a VPS, or on another cloud platform.

## IP hygiene
Use independently authored code, UI, branding and assets. Keep third-party licenses,
authorship records and development history. Obtain professional IP/trademark review
before commercial launch.
