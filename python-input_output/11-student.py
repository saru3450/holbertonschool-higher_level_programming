#!/usr/bin/python3
"""
Write the class Student with intance:
- first_name
- last_name
- age
"""


class Student:
    """
    the class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {x: y for x, y in self.__dict__.items() if x in attrs}

    def reload_from_json(self, json):
        for keys, values in json.items():
            setattr(self, keys, values)
