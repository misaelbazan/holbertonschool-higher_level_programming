#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    else:
        maximum = 0
        for number in my_list:
            if number > maximum:
                maximum = number
        return (maximum)
