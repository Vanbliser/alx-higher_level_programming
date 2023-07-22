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
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation
        """
        from json import loads
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the json representation of list_objs to a
        file
        """
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None:
                f.write(Base.to_json_string(None))
            else:
                list_of_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_of_dict))
