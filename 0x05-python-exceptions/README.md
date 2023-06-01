### Project Title: 0x05. Python - Exceptions

This project contains the following mandatory tasks

* 0-safe_print_list.py: a function that prints x elements of a list.
<pre>
Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()
</pre>

* 1-safe_print_integer.py: a function that prints an integer with "{:d}".format().
<pre>
Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to import any module
You are not allowed to use type()
</pre>

* 2-safe_print_list_integers.py: a function that prints the first x elements of a list and only integers.
<pre>
Prototype: def safe_print_list_integers(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
x represents the number of elements to access in my_list
x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
Returns the real number of integers printed
You have to use try: / except:
You have to use "{:d}".format() to print an integer
You are not allowed to import any module
You are not allowed to use len()

* 3-safe_print_division.py: a function that divides 2 integers and prints the result.

* 4-list_division.py: a function that divides element by element 2 lists.

* 5-raise_exception.py: a function that raises a type exception.

* 6-raise_exception_msg.py: a function that raises a name exception with a message.
