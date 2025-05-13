#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints the dictionary with keys sorted in alphabetical order.

    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
