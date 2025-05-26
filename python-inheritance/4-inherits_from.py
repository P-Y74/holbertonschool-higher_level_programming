#!/usr/bin/python3
"""Module that checks subclass-based inheritance.

This module provides a function that determines whether an object is an instance
of a class that inherited (directly or indirectly) from a specified class.

Functions:
    inherits_from(obj, a_class): Returns True if `obj` is an instance of a subclass
    of `a_class` (excluding instances that are exactly of type `a_class`).
"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a subclass of a_class.

    This function returns True if the specified object is an instance of a class
    that inherited (either directly or indirectly) from the specified class.
    It returns False if the object is an instance of `a_class` itself.

    Args:
        obj (any): The object to inspect.
        a_class (type): The reference class to compare against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class`
        (but not `a_class` itself), False otherwise.

    Examples:
        >>> inherits_from(True, int)
        True
        >>> inherits_from(3, int)
        False
        >>> inherits_from("hello", object)
        True
    """
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    return False
