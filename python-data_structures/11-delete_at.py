#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list from which the item will be deleted.
        idx (int): The index of the item to delete. If the index is
        out of range, the list remains unchanged.

    Returns:
        list: The list after deletion. If the index is invalid,
        the original list is returned unchanged.

    Notes:
        - If idx is negative or out of range, the original list is returned
        without modification.
        - The function does not use the pop() method.
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    del my_list[idx]
    return (my_list)
