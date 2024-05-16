#!/usr/bin/python3
"""Prime_game module."""


def is_Itprime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime,
        False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def The_playround(n):
    """
    Simulate a round of the game.

    Args:
        n (int): The upper limit of the consecutive integers.

    Returns:
        str: The name of the player who wins the round.
    """
    prime_count = sum(1 for i in range(2, n + 1) if is_Itprime(i))
    return "Maria" if prime_count % 2 == 1 else "Ben"


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the upper
                    limits for each round.

    Returns:
        str or None: The name of the player who won the most rounds,
        or None if the winner cannot be determined.
    """
    m_maria_wins = 0
    b_ben_wins = 0
    for n in nums:
        winner = The_playround(n)
        if winner == "Maria":
            m_maria_wins += 1
        elif winner == "Ben":
            b_ben_wins += 1
    if m_maria_wins > b_ben_wins:
        return "Maria"
    elif m_maria_wins < b_ben_wins:
        return "Ben"
    else:
        return None
