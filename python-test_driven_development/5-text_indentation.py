#!/usr/bin/python3
"""
This module provides a function that prints a text with two new lines
after each of the following characters: '.', '?' and ':'.
Functions:
    text_indentation(text): Prints the formatted text with proper indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?', ':'
    Args:
        text (str): The input string
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""
    for char in text:
        current_line += char
        if char in ".?:":
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip(), end="")
