"""Side-effect-free Omi runtime helpers."""
import os

def runtime_config():
    return {
        "host": os.getenv("OMI_HOST", "127.0.0.1"),
        "port": int(os.getenv("PORT", "8000")),
        "provider": os.getenv("OMI_PROVIDER", "mock"),
    }

def health_payload():
    return {"status": "ok", "service": "omi", "runtime": "independent"}
