#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# create the file if it does not exit, else leave the file as is
with open('add_item.json', mode='a') as file:
    pass
# read the file
with open('add_item.json') as file:
    JSON = file.read()
# if file contains something, then load it, else create an empty list
if JSON:
    list_obj = load_from_json_file('add_item.json')
else:
    list_obj = []
# extend the program argument list to the loaded list
list_obj.extend(sys.argv[1:])
# convert the whole list to json and save it in the file
save_to_json_file(list_obj, 'add_item.json')
