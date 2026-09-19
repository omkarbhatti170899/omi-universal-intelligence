import os
ENV=os.getenv("OMI_ENV","development")
DEBUG=ENV!="production"
RATE_LIMIT=int(os.getenv("OMI_RATE_LIMIT","30"))
RATE_WINDOW=int(os.getenv("OMI_RATE_WINDOW","60"))
MAX_QUESTION=int(os.getenv("OMI_MAX_QUESTION","12000"))
