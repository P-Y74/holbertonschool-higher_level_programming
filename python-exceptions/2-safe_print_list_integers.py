#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Tries to print only the integer values in the list using the format "{:d}".
    Silently skips any value that raises a ValueError or TypeError.
    
    Args:
        my_list (list, optional): The list containing any type of elements. Defaults to [].
        x (int): The number of elements to attempt to print.

    Returns:
        int: The number of integers successfully printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]),end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
