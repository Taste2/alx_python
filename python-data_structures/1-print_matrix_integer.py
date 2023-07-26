#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        if mat == None:
            print("\n")
        for m in mat:
            print("{:d}".format(m), end=" " if m != mat[-1] else '\n')
