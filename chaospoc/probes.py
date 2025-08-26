import time, requests

def measure_latency_seconds(url: str, timeout: float = 2.0, repeats: int = 1) -> float:
    """
    Returns latency in seconds (float). Use with a 'range' tolerance in experiment.json.
    """
    best = None
    for _ in range(max(1, int(repeats))):
        start = time.perf_counter()
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        dt = time.perf_counter() - start
        best = dt if best is None else min(best, dt)
    return best
