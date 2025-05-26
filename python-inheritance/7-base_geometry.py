#!/usr/bin/python3
"""Module providing a base class for geometry operations.

This module defines the BaseGeometry class which serves as a base for other
geometry-related classes. It provides an interface for computing area and
validating integer inputs.
"""


class BaseGeometry:
    """Base class for geometry objects.

    This class serves as a template for geometry classes. It defines a method
    `area()` that must be implemented by subclasses, and a validator method
    to ensure correct input types.
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
            name (str): The name of the parameter (used in exception messages).
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
