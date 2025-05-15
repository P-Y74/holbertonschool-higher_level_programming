#!/usr/bin/python3
"""
Module to divide all elements of a matrix by a given divisor.
Validates input matrix and divisor, and returns a new matrix with
elements rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div, rounding to 2 decimals.
    Args:
        matrix (list of list of int/float): Input matrix.
        div (int/float): Divisor.
    Raises:
        TypeError: If matrix or div is invalid.
        ZeroDivisionError: If div is zero.
    Returns:
        new matrix with divided and rounded elements.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2)for num in row]for row in matrix]
