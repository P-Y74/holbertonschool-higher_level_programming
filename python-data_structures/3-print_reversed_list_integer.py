#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
        my_list (list): The list of integers to print.

    Returns:
        None
    """
    for i in my_list[::-1]:
        print("{}".format(i))
