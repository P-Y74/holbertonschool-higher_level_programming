#!/usr/bin/python3
def islower(c):
    """
    Check if a character is a lowercase letter.

    Args:
        c (str): A single character.

    Returns:
        bool: True if c is a lowercase letter, False otherwise.
    """
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
