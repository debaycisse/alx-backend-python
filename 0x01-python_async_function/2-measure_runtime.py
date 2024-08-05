#!/usr/bin/env python3
"""This module houses the definition of
a function, named measure_runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution for the wait_n coroutine

    Args:
        n - the number of times to spawn the coroutine in wait_n
        max_delay - the maximum value for the range of random value,
        used in the nested coroutine in wait_n coroutine

    Returns:
        the total time, divided by n
    """
    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_t = time.time()
    total_time = (end_t - start_t) / n
    return total_time
