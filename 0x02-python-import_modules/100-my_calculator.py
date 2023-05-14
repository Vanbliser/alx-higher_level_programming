#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
import argparse

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="")
        sys.exit("")
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    symbol = ord(sys.argv[2])
    if symbol == 43:
        print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
    elif symbol == 45:
        print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
    elif symbol == 42:
        print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
    elif symbol == 47:
        print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /", end="")
        sys.exit("")
