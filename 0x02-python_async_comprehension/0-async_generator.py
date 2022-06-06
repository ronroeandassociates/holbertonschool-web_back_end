#!/usr/bin/env python3

"""
__SUMMARY__

0 Async Generator
a coroutine called async_generator that takes no arguments

Function:
    async_generator() -> generator[float, None, None]:
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:

    """
    The coroutine will loop 10 times each time asynchronously wait 1 second
    then yield a random number between 0 and 10
    Use the random module to generate a random number between 0 and 10
    """
    max_delay = 10
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
