import numpy as np
import matplotlib.pyplot as plt


def polynomial_values(n, degree=1):
    return [n ** i for i in range(degree)]


def exponential_values(n, num_data_points):
    return [np.e ** (i * n) for i in range(num_data_points)]


def data_points_to_matrices(data_list, term_values):
    # term_values returns a row of each coefficient

    len_data = len(data_list)
    A = []
    b = []
    for data_point in data_list:
        A.append(term_values(data_point[0], len_data))
        b.append(data_point[1])
    return [A, b]


def fit(data_list, polynomial_creator):
    # assert len(data_list) == degree + 1, 'This is not a well-determined system, add or remove data points'
    matrices = data_points_to_matrices(data_list, polynomial_creator)
    A = matrices[0]
    b = matrices[1]
    return np.linalg.solve(A, b)


def graph_polynomial(data_list, polynomial, sub=plt):
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
    sub.plot(x, poly_x, label='Polynomial: ' + poly_as_str if len(polynomial) < 5  else 'Polynomial: too long to display')
    plt.ylim(y_min - 1, y_max + 1)
    plt.title('Degree %i Polynomial, fitting %i data points' % (len(polynomial) - 1, len(data_list)))
    sub.legend()
    for point in data_list:
        sub.plot(point[0], point[1], marker='o')
    plt.savefig('visualizations/latest_polynomial_graph.png', dpi=72)


def graph_exponential(data_list, exponential, sub=plt):
    # This one ended up not being very fittable, I'll probably try sin/cos next
    x_min = min(point[0] for point in data_list)
    x_max = max(point[0] for point in data_list)
    y_min = min(point[1] for point in data_list)
    y_max = max(point[1] for point in data_list)
    x = np.linspace(x_min, x_max, 256)
    expon_x = [sum(exponential[j] * np.e ** (j * i) for j in range(len(exponential))) for i in x]
    sub.plot(x, expon_x)
    for point in data_list:
        sub.plot(point[0], point[1], marker='o')
    plt.ylim(y_min, y_max)


def predict_poly(n, polynomial):
    return sum(polynomial[i] * (n ** i) for i in range(len(polynomial)))


def predict_exp(n, exponential):
    return sum(exponential[i] * np.e ** (n * i) for i in range(len(exponential)))


data_one = [[1, 1], [1.4, 1.45], [1.6, 1.6], [2, 1.8], [3, 3.6], [4, 4], [5, 5],
            [6, 6], [7, 7], [8, 8.12], [8.5, 10], [9, 15]]
data_two = [[5, 2], [2, 6], [3, 3], [5.6, 10], [10, 15], [-5, 2], [np.pi, np.pi], [-2, 9], [-4, 6], [-4.4, 7],
            [0, 9]]
data_three = [[2, 4], [2.5, 6], [5, 10], [10, 16]]
data_problem_33 = [[1, 12], [2, 15], [3, 16]]
data_wind_tunnel = [[0, 0], [2, 2.90], [4, 14.8], [6, 39.6], [8, 74.3], [10, 119]]


cur_data = data_two
polynomial_coefficients_one = fit(cur_data, polynomial_values)
exponential_coefficients_one = fit(cur_data, exponential_values)
# f, (ax1, ax2) = plt.subplots(2, 1)
graph_polynomial(cur_data, polynomial_coefficients_one)
# graph_exponential(cur_data, exponential_coefficients_one)
plt.show()

print(predict_poly(7.5, polynomial_coefficients_one))
