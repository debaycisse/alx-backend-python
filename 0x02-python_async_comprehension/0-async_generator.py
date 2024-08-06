#!/usr/bin/env python3
"""This module houses a definition for a
coroutine, named async_generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """asyncronously generates a range of number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
