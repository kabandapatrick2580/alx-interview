#!/usr/bin/python3
"""0-making_change module."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): List of coin values available.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total amount.
             Returns -1 if the total cannot be met by any combination of coins.

    Note:
        - If total is 0 or less, returns 0.
        - The value of a coin will always be an integer greater than 0.
        - You can assume you have an infinite number of each
            denomination of coin in the list.
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin_value in coins:
        for amount in range(coin_value, total + 1):
            min_coins[amount] = min(min_coins[amount], min_coins[amount - coin_value] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
