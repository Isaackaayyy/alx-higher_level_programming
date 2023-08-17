#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    del_keys = []

    for key, value in a_dictionary.items():
        del_keys.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
