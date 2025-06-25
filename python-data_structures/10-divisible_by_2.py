#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    count = len(my_list)
    replica = my_list[:]
    for i in range(0, count):
        if my_list[i] % 2 == 0:
            replica[i] = True
        elif my_list[i] % 2 != 0:
            replica[i] = False
    return replica
