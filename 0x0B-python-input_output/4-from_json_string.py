#!/usr/bin/python3
"""contains def from_json_string(my_str) function"""


import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): a JSON string

    Returns:
        obj: a python data structure object
    """
    return json.loads(my_str)
