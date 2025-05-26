#!/usr/bin/python3
"""Module providing a utility function to check exact class membership.

This module defines the function `is_same_class` which checks whether
an object is exactly an instance of a specified class
(not considering inheritance).
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`,
        False otherwise.

    Examples:
        >>> is_same_class(5, int)
        True
        >>> is_same_class(5, float)
        False
        >>> class A: pass
        ...
        >>> a = A()
        >>> is_same_class(a, A)
        True
    """
    return type(obj) is a_class
