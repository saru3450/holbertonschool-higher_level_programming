#!/usr/bin/python3
"""
function that appends a string at the end
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
