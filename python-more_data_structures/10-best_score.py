#!/usr/bin/python3
def best_score(a_dictionary):
    """
Return the key with the highest integer value in a dictionary.

Args:
    a_dictionary (dict): A dictionary where values are integers.

Returns:
    str or None: The key with the highest value, or None if input
    is None or empty.
"""
    if not a_dictionary:
        return None
    result = max(a_dictionary, key=a_dictionary.get)
    return result
