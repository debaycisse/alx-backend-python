#!/usr/bin/env python3
"""This module houses the definition of
a coroutine, named async_comprehension"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers from the async_generator coroutine

    Returns:
        a list of the returned data from the async_generator coroutine
    """
    return [numbers async for numbers in async_generator()]
