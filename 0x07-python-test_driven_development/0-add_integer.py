#!/usr/bin/python3

"""Contains a function add_integer"""


def add_integer(a, b=98):
    """a function that add two integers

    Args:
        a (int): first integer to add
        b (int, optional): second integer to add

    Returns:
        int: the addition of a and b
    """
    inf = float('inf')
    inf_ = float('-inf')
    if a == a+1:
        a = 1
    if b == b+1:
        b = 1
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if result == inf or result == inf_:
        return 1
    return int(a) + int(b)
