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
    if a is None:
        raise TypeError("enter at least one integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
