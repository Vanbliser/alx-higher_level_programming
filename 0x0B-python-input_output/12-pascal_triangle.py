#!/usr/bin/python3
"""contains def pascal_triangle(n) function"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers representing the
    Pascal’s triangle of n.

    Args:
        n (int): You can assume n will be always an integer

    Returns:
        str: a list of lists of integers representing the Pascal’s
            triangle of n.
            returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    prev_triangle = pascal_triangle(n-1)
    a = 0
    next_list = [[]]
    for b in prev_triangle[-1]:
        next_list[0].append(a + b)
        a = b
    next_list[0].append(b + 0)
    return prev_triangle + next_list
