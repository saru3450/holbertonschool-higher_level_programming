#!/usr/bin/python
def divisible_by_2(my_list=[]):
    divi = []
    for i in my_list:
        if i % 2 == 0:
            divi.append(True)
        else:
            divi.append(False)
    return (divi)
