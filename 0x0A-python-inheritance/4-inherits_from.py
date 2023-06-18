#!/usr/bin/python3
"""contains inherits_from(obj, a_class) function"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class; otherwise
    False.

    Args:
        obj (object): the object to perform the check on
        a_class (type): the type to check against

    Returns:
        bool: True is yes, otherwise False
    """
    return isinstance(obj, a_class) and (type(obj) != a_class)
