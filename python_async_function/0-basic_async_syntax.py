#!/usr/bin/env python3
"""
This module contains a simple asynchronous coroutine
that waits for a random delay between 0 and max_delay seconds.
"""

import asyncio
import random
from typing import Optional

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    and returns the duration of the delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The duration of the random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
