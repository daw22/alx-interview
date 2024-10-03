#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime-picking game.

    Args:
        x: The number of rounds.
        nums: A list, where each element is the 'n' value for a round.

    Returns:
        The name of the player who won the most rounds ("Maria" or "Ben"),
        or None if a winner cannot be determined.
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def play_round(n):
    """
    Simulates a round of the prime-picking game.

    Args:
        n: The upper limit of the consecutive integer set (1 to n).

    Returns:
        The name of the winner of the round ("Maria" or "Ben").
    """

    numbers = list(range(1, n + 1))  # Create the set of numbers
    turn = "Maria"  # Maria always goes first

    while True:
        prime_found = False
        for i in range(2, len(numbers)):  # Start checking for primes from 2
            if numbers[i] != 0:  # If the number hasn't been removed
                prime_found = True
                for j in range(i, len(numbers), i):
                    numbers[j] = 0  # Remove the prime and its multiples
                break  # Move to the next player's turn

        if not prime_found:
            # No more primes to pick, the current player loses
            return "Ben" if turn == "Maria" else "Maria"

        turn = "Ben" if turn == "Maria" else "Maria"
