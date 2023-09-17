#!/usr/bin/env python3
def islower(c):
    ord_char = ord(c)
    if ord_char >= 97 and ord_char <= 122:
        return True
    else:
        return False
