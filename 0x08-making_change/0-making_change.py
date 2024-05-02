#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list of int): Values of the coins in possession.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
             If total is 0 or less, returns 0.
             If total cannot be met by any coins, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize a list to store minimum coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed for total of 0

    # Iterate through amounts from 1 to total
    for i in range(1, total + 1):
        # Check each coin value
        for coin in coins:
            if i - coin >= 0:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
