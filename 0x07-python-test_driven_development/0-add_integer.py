#!/usr/bin/python3

"""Contains a function add_integer"""


def add_integer(a, b=98):
    """a function that add two integers
    raises TypeError if parameters does not meet criteria

    Args:
        a (int:float): first integer to add
        b (int:float, optional): second integer to add

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
