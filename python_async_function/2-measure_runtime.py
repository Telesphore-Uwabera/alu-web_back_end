#!/usr/bin/env python3
"""
This module contains a function called measure_time
that measures the total execution time for wait_n and returns the average time.
"""

import asyncio
import time
from 1-concurrent_coroutines import wait_n  # Import wait_n from previous task

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay to pass to wait_random via wait_n.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run wait_n
    total_time = time.time() - start_time  # Calculate the total elapsed time
    
    return total_time / n  # Return the average time per coroutine
