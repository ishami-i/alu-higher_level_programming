#!/usr/bin/python3
<<<<<<< HEAD
=======
# Write a function that prints x elements of a list.
>>>>>>> cf6625bfdd5966bfcac0ddeab30cab1e667c1d22
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
