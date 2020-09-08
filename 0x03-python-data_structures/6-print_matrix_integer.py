#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in matrix:
        for fil in col:
            print("{:d}".format(fil), end="")
            if fil != col[-1]:  # controlo espa al final
                print(" ", end="")
        print("")  # salto de linea entre filas
