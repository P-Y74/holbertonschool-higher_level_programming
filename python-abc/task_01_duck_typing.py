#!/usr/bin/python3
"""Shapes module using Abstract Base Classes (ABCs).

This module defines an abstract base class `Shape` and two concrete
implementations: `Circle` and `Rectangle`. It demonstrates the use
of ABCs to enforce implementation of common interface methods.

Classes:
    Shape: Abstract base class defining the interface for shapes.
    Circle: Concrete implementation of a circle.
    Rectangle: Concrete implementation of a rectangle.

Functions:
    shape_info(shape): Prints the area and perimeter of a shape.
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class representing a geometric shape.

    All shapes must implement the `area` and `perimeter` methods.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return pi * 2 * self.radius


class Rectangle(Shape):
    """Class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of a given shape.

    Args:
        shape (Shape): An instance of a class derived from Shape.
    """
    print("Area: {}".format(repr(shape.area())))
    print("Perimeter: {}".format(repr(shape.perimeter())))
