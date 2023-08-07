#!/usr/bin/python3
"""
Script that computes a minimum operations
needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method for computing the minimum number
    of operations for task Copy All and Paste
    Args:
        n: input value
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n //= i  # Use integer division
                factor_list.append(i)
    return sum(factor_list)  # Return outside the while loop

# Example usage


result = minOperations(12)
print("Minimum operations:", result)
