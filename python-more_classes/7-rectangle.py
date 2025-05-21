#!/usr/bin/python3
"""
This module defines a Rectangle class that represents a rectangle
by its width and height, and provides methods to calculate area,
perimeter, and a string representation of the rectangle.

It also tracks the number of Rectangle instances created and deleted
using the class attribute `number_of_instances`.

Classes:
    Rectangle
"""


class Rectangle:
    """
    Represents a rectangle with width and height attributes.

    Attributes:
        width (int): The width of the rectangle (private, must be >= 0).
        height (int): The height of the rectangle (private, must be >= 0).
        number_of_instances (int): Class attribute tracking the number of
            Rectangle instances currently alive.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle
            using '#' characters.
        __repr__(): Returns a string representation to recreate
            the rectangle object.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance and increments the class
        attribute `number_of_instances`.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        using the character(s) stored in `print_symbol`.

        Returns:
            str: A string drawing of the rectangle or an empty string if
                 width or height is 0.
        """
        lines = []
        symbol = str(getattr(self, "print_symbol", type(self).print_symbol))
        if self.__width == 0 or self.__height == 0:
            return ""
        for _ in range(self.__height):
            lines.append(symbol * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Returns a string representation that can be used to recreate
        the Rectangle instance using eval().

        Returns:
            str: The string representation of the Rectangle.
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """
        Destructor for the Rectangle instance.

        Prints a farewell message when the instance is about to be destroyed,
        and decrements the class attribute `number_of_instances`.

        Note:
            This method is called when the instance is garbage collected.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
