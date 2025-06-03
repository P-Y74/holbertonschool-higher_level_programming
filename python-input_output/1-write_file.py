#!/usr/bin/python3
"""
Module write_file

This module provides a function to write a string to a text file (UTF-8)
and return the number of characters written. If the file does not exist,
it is created. If it does exist, its content is overwritten.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of
    characters written.

    This function uses the with statement for file handling. It creates
    the file if it doesn't exist and overwrites it if it does.

    Args:
        filename (str): The name of the file to write to. Defaults to
        an empty string.
        text (str): The string to write into the file. Defaults to
        an empty string.

    Returns:
        int: The number of characters written to the file.

    Note:
        This function does not handle file permission exceptions.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
