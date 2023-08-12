#!/usr/bin/env python3
''' Use a function to calculate the total runtime of a coroutine function '''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return (total_time / n)

n = 2
max_delay = 9

print(measure_time(n, max_delay))
