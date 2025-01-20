#!/usr/bin/python3
def no_c(my_string):
    new_stri = ""
    for char in my_string:
        if char == "c" or char == "C":
            char = ""
        new_stri = new_stri + char
    return new_stri
