#!/usr/bin/python3
"""contains a class Student"""


class Student:
    """a class Student"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns  a dictionary representation of a Student instance. If attrs
        is a list of strings, only attribute names contained in this list must
        be retrieved.

        Args:
            attrs (list): list of attribute to be retrieved as string.
        """
        instance_attr = self.__dict__
        if isinstance(attrs, list):
            tmp_dict = dict()
            for key in attrs:
                if isinstance(key, str):
                    if key in instance_attr:
                        tmp_dict[key] = instance_attr[key]
                else:
                    break
            else:
                instance_attr = tmp_dict
        return instance_attr


