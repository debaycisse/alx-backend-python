#!/usr/bin/env python3
"""This module houses a definition of an
asynchronous function, called coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay period and returns the random's value

    Args:
        max_delay - maximum value of the random range to wait

    Returns:
        the random value
    """
    v = random.uniform(0, max_delay)
    await asyncio.sleep(v)
    return v
