#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[ele**2 for ele in sub] for sub in matrix]
    return new_matrix
