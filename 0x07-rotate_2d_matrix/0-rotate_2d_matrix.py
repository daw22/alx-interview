#!/usr/bin/python3

"""
Rotates a 2D Matrix 90 Degrees Clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates 2D Matrix(nXn) 90 degrees clockwise
    & the matrix is  edited in place(no coping)
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
