#/usr/bin/env python3
'''Defines a module with an asynchronous function async_generator'''

import asyncio
import random


async def async_generator():
    """Yields a random number between 0 and 10"""
    for _ in range(10):
        yield random.uniform(0, 10)
