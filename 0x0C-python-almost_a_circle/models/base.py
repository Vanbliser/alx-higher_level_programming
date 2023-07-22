#!/usr/bin/python3
"""contain class Base"""


class Base:
    """a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the json representation
        of list_dictionaries
        """
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            from json import dumps
            return dumps(list_dictionaries)
