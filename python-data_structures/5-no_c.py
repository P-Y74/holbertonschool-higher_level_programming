#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.
    """
    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
    return (new_string)
