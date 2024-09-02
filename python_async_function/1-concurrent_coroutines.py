#!/usr/bin/env python3
"""
This module contains a coroutine called wait_n
that spawns wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random  # Updated import

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
    # Create a list of tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Gather results as they complete using asyncio.as_completed
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
