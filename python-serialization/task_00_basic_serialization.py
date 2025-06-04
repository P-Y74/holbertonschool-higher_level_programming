#!/usr/bin/python3
"""
Module for basic serialization and deserialization of Python dictionaries
to/from JSON files.

Provides functions to serialize a dictionary into a JSON file and
to deserialize JSON data from a file back into a Python dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the JSON file to save the serialized data.
                        If the file exists, it will be overwritten.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The Python dictionary deserialized from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
