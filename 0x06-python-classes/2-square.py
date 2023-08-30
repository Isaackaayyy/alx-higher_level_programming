#!/usr/bin/python3
"""Here, is the header"""


class Square:
    """Definition of class square"""
    def __init__(self, size=0):
	"""Initializes a square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
