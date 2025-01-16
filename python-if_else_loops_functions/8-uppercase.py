#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for x in str:
        if 97 <= ord(x) <= 122:
            upper = upper + chr(ord(x) - 32)
        else:
            upper = upper + x
    print("{:s}".format(upper))
