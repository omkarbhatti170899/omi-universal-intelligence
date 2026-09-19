import locale, os
SUPPORTED_LANGUAGES=["English","Hindi","Marathi","Spanish","French","German","Portuguese","Japanese","Korean","Arabic","Chinese"]
def profile(language=None, timezone=None, currency=None, units=None):
    return {
        "language":language or os.getenv("OMI_LANGUAGE","English"),
        "timezone":timezone or os.getenv("OMI_TIMEZONE","UTC"),
        "currency":currency or os.getenv("OMI_CURRENCY","USD"),
        "units":units or os.getenv("OMI_UNITS","metric"),
        "supported_languages":SUPPORTED_LANGUAGES,
    }
