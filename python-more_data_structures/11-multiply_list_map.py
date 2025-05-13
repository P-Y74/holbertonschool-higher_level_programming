#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Multiply all elements of a list by a given number using map.

    Args:
    my_list (list): List of integers.
    number (int): Number to multiply each element by.

    Returns:
    list: New list with all values multiplied by number.
    """
    new_list = list(map(lambda i: i * number, my_list))
    return new_list
