#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers, one row per line.

    Args:
        matrix (list of lists of int): The matrix to be printed.

    Returns:
        None
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), end=" ")
        print()
