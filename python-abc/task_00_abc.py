#!/usr/bin/python3
"""Animal sound module using Abstract Base Classes (ABCs).

This module defines an abstract base class `Animal` and two concrete
implementations: `Dog` and `Cat`. Each subclass must implement
the `sound` method.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal.

    All subclasses must implement the `sound` method to define
    the specific sound the animal makes.
    """

    @abstractmethod
    def sound(self):
        """Produce the sound made by the animal.

        Returns:
            str: A string representing the animal's sound.
        """
        pass


class Dog(Animal):
    """Concrete implementation of an Animal representing a dog."""

    def sound(self):
        """Return the sound made by a dog.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """Concrete implementation of an Animal representing a cat."""

    def sound(self):
        """Return the sound made by a cat.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
