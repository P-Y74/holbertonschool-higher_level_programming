#!/usr/bin/python3
"""
Module counted_iterator

This module defines the CountedIterator class, which wraps an iterable
and tracks
how many items have been retrieved from it using the iterator protocol.
"""


class CountedIterator:
    """An iterator that counts how many items have been fetched.

    This class wraps a standard iterable and provides a counter that increments
    each time an item is accessed using `next()`. It is useful for monitoring
    progress or behavior during iteration.

    Attributes:
        iterator (iterator): The internal iterator derived from the given
        iterable.
        counter (int): The number of items retrieved so far.
    """

    def __init__(self, iterable):
        """Initializes the CountedIterator with an iterable.

        Args:
            iterable (iterable): Any iterable object
            (e.g., list, tuple, generator).
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Returns the iterator object itself.

        Returns:
            CountedIterator: The iterator instance.
        """
        return self

    def __next__(self):
        """Retrieves the next item from the iterator and increments
        the counter.

        Returns:
            Any: The next item from the iterable.

        Raises:
            StopIteration: When there are no more items to retrieve.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Returns the number of items retrieved so far.

        Returns:
            int: The number of items accessed via `next()`.
        """
        return self.counter
