#!/usr/bin/python3
"""
 writes an Object to a text file
 """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
