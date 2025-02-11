#!/usr/bin/python3
"""
Python objects using the pickle
"""
import pickle


class CustomObject:
    """
    Class CustomObject
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):

        """
        the object and save it to the provided filename
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb")as file:
                return pickle.load(file)
        except Exception as e:
            return None
