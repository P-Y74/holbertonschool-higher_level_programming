#!/usr/bin/python3
"""
Module: 0-read_file

This module provides a function to read and print the contents
of a UTF-8 encoded text file to standard output.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path to the text file to be read.

    Notes:
        - Uses the with statement to handle file context management.
        - File permissions or exceptions related to missing files
          are not handled explicitly.
        - Only built-in features are used; no imports allowed.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
