import numpy as np


def row_reduced_matrix(A, B):
    matrix = np.hstack((A, B), dtype=float)
    # nrow - номер строки
    # row - строка
    for nrow, row in enumerate(matrix):
        # получаем диагональный элемент
        divider = row[nrow]
        # делим строку на диагональный элемент, чтобы получить 1 на диагонали
        row /= divider
        # делаем 0 под диагональным элементом
        for lower_row in matrix[nrow+1:]:
            lower_row -= row * lower_row[nrow]

    print('\nРасширенная матрица при проходе вниз:')
    print(matrix)

    # проход в обратную сторону
    for nrow in range(len(matrix)-1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            upper_row -= upper_row[nrow] * row

    print('\nРасширенная матрица при проходе вверх:')
    print(matrix)

    return matrix


def check_solution(A, X):
    check = A.dot(X)
    print("A * X =")
    for i in check:
        print(i)


def print_solution(solutions):
    for i, sol in enumerate(solutions, start=1):
        print(f"x{i}: {sol}")


# Матрица коэффициентов системы уравнений
A = np.asarray([
    [1, 2, 3, -2],
    [1, -1, -2, -3],
    [3, 2, -1, 2],
    [2, -3, 2, 1],
])
# Вектор значений
B = np.asarray([[6], [8], [4], [-8]])


try:
    # Выполнение приведения матрицы к диагональному виду
    solutions = row_reduced_matrix(A, B)[:, -1]

    # Вывод результатов
    print("\nРешение методом Гаусса:")
    print_solution(solutions)
    print("\nПроверка решения:")
    check_solution(A, solutions)

except ValueError as e:
    print(e)
