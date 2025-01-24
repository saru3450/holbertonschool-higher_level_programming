#!/usr/bin/python3
"""
prints  with these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    if not text:
        return

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
    print("")
