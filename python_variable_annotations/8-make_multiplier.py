#!/usr/bin/env python3
"""
Module 8-make_multiplier
Contains a function that returns a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that
          multiplies a float by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Multiplies the input by the stored multiplier."""
        return x * multiplier

    return multiplier_function
