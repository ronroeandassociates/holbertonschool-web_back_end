#!/usr/bin/env python3

"""_summary_
1 Let's execute multiple coroutines at the same time
with async

Import wait_random from the previous python file
that you’ve written and write an async routine called
wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times
with the specified max_delay.

Args:
    n: (int): [description]
    max_delay: (int): [description]


Functions:
    wait_n(n: int, max_delay: int) -> float:
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    """
    wait_n should return the list of all the delays (
    float values). The list of the delays should be
    in ascending order without using sort() because
    of concurrency.
    Returns:
        List[float]: [Return the list of all the delays (float values)]
    """
    lister = [await wait_random(max_delay) for _ in range(n)]
    return sorted(lister)
