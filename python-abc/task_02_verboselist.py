#!/usr/bin/python3
"""
Module verbose_list.

This module contains the VerboseList class, which extends the built-in
list class
to provide notifications when items are added or removed.

Classes:
    VerboseList -- list subclass that prints messages on modifications
"""


class VerboseList(list):
    """
    A list subclass that prints a notification message whenever items are
    added or removed.

    Methods:
        append(item): Adds an item to the list and prints a message.
        extend(iterable): Extends the list by appending elements from
        the iterable and prints a message.
        remove(item): Removes the first occurrence of the item from the list
        and prints a message.
        pop(index=-1): Removes and returns the item at the given index
        (default last) and prints a message.
    """

    def append(self, item):
        """
        Append an item to the list.

        Args:
            item: The item to be appended.

        Prints:
            A message indicating that the item was added.
        """
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, x):
        """
        Extend the list by appending elements from the iterable.

        Args:
            iterable: An iterable with items to add to the list.

        Prints:
            A message indicating the number of items added.
        """
        super().extend(x)
        print(f"Extended the list with {[len(x)]} items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list.

        Args:
            item: The item to be removed.

        Prints:
            A message indicating the item removed.
        """
        super().remove(item)
        print(f"Removed {[item]} from the list.")

    def pop(self, index=-1):
        """
        Remove and return the item at the given index.

        Args:
            index (int, optional): The index of the item to remove.
            Defaults to -1 (last item).

        Returns:
            The removed item.

        Prints:
            A message indicating the item popped.
        """
        item = super().pop(index)
        print(f"Popped {[item]} from the list.")
