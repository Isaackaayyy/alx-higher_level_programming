#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for a in range(list_length):
        try:
            result = my_list_1[a] / my_list_2[a]
        except (ZeroDivisionError, TypeError):
            result = 0
            if isinstance(my_list_1[a], (int, float)) and \
               isinstance(my_list_2[a], (int, float)):
                if my_list_2[i] == 0:
                    print("division by 0")
                else:
                    print("wrong type")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
