#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format(), safely.

    Args:
        value: The value to print.

    Returns:
        bool: True if value is an integer and was printed successfully,
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
