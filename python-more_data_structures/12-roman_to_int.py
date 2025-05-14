#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a Roman numeral string to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: The integer representation of the Roman numeral.
             Returns 0 if the input is not a valid string.
    """
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    for i in range(len(roman_string)):
        if (i + 1) < len(roman_string) and values[roman_string[i]] < values[roman_string[i + 1]]:
            total -= values[roman_string[i]]
        else:
            total += values[roman_string[i]]
    return total
