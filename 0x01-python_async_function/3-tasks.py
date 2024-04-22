#!/usr/bin/env python3
'''Defines a module with an async routine task_wait_random
    that returns an asyncio.Task'''

import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    '''return a asyncio.Task'''
    task = asyncio.create_task(wait_random(max_delay))
    return task
