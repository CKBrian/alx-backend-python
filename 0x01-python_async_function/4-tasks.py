#!/usr/bin/env python3
'''Defines a module with an async routine called task_wait_n'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays (float values)'''
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
