#!/usr/bin/python3
"""
student module

This module defines a Student class with basic attributes and a method
to serialize selected attributes into a dictionary for JSON operations.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If `attrs` is a list of strings, only those attributes will be included
        in the resulting dictionary, provided they exist. Otherwise,
        all attributes are included.

        Args:
            attrs (list, optional): A list of attribute names to include.
                Defaults to None.

        Returns:
            dict: A dictionary containing the requested attributes.
        """
        if isinstance(attrs, list):
            empty_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    empty_dict[name] = self.__dict__[name]
            return empty_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary with keys corresponding to
                         attribute names and values to set on the instance.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
