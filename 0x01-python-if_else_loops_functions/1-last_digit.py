#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
div = -10
if (number > 0):
    div = 10
if ((number % div) > 5):
    print(f"Last digit of {number} is {number % div} and is greater than 5")
if ((number % div) == 0):
    print(f"Last digit of {number} is {number % div} and is 0")
if ((number % div) < 6 and (number % div) != 0):
    print(f"Last digit of {number} is {number % div} and is less ", end="")
    print(f"than 6 and not 0")
