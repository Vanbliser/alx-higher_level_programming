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
    def to_csv_string(list_dictionaries):
        """static method that return a csv representation
        of list_dictionatries
        """
        value = ""
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            for i in list_dictionaries:
                if "size" in i.keys():
                    value += f"{i['id']},{i['size']},{i['x']},{i['y']}\n"
                else:
                    value += f"{i['id']},\
                               {i['width']},\
                               {i['height']},\
                               {i['x']},\
                               {i['y']}\n"
        return value

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation
        """
        if json_string is None or json_string == "":
            return []
        from json import loads
        return loads(json_string)

    @staticmethod
    def from_csv_string(csv_string):
        """static method that returns the list of csv string
        representation
        """
        result = []
        if csv_string is None or csv_string == "":
            return result
        for line in csv_string.splitlines():
            values = list(map(int, line.split(',')))
            if len(values) == 4:
                keys = ['id', 'size', 'x', 'y']
                result.append(dict(zip(keys, values)))
            if len(values) == 5:
                keys = ['id', 'width', 'height', 'x', 'y']
                result.append(dict(zip(keys, values)))
        return result

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize to csv and save"""
        with open(f"{cls.__name__}.csv", "w") as f:
            if list_objs is None:
                f.write(Base.to_csv_string(None))
            else:
                list_of_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_csv_string(list_of_dict))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        import os
        if os.path.exists(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r") as f:
                list_of_obj_rep = Base.from_json_string(f.read())
                list_of_obj = []
                for obj in list_of_obj_rep:
                    list_of_obj.append(cls.create(**obj))
                return list_of_obj
        else:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """load from a csv file and deserialize"""
        import os
        if os.path.exists(f"{cls.__name__}.csv"):
            with open(f"{cls.__name__}.csv", "r") as f:
                list_of_obj_rep = Base.from_csv_string(f.read())
                list_of_obj = []
                for obj in list_of_obj_rep:
                    list_of_obj.append(cls.create(**obj))
                return list_of_obj
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attribute set"""
        if cls.__name__ == "Square":
            args = [1]
        elif cls.__name__ == "Rectangle":
            args = [1, 1]
        else:
            raise TypeError("Unsupported Type")
        obj = cls(*args)
        obj.update(**dictionary)
        return obj
