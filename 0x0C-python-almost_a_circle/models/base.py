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
            type(self).__nb_objects += 1
            self.id = Base.__nb_objects
