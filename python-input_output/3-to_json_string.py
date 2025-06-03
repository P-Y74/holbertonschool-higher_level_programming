#!/usr/bin/python3
"""
Module to_json_string

This module provides a function to convert a Python object into its
JSON string representation.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    This function uses the json.dumps() method to serialize a Python object
    into a JSON-formatted string.

    Args:
        my_obj (Any): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.

    Note:
        Exceptions for non-serializable objects are not handled in
        this function.
    """
    return json.dumps(my_obj)
