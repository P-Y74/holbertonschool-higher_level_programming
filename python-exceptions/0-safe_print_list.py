#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints up to x elements from a given list safely.

    Args:
        my_list (list, optional): The list to print elements from.
        Defaults to [].
        x (int, optional): The number of elements to attempt to print.
        Defaults to 0.

    Returns:
        int: The actual number of elements successfully printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            pass
    print()
    return count
