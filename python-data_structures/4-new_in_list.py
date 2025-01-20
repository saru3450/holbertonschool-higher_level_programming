#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lengt = len(my_list)
    new_in_list = list.copy(my_list)
    if idx < 0:
        return my_list
    elif idx > lengt:
        return my_list
    else:
        new_in_list[idx] = element
        return new_in_list
