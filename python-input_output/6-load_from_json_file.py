#!/usr/bin/python3
"""Module to load a Python object from a JSON file using json.load()."""

import json

def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object parsed from the JSON file.

    Notes:
        - Uses 'with' to open the file.
        - Assumes the file contains valid JSON.
        - Does not handle exceptions.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
