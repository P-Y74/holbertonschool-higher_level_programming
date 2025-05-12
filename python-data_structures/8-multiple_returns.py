#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Return the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing:
            - int: The length of the string.
            - str or None: The first character of the string, or None if the string is empty.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
