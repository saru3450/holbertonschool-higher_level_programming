#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numb = []
    sum = 0
    for number in my_list:
        if number not in unique_numb:
            unique_numb.append(number)
            sum += number
    return sum
