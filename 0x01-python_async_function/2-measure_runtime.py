#!/usr/bin/env python3
"""Script contain measure_time function"""
import asyncio
import time
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ fucntion  that measure the total
    excution time for wait_n function"""
    start_time = time.perf_counter()
    # time.perf_counter() return the current time
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
