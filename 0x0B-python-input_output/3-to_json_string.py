#!/usr/bin/python3
"""contains def to_json_string(my_obj) function"""


import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)

    Args:
        my_obj (str): the object of type str

    Returns:
        str: the JSON representation as string
    """
    return json.dumps(my_obj)
