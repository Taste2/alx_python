#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = matrix[0]
    b = matrix[1]
    c = matrix[2]
    for i in a:
        print("{:d}".format(i), end=" " if i == a[0] or i == a[1] else '\n')
    for j in b:
        print("{:d}".format(j), end=" " if j == b[0] or j == b[1] else '\n')
    for k in c:
        print("{:d}".format(k), end=" ")
