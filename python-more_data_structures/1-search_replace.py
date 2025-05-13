#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a list with a new element.

    Args:
        my_list (list): The original list of elements.
        search: The element to be replaced.
        replace: The new element to replace with.

    Returns:
        list: A new list with all occurrences of 'search' replaced by 'replace'.
    """
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
