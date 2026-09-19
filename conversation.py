from collections import defaultdict, deque
import threading
_LOCK=threading.RLock()
_SESSIONS=defaultdict(lambda: deque(maxlen=12))

def history(session_id):
    with _LOCK:
        return list(_SESSIONS.get(str(session_id), ()))

def add(session_id, role, content):
    if not session_id or not content: return
    with _LOCK:
        _SESSIONS[str(session_id)].append({"role":role,"content":str(content)[:6000]})

def clear(session_id):
    with _LOCK:
        _SESSIONS.pop(str(session_id),None)
