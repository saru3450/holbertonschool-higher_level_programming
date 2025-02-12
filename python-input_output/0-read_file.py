#!/usr/bin/python3
"""
that reads a text file (UTF8)
"""


def read_file(filename=""):
    """
     function that reads a text file
    """
    with open(filename, encoding="utf-8") as f:
        f.read = file.read()
        print(f.read(), end="")
        file.close()
