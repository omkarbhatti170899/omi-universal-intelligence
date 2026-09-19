# Start Omi

1. Install Python 3.10+.
2. Optional: create a virtual environment.
3. Set `OMI_PROVIDER=mock` for a zero-credential local demo.
4. Run `python run_omi.py`.
5. Open `http://127.0.0.1:8000/` in a browser.

For live AI generation, configure an approved provider key through environment variables.
Never put API keys into the frontend or commit them to the repository.

This is a standalone web application and does not require AppDeploy or Floot.
