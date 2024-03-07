#!/usr/bin/python3
"""This function generates Pascal's triangle up to 
    the specified number of rows."""


def pascal_triangle(p):
    """
    Generates Pascal's triangle up to the specified number of rows.
    
    Arguments:
    p -- The number of rows to generate in the triangle.
    
    Returns:
    A list of lists representing Pascal's triangle.
    """
    if p <= 0:
        return []

    triangle = []
    for m in range(p):
        row = [1] * (m + 1)
        if m > 1:
            for n in range(1, m):
                row[n] = triangle[m - 1][n - 1] + triangle[m - 1][n]
        triangle.append(row)

    return triangle
