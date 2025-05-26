#!/usr/bin/python3
"""
geometry.py

Module providing base and derived classes for geometry operations.

This module defines three classes:
- BaseGeometry: A base class with interface methods for geometry operations.
- Rectangle: A subclass of BaseGeometry representing a rectangle.
- Square: A subclass of Rectangle representing a square.

Classes:
    BaseGeometry
    Rectangle
    Square
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

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area computed as width * height.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation in the format
            "[Rectangle] width/height".
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Represents a square with all sides of equal length.

    Attributes:
        __size (int): The size of the square's sides (private).

    Methods:
        __init__(size): Constructor that validates and sets the size.
        area(): Calculates the area of the square.
    """

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area computed as size * size.
        """
        return self.__size * self.__size
