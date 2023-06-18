#!/usr/bin/python3
"""contain is_kind_of_class(obj, a_class): function"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj (object): the object to perform the check on
        a_class (type): the type to check against

    Returns:
        bool: True if so, else False
    """
    return isinstance(obj, a_class)
