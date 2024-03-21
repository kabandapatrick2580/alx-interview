#!/usr/bin/python3
"""
Module for minimum operations task.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
