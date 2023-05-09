## Project title: 0x01-python-if_else_loops_functions

This project contains the following mandatory tasks:
* 0-positive_or_negative.py: program will assign a random signed number to the variable number each time it is executed.
* 1-last_digit.py: This program will assign a random signed number to the variable number each time it is executed.
* 2-print_alphabet.py: a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
* 3-print_alphabt.py: a program that prints the ASCII alphabet, in lowercase, not followed by a new line, except q and e.
* 4-print_hexa.py: a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example).
* 5-print_comb2.py: a program that prints numbers from 0 to 99.
* 6-print_comb3.py: a program that prints all possible different combinations of two digits.
* 7-islower.py: a function that checks for lowercase character.
* 8-uppercase.py: a function that prints a string in uppercase followed by a new line.
* 9-print_last_digit.py: a function that prints the last digit of a number.
* 10-add.py: a function that adds two integers and returns the result.
* 11-pow.py: a function that computes a to the power of b and return the value.
* 12-fizzbuzz.py: a function that prints the numbers from 1 to 100 separated by a space.
* 13-insert_number.c, lists.h: a function in C that inserts a number into a sorted singly linked list.

The following are advance tasks:
* 100-print_tebahpla.py: a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
* 101-remove_char_at.py: a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
* 102-magic_calculation.py: Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

<pre>
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
</pre>
