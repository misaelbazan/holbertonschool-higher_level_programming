#!/usr/bin/python3
import copy
def square_matrix_simple(matrix=[]):
    new_matrix = copy.deepcopy(matrix)
    for sub in new_matrix:
        for ele in range(len(sub)):
            sub[ele] = sub[ele]**2
    return new_matrix
