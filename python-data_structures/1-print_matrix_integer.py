#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for mat in matrix:
        for m in mat:
            print("{:d}".format(m), end=" " if m != mat[-1] else '\n')
