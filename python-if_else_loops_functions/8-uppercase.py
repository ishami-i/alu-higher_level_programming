#!/usr/bin/python3
def islower(c):
    """Check if a character is a lowercase letter."""
    if not isinstance(c, str) or len(c) != 1:
        return False
    char = ord(c)
    if char >= 97 and char <= 122:
        return True
    else:
        return False
