#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == 0:
        print("\n")
    else:
        for mat in matrix:
            for m in mat:
                print("{:d}".format(m), end=" " if m != mat[-1] else '\n')
