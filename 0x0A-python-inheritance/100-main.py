#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
my_4 = MyInt(4)
my_1 = MyInt(1)
print("3 == 3")
print(my_i == 3)
print("3 != 3")
print(my_i != 3)
print("3 == 3")
print(my_i == my_i)
print("3 != 3")
print(my_i != my_i)
print("4 == 3")
print(my_4 == 3)
print("4 != 3")
print(my_4 != 3)
print("4 == 3")
print(my_4 == my_i)
print("4 != 3")
print(my_4 != my_i)
print("1 == 3")
print(my_1 == 3)
print("1 != 3")
print(my_1 != 3)
print("1 == 3")
print(my_1 == my_i)
print("1 != 3")
print(my_1 != my_i)
print("1 != 1.34")
print(my_1 != 1.34)