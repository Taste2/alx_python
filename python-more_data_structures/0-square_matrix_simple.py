#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if not matrix or not matrix[0]:
        print()
        return
    exp_matrix = []
    for row in matrix:
        exp_number_row = []
        for number in row:
            square_ = number ** 2
            exp_number_row.append(square_)
        exp_matrix.append(exp_number_row)
    return exp_matrix
