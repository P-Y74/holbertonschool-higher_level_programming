#!/usr/bin/python3
"""
Module for serializing and deserializing custom Python objects using pickle.

This module defines the CustomObject class which supports serialization to
a file and deserialization from a file, with proper exception handling for
file-related errors.
"""


import pickle


class CustomObject:
    """
    A custom object class representing a person with attributes name, age,
    and student status.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student or not.

    Methods:
        serialize(filename):
            Serializes the current instance to a file using pickle.
        deserialize(filename):
            Class method that deserializes and returns an instance from
            a pickle file.
        display():
            Prints the object's attributes in a formatted way.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serializes the current instance to a binary file using pickle.

        Args:
            filename (str): The file path where the object will be saved.

        Returns:
            None if an error occurs during serialization
            (e.g., IOError, TypeError).
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except (pickle.PicklingError, IOError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject instance from a binary pickle file.

        Args:
            filename (str): The file path from which to load the object.

        Returns:
            CustomObject instance if successful, otherwise None if file
            is missing or corrupted.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (pickle.PicklingError, IOError):
            return None

    def display(self):
        """
        Prints the attributes of the CustomObject instance.

        Format:
            Name: <name>
            Age: <age>
            Is Student: <is_student>
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
