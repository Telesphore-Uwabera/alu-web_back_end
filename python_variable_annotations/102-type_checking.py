#!/usr/bin/env python3
"""
Module 102-type_checking
Contains a function that zooms in on an array.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on a tuple by repeating each element `factor` times.

    Args:
        lst (Tuple[int, ...]): The tuple of integers to zoom in on.
        factor (int): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A new list with elements repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

# Test cases
array = (12, 72, 91)  # Changed to tuple for testing

zoom_2x = zoom_array(array)

# This should raise a TypeError if uncommented, as expected
# zoom_3x = zoom_array(array, 3.0)
