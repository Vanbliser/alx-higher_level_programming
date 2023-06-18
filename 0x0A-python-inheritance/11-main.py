#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

s = Square(-1)

print(s)
print(s.area())
