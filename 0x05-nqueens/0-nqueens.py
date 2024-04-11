#!/usr/bin/python3
"""N-Queens module."""

import sys


def is_safe(board, row, col, board_size):
    """
    Check if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (List[List[int]]): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        board_size (int): The size of the board.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, board_size), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_recursive(board, col, board_size, solutions):
    """
    Utility function to solve the N-Queens problem recursively.

    Args:
        board (List[List[int]]): The current state of the chessboard.
        col (int): The current column index being processed.
        board_size (int): The size of the board.
        solutions (List[List[int]]): List to store all possible solutions.
    """
    # If all queens are placed then add the solution
    if col == board_size:
        solution = []
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Consider this column and try placing this queen in all rows
    for i in range(board_size):
        if is_safe(board, i, col, board_size):
            board[i][col] = 1
            solve_nqueens_recursive(board, col + 1, board_size, solutions)
            board[i][col] = 0


def solve_nqueens(board_size):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        board_size (str): The size of the board.
    """
    if not board_size.isdigit():
        print("Board size must be a number")
        sys.exit(1)
    board_size = int(board_size)
    if board_size < 4:
        print("Board size must be at least 4")
        sys.exit(1)

    board = [[0] * board_size for _ in range(board_size)]
    solutions = []
    solve_nqueens_recursive(board, 0, board_size, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens <board_size>")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
