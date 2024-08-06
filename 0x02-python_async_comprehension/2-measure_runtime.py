#!/usr/bin/env python3
"""This module houses the definition of a
coroutine function, named measure_runtime"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension coroutine 4 times"""
    start_t = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_t
