#!/usr/bin/python3
"""
Module defining mixin classes for swimming and flying behaviors,
and a Dragon class that combines both capabilities.
"""


class SwimMixin:
    """
    Mixin class providing swimming behavior.

    Methods:
        swim(): Prints a message indicating the creature is swimming.
    """
    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing flying behavior.

    Methods:
        fly(): Prints a message indicating the creature is flying.
    """
    def fly(self):
        """Prints a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a Dragon that can swim, fly, and roar.

    Inherits:
        SwimMixin: Provides swimming behavior.
        FlyMixin: Provides flying behavior.

    Methods:
        roar(): Prints a message indicating the dragon is roaring.
    """
    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")
