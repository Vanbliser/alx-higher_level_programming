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
