#!/usr/bin/python3
"""
This module defines a function that prints a square using '#' characters.
"""


def print_square(size):
    """Prints a square with the character '#'

    Args:
        size (int): The size of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
