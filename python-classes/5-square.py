#!/usr/bin/python3
"""Module that defines a Square class.

This module provides a class to represent a square with methods
to compute its area and to print a visual representation using `#`.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of one side of the square (private).
    """
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for the square size.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the square size with validation.

        Args:
            value (int): The new size to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the `#` character.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
        for _ in range(int(self.__size)):
            print("#" * self.__size)
