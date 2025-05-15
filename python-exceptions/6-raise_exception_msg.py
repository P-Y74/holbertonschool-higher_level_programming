#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a NameError exception with a custom message.

    Args:
        message (str): The message to include in the NameError.
        Defaults to an empty string.

    Raises:
        NameError: Always raised with the provided message.
    """
    raise NameError(message)
