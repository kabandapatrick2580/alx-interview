#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing locked boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of the boxes that have been visited
    visited = set()

    # Initialize a stack to keep track of boxes that need to be visited
    stack = [0]  # Start with the first box

    # While there are boxes to visit
    while stack:
        # Pop a box from the stack
        current_box = stack.pop()

        # Mark the current box as visited
        visited.add(current_box)

        # Check if the current box contains keys to other boxes
        for key in boxes[current_box]:
            # If the key opens a box that hasn't been visited yet
            if key < len(boxes) and key not in visited:
                # Add the box to the stack to be visited later
                stack.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)


# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
