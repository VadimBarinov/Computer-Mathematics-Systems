import numpy as np
import sympy as sp


def row_reduced_matrix(A, B):
    matrix = np.hstack((A, B), dtype=float)
    # nrow - номер строки
    # row - строка
    for nrow, row in enumerate(matrix):
        # получаем диагональный элемент
        divider = row[nrow]
        if abs(divider) < 1e-10:  # почти 0 на диагонали
            break
        # делим строку на диагональный элемент, чтобы получить 1 на диагонали
        row /= divider
        # делаем 0 под диагональным элементом
        for lower_row in matrix[nrow+1:]:
            lower_row -= row * lower_row[nrow]

    print('\nРасширенная матрица при проходе вниз:')
    with np.printoptions(precision=2):
        print(matrix)

    # проход в обратную сторону
    for nrow in range(len(matrix)-1, 0, -1):
        row = matrix[nrow]
        divider = row[nrow]
        if abs(divider) < 1e-10:  # почти 0 на диагонали
            continue
        for upper_row in matrix[:nrow]:
            upper_row -= upper_row[nrow] * row

    print('\nРасширенная матрица при проходе вверх:')
    with np.printoptions(precision=2):
        print(matrix)

    return matrix


def fundamental_solution(solutions, free_vectors, rank_AB):
    result = []
    len_row = len(solutions[0])
    count_free_var = len_row - rank_AB - 1
    for free_var in free_vectors:
        current_result = []

        for nrow, row in enumerate(solutions):
            # получаем диагональный элемент
            divider = row[nrow]
            if divider == 1:
                temp_res = row[-1] - sum([
                    row[len_row-1-count_free_var+i]*free_var[i]
                    for i in range(count_free_var)
                ])
                current_result.append([temp_res])

        current_result = np.vstack((
            np.array(current_result),
            np.array([[i] for i in free_var])
        ))

        result.append(current_result)

    result = np.array(result)

    return result


def check_solution(A, X):
    check = np.dot(A, X)
    print("A * X =")
    for i in check:
        print(i)


# Матрица коэффициентов системы уравнений
A = np.asarray([
    [1, 2, 3, -2, -1],
    [1, -1, -2, -3, 2],
    [3, 2, 1, 2, -3],
    [5, 3, 2, -3, -2],
])
# Вектор значений
B = np.asarray([[0], [0], [0], [0]])


# Определение переменных
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')
# Матрица коэффициентов системы уравнений SymPy
AB_SP = [
    sp.Eq(1*x1 + 2*x2 + 3*x3 - 2*x4 - 1*x5, 0),
    sp.Eq(1*x1 - 1*x2 - 2*x3 - 3*x4 + 2*x5, 0),
    sp.Eq(3*x1 + 2*x2 + 1*x3 + 2*x4 - 3*x5, 0),
    sp.Eq(5*x1 + 3*x2 + 2*x3 - 3*x4 - 2*x5, 0),
]


try:

    # Вывод матриц A и B
    print("\nОсновная матрица A:")
    print(A)
    print("\nВектор-столбец B:")
    print(B)

    rank_A = np.linalg.matrix_rank(A)
    rank_AB = np.linalg.matrix_rank(np.hstack((A, B), dtype=float))

    # Вывод рангов матриц
    print("\nРанг матрицы A")
    print(rank_A)
    print("\nРанг матрицы AB")
    print(rank_AB)

    # Решение системы с помощью .solve() (символьное) + вывод результатов
    print("\nРешение системы с помощью .solve() (символьное):")
    print("\nОбщее решение:")
    sym_solutions = sp.solve(AB_SP, (x1, x2, x3, x4, x5))
    for key, value in sym_solutions.items():
        print(f"{key} = {value}")

    # Численное решение методом Гаусса + вывод результатов
    print("\nЧастное решение (методом Гаусса):")
    solutions = row_reduced_matrix(A, B)

    print("\nНаходим ФСР:")
    free_vectors = np.array([
        [1, 0],
        [0, 1]
    ])
    fundamental_solution_value = fundamental_solution(
        solutions,
        free_vectors,
        rank_AB
    )

    print()
    for n, c in enumerate(free_vectors):
        print(f"c{n+1} = {c}")
    for n, solution in enumerate(fundamental_solution_value):
        print(f"\nE{n+1} = ")
        print(solution)

    for n, solution in enumerate(fundamental_solution_value):
        print(f"\nПроверка решения {n+1}:")
        check_solution(A, np.array([i for i in solution]))

    print()


except ValueError as e:
    print(e)
