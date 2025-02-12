#!/usr/bin/python3
"""
The function reads a texte file
"""


def read_file(filename=""):
    """
    the function read_file
    """
    with open(filename, encoding="utf-8") as file:
        readfile = file.read()
        print(readfile, end="")
        file.close()
