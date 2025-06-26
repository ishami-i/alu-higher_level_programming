#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_keys = sorted(list(a_dictionary))
    for i in dic_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
