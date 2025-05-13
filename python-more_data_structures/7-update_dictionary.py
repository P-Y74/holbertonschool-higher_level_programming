#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Updates or adds a key/value pair in a dictionary.

    If the key exists, its value is updated.
    If the key does not exist, it is added to the dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to update or add.
        value (any): The value to assign to the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
