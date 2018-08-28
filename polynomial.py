import numpy as np
import matplotlib.pyplot as plt


def polynomial_values(n, degree=1):

    return [n ** i for i in range(degree + 1)]


def data_points_to_matrices(data_list):
    degree = len(data_list) - 1
    A = []
    b = []
    for data_point in data_list:
        A.append(polynomial_values(data_point[0], degree))
        b.append(data_point[1])

    return [A, b]


def fit_polynomial(data_list):
    # assert len(data_list) == degree + 1, 'This is not a well-determined system, add or remove data points'
    matrices = data_points_to_matrices(data_list)
    A = matrices[0]
    b = matrices[1]
    return np.linalg.solve(A, b)


data_one = [[1, 1], [2, 1.8], [3, 3.6],[4,4],[5,5],[6,6],[7,7],[8,8.12]]

polynomial_coefficients_one = fit_polynomial(data_one)


def graph_polynomial(data_list, polynomial):
    x_min = min(point[0] for point in data_list)
    x_max = max(point[0] for point in data_list)
    x = np.linspace(1 * x_min, 1 * x_max, 30)
    poly_x = [sum(polynomial[j] * (i ** j) for j in range(len(polynomial))) for i in x]
    poly_as_str = '+'.join(['%s$x^%i$' % (str(round(polynomial[i], 2)), i) for i in range(len(polynomial))])
    print(poly_as_str)
    with open('latest_polynomial_description.txt', 'w') as file:
        file.write('Polynomial Coefficients: ' + str([round(polynomial[i], 2) for i in range(len(polynomial))]) + '\n')
        file.write('Polynomial Degree: ' + str(len(polynomial) - 1) + '\n')
        file.write('Fitted Points: ' + str(data_list)[1:-1])
    plt.plot(x, poly_x, label='Polynomial: ' + poly_as_str if len(polynomial) < 4 else 'Polynomial: too long to display')
    plt.title('Degree %i Polynomial, fitting %i data points' % (len(polynomial) - 1, len(data_list)))
    plt.legend()
    for point in data_list:
        plt.plot(point[0], point[1], marker='o')

    plt.savefig('latest_polynomial_graph.png', dpi=72)
    plt.show()


graph_polynomial(data_one, polynomial_coefficients_one)
