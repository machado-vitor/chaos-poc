import time
import requests

def measure_latency_seconds(url: str, timeout: int = 2) -> float:
    """
    Returns the elapsed time in seconds for a single HTTP GET.
    Chaos Toolkit will compare this numeric result against the tolerance range.
    """
    t0 = time.perf_counter()
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return time.perf_counter() - t0
