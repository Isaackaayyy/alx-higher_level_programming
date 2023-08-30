#!/usr/bin/python3
"""Here is the header"""


class Square:
    """Defining the class"""
    def __init__(self, size=0):
        """Initialize the instance"""
        self.size = size


    def size(self):
	"""find the square's dimensions"""
        return self.__size

    def size(self, value):
        """Decide on the square's size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes the square's area"""
        return self.__size ** 2
