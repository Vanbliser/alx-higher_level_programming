## 0x0B. Python - Input/Output

### Requirements
#### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc

#### Python Test Cases
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

#### Mandatory tasks
* 0-read_file.py: Write a function that reads a text file (UTF8) and prints it to stdout:
<pre>
Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
</pre>

* 1-write_file.py: Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
<pre>
Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module
</pre>

* 2-append_write.py: Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
<pre>
Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
</pre>

* 3-to_json_string.py: Write a function that returns the JSON representation of an object (string):
<pre>
Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.
</pre>

* 4-from_json_string.py: Write a function that returns an object (Python data structure) represented by a JSON string:
<pre>
Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
</pre>

* 5-save_to_json_file.py: Write a function that writes an Object to a text file, using a JSON representation:
<pre>
Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.
</pre>

* 6-load_from_json_file.py: Write a function that creates an Object from a “JSON file”:
<pre>
Prototype: def load_from_json_file(filename):
You must use the with statement
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
You don’t need to manage file permissions / exceptions.
</pre>

* 7-add_item.py: Write a script that adds all arguments to a Python list, and then save them to a file:
<pre>
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.
</pre>

* 8-class_to_json.py: Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
<pre>
Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
You are not allowed to import any module
</pre>

* 9-student.py: Write a class Student that defines a student by:
<pre>
Public instance attributes: first_name, last_name, age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module
</pre>

* 10-student.py: Write a class Student that defines a student by: (based on 9-student.py)
<pre>
Public instance attributes: first_name, last_name, age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py): If attrs is a list of strings, only attribute names contained in this list must be retrieved. Otherwise, all attributes must be retrieved
You are not allowed to import any module
</pre>

* 11-student.py: Write a class Student that defines a student by: (based on 10-student.py)
<pre>
Public instance attributes: first_name, last_name, age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py): If attrs is a list of strings, only attributes name contain in this list must be retrieved. Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module
</pre>

* 12-pascal_triangle.py: Technical interview preparation: You are not allowed to google anything. Whiteboard first.
<pre>
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
</pre>

#### Advance tasks
* 100-append_after.py: Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
<pre>
Prototype: def append_after(filename="", search_string="", new_string=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
</pre>

* 101-stats.py: Write a script that reads stdin line by line and computes metrics:
<pre>
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
</pre>
