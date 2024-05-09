#!/usr/bin/python3
"""Calculate the perimeter of an island."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]): A list of lists representing the grid where:
        - 0 represents water
        - 1 represents land

    Returns:
    int: The perimeter of the island.

    Constraints:
    - grid is rectangular, with its width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing)
    - The island doesn’t have “lakes” (water inside that isn’t connected to
    - the water surrounding the island)
    """
    if not grid:
        return 0

    island_perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                # Each land cell contributes 4 sides peri
                island_perimeter += 4

                # Check neighbors
                if row > 0 and grid[row - 1][col] == 1:
                    # Subtract 2 for each adjacent land cell
                    island_perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    island_perimeter -= 2

    return island_perimeter
