#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements between two sets.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: Elements that are common to both sets.
    """
    return set_1.intersection(set_2)
