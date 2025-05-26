#!/usr/bin/python3
"""
geometry.py

Module providing a base class and a derived class for geometry operations.

This module defines two classes:
- BaseGeometry: A base class with interface methods for geometry operations.
- Rectangle: A subclass of BaseGeometry that represents a rectangle.

Classes:
    BaseGeometry
    Rectangle
"""


class BaseGeometry:
    """Base class for geometry-related operations.

    This class provides a common interface for geometric shapes and includes
    utility methods such as input validation.

    Methods:
        area(): Raises an Exception since it is not implemented in this
        base class.
        integer_validator(name, value): Validates that value is a
        positive integer.
    """

    def area(self):
        """Compute the area of the shape.

        This method is not implemented in the base class and must be overridden
        by subclasses.

        Raises:
            Exception: Always raised with message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a parameter is a positive integer.

        Args:
            name (str): Name of the parameter (used in error messages).
            value (int): Value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
