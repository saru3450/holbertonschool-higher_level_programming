#!/usr/bin/python3
"""
 writes an Object to a text file
 """
import json


def load_from_json_file(filename):
    """
    load_from_json
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
