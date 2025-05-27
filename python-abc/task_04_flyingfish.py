#!/usr/bin/python3
"""
Module flying_fish

This module demonstrates multiple inheritance and method resolution order (MRO)
in Python using a Fish, Bird, and FlyingFish class structure.
"""


class Fish:
    """A class representing a fish.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints the natural habitat of the fish.
    """
    def swim(self):
        """Prints a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the natural habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints the natural habitat of the bird.
    """
    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the natural habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, which inherits from Fish and Bird.

    This class overrides the swim, fly, and habitat methods to represent
    its dual nature of living both in water and the air.

    Methods:
        swim(): Prints a message indicating the flying fish is swimming.
        fly(): Prints a message indicating the flying fish is soaring.
        habitat(): Prints the natural habitat of the flying fish.
    """
    def fly(self):
        """Prints a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the natural habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")


def __MRO__():
    """Demonstrates method calls and prints the Method Resolution Order
    (MRO) for FlyingFish."""
    FlyingFish().fly()
    FlyingFish().swim()
    FlyingFish().habitat()
    print(FlyingFish.mro())
