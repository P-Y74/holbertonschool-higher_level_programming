#!/usr/bin/python3
"""
Module defining a Rectangle class with width and height attributes,
including validation and methods to compute area and perimeter.

Classes:
    Rectangle

Example:
    >>> r = Rectangle(3, 4)
    >>> r.width
    3
    >>> r.height
    4
    >>> r.area()
    12
    >>> r.perimeter()
    14
"""


class Rectangle:
    """
    Represents a rectangle defined by width and height.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width=0, height=0):
            Initializes a new Rectangle instance.

        width(self):
            Getter for the width attribute.

        width(self, value):
            Setter for the width attribute with validation.

        height(self):
            Getter for the height attribute.

        height(self, value):
            Setter for the height attribute with validation.

        area(self):
            Returns the area of the rectangle.

        perimeter(self):
            Returns the perimeter of the rectangle,
            or 0 if width or height is 0.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with optional width and height.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: Perimeter (2*(width + height)) or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
