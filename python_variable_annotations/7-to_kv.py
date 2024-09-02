#!/usr/bin/env python3
"""
Module 7-to_kv
Contains a function that returns a tuple
with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): A string.
        v (Union[int, float]): A number (integer or float).

    Returns:
        Tuple[str, float]: A tuple where the first
        element is the string k,
                           and the second element
                           is the square of v as a float.
    """
    return (k, float(v ** 2))
