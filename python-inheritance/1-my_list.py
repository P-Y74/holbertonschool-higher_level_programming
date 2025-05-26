#!/usr/bin/python3
"""Module that defines a subclass of the built-in list type.

This module defines the MyList class, which inherits from the built-in
list class and adds a method to print the list in a sorted order.
"""


class MyList(list):
    """Custom list class that extends the built-in list.

    This class inherits from Python's built-in list and adds a method
    to print the elements of the list in ascending sorted order without
    modifying the original list.
    """
    def print_sorted(self):
        """Print the list elements in ascending sorted order.

        The method uses the built-in sorted() function to display a sorted
        version of the list, without altering the original list instance.
        """
        print(sorted(self))
