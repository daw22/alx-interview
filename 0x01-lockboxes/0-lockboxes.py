#!/usr/bin/python3
"""
The Lockboxes Problem
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes: A list of lists, where each inner list contains
        keys to other boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    def dfs(box_index):
        """
        Dept-first Search
        recursively explore the boxes the can be
        opened using the keys found in the current
        box
        """
        for key in boxes[box_index]:
            if key < n and not visited[key]:
                visited[key] = True
                dfs(key)

    dfs(0)
    return all(visited)
