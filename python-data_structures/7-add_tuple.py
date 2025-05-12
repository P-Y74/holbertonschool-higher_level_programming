#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.

    If a tuple has less than 2 elements, it is padded with 0s.
    If a tuple has more than 2 elements, only the first 2 are used.

    Args:
        tuple_a (tuple): First input tuple.
        tuple_b (tuple): Second input tuple.

    Returns:
        tuple: A tuple of 2 integers, the sum of the inputs.
    """
    new_tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a[:2]))
    new_tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b[:2]))
    return tuple(map(lambda i, j: i + j, new_tuple_a, new_tuple_b))
