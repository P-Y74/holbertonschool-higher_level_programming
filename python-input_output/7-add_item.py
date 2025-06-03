#!/usr/bin/python3
"""
Module add_item

Script to add all command-line arguments to a Python list stored in a JSON file.

The list is stored in "add_item.json" as a JSON array.
If the file doesn't exist, it is created automatically.
Existing items are loaded from the file and new arguments are appended.

Usage:
    ./7-add_item.py item1 item2 item3 ...

Example:
    ./7-add_item.py Best School
    # The items "Best" and "School" will be added to the JSON file.

Dependencies:
    - save_to_json_file from 5-save_to_json_file.py
    - load_from_json_file from 6-load_from_json_file.py
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
