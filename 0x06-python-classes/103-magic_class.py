#!/usr/bin/python3
import math


class MagicClass:
    """class named MagicClass"""
    def __init__(self, radius):
        """Initialazation of the class with the radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calcu;ates the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference"""
        return 2 * math.pi * self.__radius
