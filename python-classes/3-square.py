#!/usr/bin/python3
"""Module defining the Square class with size validation and area computation.

This module provides a Square class that allows instantiation of a square
object with an optional size. It includes validation to ensure the size is a
non-negative integer and provides a method to compute the square's area.
"""


class Square:
    """Represents a square.

    This class defines a square with a private size attribute and validates the
    value during instantiation. It also provides a method to calculate the area
    of the square.
    """
    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int, optional): The size of the square (length of one side).
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
