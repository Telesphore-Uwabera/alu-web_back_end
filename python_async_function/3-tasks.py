#!/usr/bin/env python3
"""
This module contains a function task_wait_random that returns an asyncio.Task.
"""

import asyncio
from 0-basic_async_syntax import wait_random  # Import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: The asyncio.Task object running wait_random.
    """
    # Create and return a task running wait_random
    return asyncio.create_task(wait_random(max_delay))
