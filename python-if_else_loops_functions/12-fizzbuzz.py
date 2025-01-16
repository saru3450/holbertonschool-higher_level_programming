#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("FIZZ", end="")
        if i % 5 == 0:
            print("BUZZ", end="")
        if i % 3 != 0 and i % 5 != 0:
            print(i, end="")
            print(" ", end="")
