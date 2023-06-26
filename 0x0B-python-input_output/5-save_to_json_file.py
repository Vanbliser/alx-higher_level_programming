#!/usr/bin/python3
"""contains def save_to_json_file(my_obj, filename) function"""


import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (obj): the object to write to file
        filename (str): the name of the file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
