#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    If the key exists, it is removed from the dictionary.
    If the key does not exist, the dictionary remains unchanged.

    Args:
        a_dictionary (dict): The dictionary from which to remove the key.
        key (str, optional): The key to remove. Defaults to an empty string.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
