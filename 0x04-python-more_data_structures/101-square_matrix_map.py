#!/usr/bin/python3
def square_matrix_map(matrix=[]):
		return list(map(lambda col: list(map(lambda fil: fil ** 2, col)), matrix))
