#!/usr/bin/python3
"""
Module from_json_string

This module provides a function to convert a JSON string into a corresponding
Python data structure.
"""


import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    This function uses json.loads() to deserialize a JSON-formatted string
    into its corresponding Python data structure
    (e.g., dict, list, str, int, etc.).

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        Any: The Python object resulting from the deserialization of the
        JSON string.

    Note:
        Exceptions for invalid JSON strings are not handled in this function.
    """
    return json.loads(my_str)
