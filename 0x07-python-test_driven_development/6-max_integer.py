#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(l=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if not isinstance(l, list):
        raise TypeError("l must be a list of integers")
    if len(l) == 0:
        return None
    if not all(list(map(lambda x: check(x), l))):
        raise TypeError("l must be a list of integers") 
    result = l[0]
    i = 1
    while i < len(l):
        if l[i] > result:
            result = l[i]
        i += 1
    return result


def check(x):
    """a function that returns True if x is an integer and not too
    large.

    Args:
        x (int): the value to check
    Returns:
        bool: True if so, else False
    """
    if isinstance(x, bool):
        return False
    if not isinstance(x, int):
        return False
    if x == x+1:
        return False
    return True
