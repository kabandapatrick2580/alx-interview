#!/usr/bin/python3
"""This function generates Pascal's triangle up to 
the specified number of rows."""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.
    
    Arguments:
    n -- The number of rows to generate in the triangle.
    
    Returns:
    A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
