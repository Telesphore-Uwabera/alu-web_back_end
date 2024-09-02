#!/usr/bin/env python3
"""
This module contains a coroutine called wait_n
that spawns wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of coroutines
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Sort the delays manually by using bubble sort (to avoid using built-in sort())
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]

    return delays
