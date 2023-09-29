#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    addition_0 = tuple_a[0] + tuple_b[0]
    addition_1 = tuple_a[1] + tuple_b[1]
    addition = int(addition_0), int(addition_1)
    return(addition)
