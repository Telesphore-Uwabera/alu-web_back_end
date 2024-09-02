#!/usr/bin/env python3
"""
This module contains a function task_wait_n that spawns multiple asyncio tasks
using task_wait_random and returns their results in ascending order.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random  # Import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay to pass to wait_random via task_wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Gather results as they complete using asyncio.as_completed
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
