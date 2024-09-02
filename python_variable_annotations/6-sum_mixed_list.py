#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Contains a function to sum a list of integers and floats.
"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list containing both integers and floats and returns the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return sum(mxd_lst)
