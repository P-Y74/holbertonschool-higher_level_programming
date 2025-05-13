#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
        my_list (list): List of integers.

    Returns:
        int: Sum of unique integers.
    """
    my_list = set(my_list)
    result = sum(my_list)
    return result
