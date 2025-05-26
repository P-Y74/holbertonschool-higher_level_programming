#!/usr/bin/python3
"""Module that provides a function to check if an object is an instance of
a class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or inherits from it.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or a subclass of
        `a_class`, False otherwise.
    """
    return isinstance(obj, a_class)
