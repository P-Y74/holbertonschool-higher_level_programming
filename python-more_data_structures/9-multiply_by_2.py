#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    This function takes a dictionary and returns a new dictionary
    where all values are multiplied by 2.

    Args:
        a_dictionary (dict): A dictionary where the values are integers.

    Returns:
        dict: A new dictionary where each value is the result of multiplying
              the original value by 2.
    """
    new_dictionary = {}
    for add in a_dictionary:
        new_dictionary[add] = a_dictionary[add] * 2
    return new_dictionary
