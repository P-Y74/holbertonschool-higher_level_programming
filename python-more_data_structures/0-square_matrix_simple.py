#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square of all integers in a matrix.

    Args:
        matrix (list of lists of int): A 2D matrix of integers.

    Returns:
        list of lists of int: A new matrix with each integer squared.
        The original matrix is not modified.
    """
    new_matrix = []
    for line in matrix:
        new_matrix.append(list(map(lambda i: i ** 2, line)))
    return new_matrix
