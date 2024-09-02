#!/usr/bin/env python3
"""
Module 9-element_length
Contains a function that returns the length of each
 element in a list of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains a sequence
      and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
          (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
          each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
