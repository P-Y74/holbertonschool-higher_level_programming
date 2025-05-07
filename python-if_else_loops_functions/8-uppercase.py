#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        str (str): The input string.

    Notes:
        - Only two print functions are used.
        - Does not use str.upper() or any imports.
    """
    for i in str:
        print("{}".format(chr(ord(i) - 32)
                          if 97 <= ord(i) <= 122 else i), end="")
    print()
