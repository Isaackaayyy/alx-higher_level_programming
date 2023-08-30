#!/usr/bin/python3
"""Here is the header"""


class Square:
    """class defined as square"""

    def __init__(self, size=0):
        """Initialization of as instance"""
        self.size = size

    def size(self):
        """Get the dimensions of the square"""
        return self.__size

    def size(self, value):
        """Set the dimensions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
