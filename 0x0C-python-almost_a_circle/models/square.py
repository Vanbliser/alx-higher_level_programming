#!/usr/bin/python3

"""contains the class Square that inhrits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """property size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """update this class' attributes"""
        if "size" in kwargs.keys():
            kwargs["width"] = kwargs["size"]
            kwargs["height"] = kwargs["size"]
            del kwargs["size"]
        if len(args) >= 2:
            args = list(args)
            args.insert(2, args[1])
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of square"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
