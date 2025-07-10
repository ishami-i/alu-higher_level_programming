#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """ a class that defines the a rectangle
        properties: getter and setter methods for width and height
        methods: __init__ method -for creating a class
                area method - for calculating the area of the rectangle
                perimeter method -for calculating the perimeter of rectangle
                __str__ methods - that returns the string representation of
                Rectangle instance(s)
                _repr__ method - returns the formal strig representation of
                an object that can be evaluated
                _del_ method - performs clean up operation before an object
                is deleted
    """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += str(self.print_symbol) * self.width + "\n"
        return result.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @propert
