#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print all integers of a list, one per line.

    Args:
        my_list (list, optional): A list of integers to print. Defaults to an empty list.

    Returns:
        None
    """
    for i in my_list:
        print("{}".format(i))
