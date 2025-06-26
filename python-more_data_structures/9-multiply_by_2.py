#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict()
    for i, values in a_dictionary.items():
        new_dictionary[i] = values * 2
    return new_dictionary
