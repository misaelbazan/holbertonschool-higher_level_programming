#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    tuple_a = length, first
    if len(sentence) <= 0:
        tuple_a = length, None
    else:
        return(tuple_a)
