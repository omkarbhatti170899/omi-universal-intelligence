import os
def policy():
    return {
        "retention_days":int(os.getenv("OMI_RETENTION_DAYS","30")),
        "store_conversations":os.getenv("OMI_STORE_CONVERSATIONS","true").lower()=="true",
        "redact_logs":os.getenv("OMI_REDACT_LOGS","true").lower()=="true",
        "training_use":"not_enabled_by_omi",
        "user_delete_supported":True
    }
