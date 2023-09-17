#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        if ord(i) >= 97 and ord(i) <= 122:
            convert_str = ord(i) - 32
            i = chr(convert_str)
        print("{0}".format(i), end="")
    print()
