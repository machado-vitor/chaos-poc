import time, requests

def is_latency_under_seconds(url: str, threshold: float, timeout: float = 2.0, repeats: int = 1) -> bool:
    """
    Returns True when the best observed latency is below the provided threshold (in seconds).
    """
    latency = None
    for _ in range(max(1, int(repeats))):
        start = time.perf_counter()
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        dt = time.perf_counter() - start
        latency = dt if latency is None else min(latency, dt)
    return latency < threshold
