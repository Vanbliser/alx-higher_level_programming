#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CCXLVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMCDXXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CLX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MLXVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCMXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MDCCLXXVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCMXVIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCMXLIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "mmmcmxxix"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MmMcmxXix"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
