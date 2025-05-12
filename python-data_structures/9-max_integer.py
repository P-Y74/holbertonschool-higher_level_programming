#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds and returns the biggest integer in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        int or None: The largest integer in the list.
                     If the list is empty, returns None.
    """
    if len(my_list) == 0:
        return (None)
    max_int = my_list[0]
    for value in my_list:
        if value > max_int:
            max_int = value
    return (max_int)
