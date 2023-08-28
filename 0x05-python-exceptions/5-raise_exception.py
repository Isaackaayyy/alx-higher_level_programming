#!/usr/bin/python3


def raise_exception():
    try:
        raise TypeError("This is an exception")
    except TypeError as ex:
        raise ex
