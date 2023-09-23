#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row[:-1]:
            print("{:d} ".format(val), end="")
        for val in row[-1:]:
            print("{:d}".format(val), end="")
        print()
