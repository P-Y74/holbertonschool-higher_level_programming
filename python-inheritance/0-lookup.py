#!/usr/bin/python3
"""Module that defines the lookup function.

This module provides a utility function to return a list of available
attributes and methods of an object using the built-in dir() function.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj (object): The object whose attributes and methods are to be listed.

    Returns:
        list: A list of strings representing the names of the object's
        attributes and methods.
    """
    return dir(obj)
