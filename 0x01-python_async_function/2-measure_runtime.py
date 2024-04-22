#!/usr/bin/env python3
'''
    Defines a module with an async function measure_time that measures
    the total execution time for a wait_n() function and returns total_time / n
'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Returns the total execution time'''
    initial = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapse = time.time() - initial
    return elapse / n
