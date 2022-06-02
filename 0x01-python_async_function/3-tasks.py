#!/usr/bin/env python3

"""_summary_
3 Tasks
Import wait_random from 0-basic_async_syntax

a function (do not create an async function,
use the regular function syntax to do this)

Function:
    task_wait_random(max_delay: int = 0)->asyncio.Task:
"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    task_wait_random that takes an integer
    max_delay and returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
