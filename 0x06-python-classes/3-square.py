#!/usr/bin/python3
"""Here, is the header"""


class Square:
    """Definition os class Square"""
    def __init__(self, size=0):
        """Initializing of an instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
