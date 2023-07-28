#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2 dimensional array.

    Returns:
        A new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
        Initial matrix should not be modified
    """
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: x ** 2, row))
        new_matrix.append(new_row)
    return new_matrix
