import time, threading
from collections import defaultdict, deque
from config import RATE_LIMIT, RATE_WINDOW
_lock=threading.Lock()
_hits=defaultdict(deque)
def allow(key):
    now=time.time()
    with _lock:
        q=_hits[key]
        while q and now-q[0]>RATE_WINDOW: q.popleft()
        if len(q)>=RATE_LIMIT: return False
        q.append(now); return True
