#!/usr/bin/python3
"""
rectangle.py

Module contenant la classe Rectangle pour représenter un rectangle
avec gestion des attributs width et height via des propriétés,
et calcul des aires, périmètres, et affichage textuel.

Ce module ne dépend d'aucune autre bibliothèque externe.
"""


class Rectangle:
    """
    Represents a rectangle with width and height attributes.

    Attributes:
        width (int): The width of the rectangle (private, must be >= 0).
        height (int): The height of the rectangle (private, must be >= 0).

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle
        using '#' characters.
        __repr__(): Returns a string representation to recreate
        the rectangle object.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        int: The width of the rectangle.

        Raises:
            TypeError: If assigned value is not an integer.
            ValueError: If assigned value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.

        Raises:
            TypeError: If assigned value is not an integer.
            ValueError: If assigned value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area computed as width * height.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter computed as 2 * (width + height),
                 or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns the string representation of the rectangle
        using the '#' character.

        Returns:
            str: A string drawing of the rectangle or an empty string if
                 width or height is 0.
        """
        lines = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a string representation that can be used to recreate
        the Rectangle instance using eval().

        Returns:
            str: The string representation of the Rectangle.
        """
        return (f"Rectangle({self.__width}, {self.__height})")
