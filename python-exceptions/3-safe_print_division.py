#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of the division if possible, otherwise None.
    """
    result = None
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
