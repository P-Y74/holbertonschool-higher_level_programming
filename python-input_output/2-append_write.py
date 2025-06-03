#!/usr/bin/python3
"""
Module append_write

This module provides a function to append a string to the end of a text file (UTF-8)
and return the number of characters added. If the file does not exist, it is created.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns the number of characters added.

    This function uses the with statement for file handling. It creates the file
    if it doesn't exist and appends the given text to the end of the file.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty string.
        text (str): The string to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.

    Note:
        This function does not handle file permission or file-not-found exceptions.
    """
    with open(filename,'a', encoding='utf-8') as file:
        return (file.write(text))
