#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
MyClass2 = __import__('8-my_class_3').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

m = MyClass2("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
