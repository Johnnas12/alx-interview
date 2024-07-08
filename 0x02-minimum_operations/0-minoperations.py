#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def minOperations(n):
    """Create a function def minOperations(n): that returns a operation
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
