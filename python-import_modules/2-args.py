#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv)

    if arg == 1:
        print("0 arguments.")
    elif arg == 2:
        print("1 argument:")
    elif arg > 2:
        print(f"{arg - 1} arguments:")

for i in range(1, arg):
    print("{}: {}".format(i, argv[i]))
