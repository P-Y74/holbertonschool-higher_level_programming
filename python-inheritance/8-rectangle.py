#!/usr/bin/python3
"""Rectangle module that defines a class inheriting from BaseGeometry.

This module defines the `Rectangle` class, which inherits from `BaseGeometry`.
It validates dimensions upon instantiation to ensure they are
positive integers.

Classes:
    Rectangle: Represents a rectangle with validated width and height.

Example:
    >>> r = Rectangle(3, 5)
    >>> print(r)
    <Rectangle object>
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    Represents a rectangle with width and height, both validated as
    positive integers.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(width, height): Constructor that validates and sets
        width and height.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
