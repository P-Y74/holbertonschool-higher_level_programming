#!/usr/bin/python3
"""
This module provides a function to add two integers.
It takes two parameters, casts them to integers if necessary,
returns their sum. It raises a TypeError if inputs are not int or float.
"""


def add_integer(a, b=98):
    """
    Adds two integers after casting floats to int. Raises Typerror
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
