#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result
    in exactly n 'H' characters in the file.

    Args:
      n: The desired number of 'H' characters.

    Returns:
      The minimum number of operations needed.
    """

    if n <= 0:
        return 0
    if n == 1:
        return 0  # Already have one 'H'

    operations = 0
    h_count = 1
    clipboard = 1

    while h_count < n:
        """If n is divisible by current h_count, pasting
           is the most efficient way"""
        if n % h_count == 0:
            clipboard = h_count
            operations += 1  # For Copy All

        h_count += clipboard
        operations += 1  # For Paste

    return operations
