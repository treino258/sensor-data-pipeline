import time
from contextlib import contextmanager

@contextmanager
def measure_time():
    star = time.perf_counter()
    yield lambda: time.perf_counter() - start
    