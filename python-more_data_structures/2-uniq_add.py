#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp = set(my_list)
    result = 0
    for i in tmp:
        result += i
    return result
