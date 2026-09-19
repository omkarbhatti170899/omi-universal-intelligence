import os

MODELS = {
    "luna": os.getenv("OMI_MODEL_LUNA", "gpt-5.6-luna"),
    "terra": os.getenv("OMI_MODEL_TERRA", "gpt-5.6-terra"),
    "astra": os.getenv("OMI_MODEL_ASTRA", "gpt-6-astra"),
}

def choose(mode="auto", complexity=0, tools=False):
    requested = str(mode).lower()
    if requested in ("expert", "maximum", "astra"):
        return "astra", MODELS["astra"]
    if requested in ("deep", "terra"):
        return "terra", MODELS["terra"]
    if requested in ("luna", "fast"):
        return "luna", MODELS["luna"]
    # Auto escalation: routine -> Luna, deeper -> Terra, hardest/tool-heavy -> Astra.
    if tools and complexity >= 8:
        return "astra", MODELS["astra"]
    if complexity >= 5:
        return "terra", MODELS["terra"]
    return "luna", MODELS["luna"]

def profile(tier):
    key = tier if tier in MODELS else "luna"
    return {"tier": key, "model": MODELS[key]}
