#!/usr/bin/python3
"""Square module that defines a Square class inheriting from Rectangle.

This module defines the `Square` class, which is a subclass of `Rectangle`.
It uses validation from the parent class and ensures that both the width
and height are equal, as expected for a square.

Classes:
    Square: Represents a square with equal side lengths. Inherits
    from Rectangle.

Usage Example:
    >>> s = Square(5)
    >>> print(s.area())
    25
"""


Rectangle = __import__('9-rectangle').Rectangle


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
        return self._Rectangle__width * self._Rectangle__height
