#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if type(x) != int:
        raise ValueError("is not an integer")
    while count < x:
        try:
            print(my_list[count], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
