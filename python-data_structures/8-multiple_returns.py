#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    if len(sentence) <= 0:
        return(length, None)
    else:
        return(length, first)
