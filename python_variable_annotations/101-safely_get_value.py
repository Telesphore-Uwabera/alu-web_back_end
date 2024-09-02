#!/usr/bin/env python3
"""
Module 101-safely_get_value
Contains a function that safely retrieves a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(
    dct: Mapping[Any, T], 
    key: Any, 
    default: Union[T, None] = None
) -> Union[T, None]:
    """
    Retrieves the value for a given key from a dictionary, 
    returning a default value if the key is not found.

    Args:
        dct (Mapping[Any, T]): A dictionary-like object where 
            the value type is T.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return 
            if the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key or the 
            default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
