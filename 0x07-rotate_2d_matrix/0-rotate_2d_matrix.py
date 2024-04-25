#!/usr/bin/python3
"""Perform 2D matrix rotation."""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix in-place by 90 degrees clockwise.

    Args:
        matrix (list[list]): The 2D matrix to be rotated.

    Returns:
        None: The matrix is rotated in-place.
    """
    size = len(matrix)  # Get the size of the matrix
    # Iterate over each layer of the matrix
    for row in range(size // 2):
        # Iterate over each element in the current layer
        for col in range(row, size - row - 1):
            # Perform the 4-way swap of elements
            temp = matrix[row][col]
            matrix[row][col] = matrix[size - 1 - col][row]
            matrix[size - 1 - col][row] = matrix[
                size - 1 - row][size - 1 - col]
            matrix[size - 1 - row][size - 1 - col] = matrix[
                col][size - 1 - row]
            matrix[col][size - 1 - row] = temp
