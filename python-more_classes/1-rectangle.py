#!/usr/bin/python3
"""
This module defines a `Rectangle` class to model a rectangle
with width and height attributes, including proper data validation
using property decorators.

Classes:
    Rectangle

Example:
    >>> r = Rectangle(3, 4)
    >>> print(r.width)
    3
    >>> print(r.height)
    4
    >>> r.width = 10
    >>> print(r.width)
    10
"""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance with optional
            width and height.

        width(self):
            Getter for the width of the rectangle.

        width(self, value):
            Setter for the width of the rectangle. Ensures it is a
            non-negative integer.

        height(self):
            Getter for the height of the rectangle.

        height(self, value):
            Setter for the height of the rectangle. Ensures it is a
            non-negative integer.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width to assign.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height to assign.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
