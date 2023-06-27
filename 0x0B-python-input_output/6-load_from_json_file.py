#!/usr/bin/python3
"""contain def load_from_json_file(filename) function"""


import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file and returns it

    Args:
        filename (str): the name of the file.

    Returns:
        obj: the created object
    """
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
