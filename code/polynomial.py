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


def graph_polynomial(data_list, polynomial):
    # create graph from polynomial
    x_min = min(point[0] for point in data_list)
    x_max = max(point[0] for point in data_list)
    y_min = min(point[1] for point in data_list)
    y_max = max(point[1] for point in data_list)
    x = np.linspace(1 * x_min, 1 * x_max, 500)
    poly_x = [sum(polynomial[j] * (i ** j) for j in range(len(polynomial))) for i in x]

    poly_as_str = '+'.join(['%s$x^%i$' % (str(round(polynomial[i], 2)), i) for i in range(len(polynomial))])

    # save polynomial stats
    with open('visualizations/latest_polynomial_description.txt', 'w') as file:
        file.write('Polynomial Coefficients: ' + str([round(polynomial[i], 2) for i in range(len(polynomial))]) + '\n')
        file.write('Polynomial Degree: ' + str(len(polynomial) - 1) + '\n')
        file.write('Fitted Points: ' + str(data_list)[1:-1])

    # plot
    plt.plot(x, poly_x, label='Polynomial: ' + poly_as_str if len(polynomial) < 5  else 'Polynomial: too long to display')
    plt.ylim(y_min - 1, y_max + 1)
    plt.title('Degree %i Polynomial, fitting %i data points' % (len(polynomial) - 1, len(data_list)))
    plt.legend()
    for point in data_list:
        plt.plot(point[0], point[1], marker='o')

    plt.savefig('visualizations/latest_polynomial_graph.png', dpi=72)
    plt.show()


def predict(n, polynomial):
    return sum(polynomial[i] * (n ** i) for i in range(len(polynomial)))


data_one = [[1, 1], [1.4, 1.45], [1.6, 1.6], [2, 1.8], [3, 3.6], [4, 4], [5, 5],
            [6, 6], [7, 7], [8, 8.12], [8.5, 10], [9, 15]]
data_two = [[5, 2], [2, 6], [3, 3], [5.6, 10], [10, 15], [-5, 2], [np.pi, np.pi], [-2, 9], [-4, 6], [-4.4, 7],
            [0, 9]]
data_three = [[2, 4], [2.5, 6], [5, 10], [10, 16]]
data_problem_33 = [[1, 12], [2, 15], [3, 16]]
data_wind_tunnel = [[0, 0], [2, 2.90], [4, 14.8], [6, 39.6], [8, 74.3], [10, 119]]


cur_data = data_one
polynomial_coefficients_one = fit_polynomial(cur_data)
graph_polynomial(cur_data, polynomial_coefficients_one)

print(predict(7.5, polynomial_coefficients_one))
