#!/usr/bin/python3
"""
This function defines a Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(len(prev_row) - 1):
            new_value = prev_row[i] + prev_row[i + 1]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle

