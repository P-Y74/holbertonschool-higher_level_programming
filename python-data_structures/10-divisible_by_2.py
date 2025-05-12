#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Function that returns a list of True or False depending on whether
    the numbers in the original list are divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of boolean values (True or False).
    """
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
