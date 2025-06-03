#!/usr/bin/python3
"""
Module student

This module defines a `Student` class with basic attributes and
a method to retrieve a dictionary representation suitable for
JSON serialization.

No external modules are used.
"""


class Student:
    """Defines a student with a first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing all serializable attributes
            of the instance (suitable for JSON serialization).
        """
        return self.__dict__
