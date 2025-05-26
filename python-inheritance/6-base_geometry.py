#!/usr/bin/python3
"""Module defining a base geometry class.

This module contains the BaseGeometry class which serves as a base class
for geometric shapes. It defines an area method that is expected to be
implemented by subclasses.
"""


class BaseGeometry:
    """Base class for geometric shapes.

    This class provides a template for geometry-related classes. The `area`
    method is intended to be overridden by subclasses to compute the area
    of the shape.

    Methods:
        area(): Raises an Exception indicating the method is not implemented.
    """
    def area(self):
        """Calculate the area of the geometry.

        This method should be overridden by subclasses. Raises an Exception
        if called directly.

        Raises:
            Exception: Always raised with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
