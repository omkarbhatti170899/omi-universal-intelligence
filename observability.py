import time, uuid, threading
_lock=threading.Lock()
_metrics={"requests":0,"errors":0,"ask_requests":0,"latency_ms_total":0.0}

def request_id(): return uuid.uuid4().hex[:16]

def record(path, elapsed_ms, error=False):
    with _lock:
        _metrics["requests"]+=1
        _metrics["latency_ms_total"]+=elapsed_ms
        if path=="/ask": _metrics["ask_requests"]+=1
        if error: _metrics["errors"]+=1

def snapshot():
    with _lock:
        d=dict(_metrics)
    d["avg_latency_ms"]=round(d["latency_ms_total"]/d["requests"],2) if d["requests"] else 0
    return d
