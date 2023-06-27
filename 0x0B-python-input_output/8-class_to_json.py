#!/usr/bin/python3
"""contains def class_to_json(obj) function"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Args:
        obj (object): the object

    Returns:
        dict: the dictionary representation of the object
    """
    return obj.__dict__
