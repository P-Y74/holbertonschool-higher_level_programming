#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position without modifying the original list.

    Args:
        my_list (list): The original list of elements.
        idx (int): The index at which to replace the element.
        element: The new element to insert.

    Returns:
        list: A new list with the element replaced if the index is valid,
              otherwise a copy of the original list.
    """
    copy_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return(copy_list)
    copy_list[idx] = element
    return(copy_list)
