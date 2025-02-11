#!/usr/bin/python3
"""
functionality to serialize a Python dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    function serialize_and_save_from_to_file
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    function load_and_deserialize
    """
    with open(filename, 'r') as file:
        return json.load(file)
