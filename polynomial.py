import numpy as np


def polynomial(n, degree=1):

    return [n ** i for i in range(degree + 1)]


def data_points_to_matrices(data_list):
    A = []
    b = []
    for data_point in data_list:
        A.append(polynomial(data_point[0], 2))
        b.append(data_point[1])

    return [A, b]


data = [[5, 2], [2, 6], [3, 3]]
matrices = data_points_to_matrices(data)
A = matrices[0]
b = matrices[1]

print(A, '\n', b)

S = np.linalg.solve(A, b)

print(S)
