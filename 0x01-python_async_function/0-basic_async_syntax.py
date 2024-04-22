#!/usr/bin/env python3
'''
    Defines a module with an asynchronous coroutine that
    takes in an integer argument that waits for a random delay
    between 0 and max_delay seconds and eventually returns it
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
        Returns an integer after a delay

        Args:
            max_delay (int): An integer number

        Returns:
            int : max_delay's value
    '''
    delay2: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay2)
    return delay2
