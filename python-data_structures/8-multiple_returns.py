#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    if not sentence:
        return(length, None)
    else:
        return(length, first)
