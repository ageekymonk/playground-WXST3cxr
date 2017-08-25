import time
from functools import lru_cache


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)


time1 = time.time()
print(f'35 Fibonocci number is {fibonacci(35)}')
time2 = time.time()
print(f'Total time taken is {(time2-time1)*1000}ms')

time1 = time.time()
print(f'35 Fibonocci number is {fibonacci_cached(35)}')
time2 = time.time()
print(f'Total time taken is {(time2-time1)*1000 }ms')

print(f'{fibonacci_cached.cache_info()}')
