#!/usr/bin/env python3
'''Defines a mdule that measures asynchronous functions' runtime'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension four times in parallel and
        returns total runtime"""
    start = time.time()
    functs = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*functs)
    stop = time.time()
    elapsed = stop - start
    return elapsed
