#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[0:]
    count = len(my_list)
    if idx < 0:
        return copy
    elif idx >= count:
        return copy
    else:
        copy[idx] = element
        return copy
