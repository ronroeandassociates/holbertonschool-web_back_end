#!/usr/bin/env python3

"""_summary_
2 Run time for four parallel comprehensions

Import async_comprehension from the previous file

write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it

Function:
    measure_runtime() -> float:
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The coroutine will loop 10 times each time asynchronously wait 1 second
    then yield a random number between 0 and 10
    Use the random module to generate a random number between 0 and 10
    """
    start: float = time.time()
    await asyncio.gather(
        *[async_comprehension() for _ in range(4)]
    )
    end: float = time.time()
    return end - start
