#!/usr/bin/python3
"""contain is_same_class(obj, a_class) function"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly an instance of the
    specified class; otherwise False.

    Args:
        obj (object): the object to test for
        a_class (type): a type

    Returns:
        bool: return True if it is an instacne of a_class, else False.
    """
    return isinstance(obj, a_class) and not issubclass(object, a_class)
