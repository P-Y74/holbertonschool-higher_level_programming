#!/usr/bin/python3
"""Module save_to_json_file

This module provides a function to serialize a Python object
and save it as a JSON-formatted file.
"""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    This function serializes a Python object into JSON format and writes
    it directly to a file. If the file already exists, its contents
    are overwritten.
    The file is created if it does not exist.

    Args:
        my_obj (object): The Python object to serialize.
        filename (str): The name of the file to write to.

    Returns:
        None

    Example:
        save_to_json_file({"name": "Alice"}, "data.json")
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
