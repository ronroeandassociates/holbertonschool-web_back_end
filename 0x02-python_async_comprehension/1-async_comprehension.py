#!/usr/bin/env python3

"""_summary_
1 Async Comprehensions
Import async_generator from the previous task
write a coroutine called async_comprehension that takes no arguments
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers

Function:
    async_comprehension() -> list[float]:
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will loop 10 times each time asynchronously wait 1 second
    then yield a random number between 0 and 10
    Use the random module to generate a random number between 0 and 10
    """
    numbers = [i async for i in async_generator()]
    return numbers
