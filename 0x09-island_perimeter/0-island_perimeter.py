#!/usr/bin/python

"""
Island perimeter problem
"""


def island_perimeter(grid):
    """
    solution for island perimeter problem
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num = grid[i][j]
            if num == 1:
                nums = []
                if i > 0:
                    nums.append(grid[i - 1][j])
                if j > 0:
                    nums.append(grid[i][j - 1])
                if i < len(grid[i]) - 1:
                    nums.append(grid[i + 1][j])
                if j < len(grid):
                    nums.append(grid[i][j + 1])
                perimeter += 4 - sum(nums)
    return perimeter
