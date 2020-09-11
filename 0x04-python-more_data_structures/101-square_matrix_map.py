#!/usr/bin/python3
def square_matrix_map(matrix=[]):
		return list(map(lambda colum: list(map(lambda fil: fil ** 2, colum)), matrix))
