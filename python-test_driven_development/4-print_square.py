#!/usr/bin/python3
"""
Module 4-print_square
Provides the function print_square that prints a square with the character '#'.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square. Must be an integer >= 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Prints:
        A square of size x size made of '#'.
        Prints nothing if size is 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
