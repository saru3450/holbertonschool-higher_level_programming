#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lengt = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > lengt:
        return (my_list)
    my_list[idx] = element
    return my_list
