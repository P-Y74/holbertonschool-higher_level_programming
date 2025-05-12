#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific index.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to replace.
        element: The new element to insert at the given index.

    Returns:
        list: The modified list if index is valid, or the original list if the index is invalid.
    """
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    my_list[idx] = element
    return my_list
