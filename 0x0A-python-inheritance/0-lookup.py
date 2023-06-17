#!/usr/bin/python3
"""contains lookup(obj)"""


def lookup(obj):
    """a function that returns the list of available attributes
    and methods of an object:

    Args:
        obj (object): the object

    Returns:
        list: the list of available attributes
    """
    return dir(obj)
