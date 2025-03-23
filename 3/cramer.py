import numpy as np


# Функция применения метода Крамера для решения системы линейных уравнений
def cramer_rule(A, B):
    # Вычисление определителя главной матрицы
    det_A = np.linalg.det(A)
    # Проверка на случай, если определитель главной матрицы равен нулю
    if det_A == 0:
        raise ValueError("Определитель матрицы коэффициентов равен нулю.")
    solutions = []
    # Проходим по каждому столбцу матрицы
    # и вычисляем определитель со заменой столбца на вектор значений
    for i in range(A.shape[0]):
        Ai = A.copy()
        Ai[:, i] = B
        solutions.append(np.linalg.det(Ai) / det_A)

    return solutions


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
    [1, 9, -4],
    [2, 5, -3],
    [5, 6, -2],
])
# Вектор значений
B = np.asarray([9, 4, 18])

try:
    # Вызов функции для решения системы уравнений методом Крамера
    solutions = cramer_rule(A, B)
    # Вывод результатов
    print("\nРешение методом Крамера:")
    print_solution(solutions)
    print("\nПроверка решения:")
    check_solution(A, solutions)
except ValueError as e:
    print(e)
