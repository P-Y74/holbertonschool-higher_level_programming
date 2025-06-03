#!/usr/bin/python3
"""
Module class_to_json

This module provides a function to generate a dictionary representation of
an object suitable for JSON serialization. Only simple Python data types
(list, dict, str, int, bool) are considered.

Functions:
    class_to_json(obj): Returns the dictionary description of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary representation of a simple Python object.

    This function returns the `__dict__` attribute of an instance, which contains
    all the attributes of the object as key-value pairs. It assumes that all attributes
    are of simple serializable types: list, dict, str, int, or bool.

    Args:
        obj (object): An instance of a class with simple attributes.

    Returns:
        dict: A dictionary representing the object's attributes.
    """
    return obj.__dict__