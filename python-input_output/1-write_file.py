#!/usr/bin/python3
"""
string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
