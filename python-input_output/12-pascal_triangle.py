#!/usr/bin/python3
"""
Module 12-pascal_triangle

Provides a function to generate Pascal's Triangle up to a given number of rows.

Functions:
    pascal_triangle(n): Returns a list of lists representing Pascal's Triangle of n.
"""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list[list[int]]: A list of lists of integers representing Pascal's Triangle.
        Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(4)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)
        prev_row = row

    return triangle