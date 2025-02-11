from copy import deepcopy

import numpy as np

ALPHA_1 = 1
ALPHA_2 = 2
ALPHA_3 = 3
ALPHA_4 = 4

A = 2
B = 4
C = 3
D = 1

A = np.array(
    [[ALPHA_1, ALPHA_2, ALPHA_3, ALPHA_4],
     [2, A, B, C],
     [B, 2*C, A+B, -A],
     [-D, -A, C+B, 0]], dtype=float
)


def calc_det_first():
    result = deepcopy(A)
    print('Исходная матрица:')
    print(result)
    matrix_len = result.shape[0]
    coefficient = 1
    while matrix_len > 2:
        for i in range(1, matrix_len):
            result[i] = np.add(result[i], result[0] * (-(result[i, 0] / result[0, 0])))
        print('\nВыполняем операции над матрицей')
        if coefficient != 1:
            print(f'{coefficient} *')
        print(result)
        coefficient *= result[0, 0]
        result = result[1:, 1:]
        matrix_len = result.shape[0]
        print(f'\nПонижаем порядок: \n{coefficient} *')
        print(result)

    matrix_determinant = coefficient * (result[0, 0] * result[1, 1] - result[1, 0] * result[0, 1])
    print(f'\nDeterminant = {matrix_determinant}')
    return matrix_determinant


def calc_det_second():
    result = deepcopy(A)
    print('Исходная матрица:')
    print(result)
    matrix_len_i = result.shape[0]
    current_i = 1
    matrix_len_j = result.shape[1] - 1
    current_j = 0
    for j in range(current_j, matrix_len_j):
        for i in range(current_i, matrix_len_i):
            result[i] = np.add(
                result[i],
                result[current_i - 1] * (-(result[i, current_j] / result[current_i - 1, current_j]))
            )
        print('\nВыполняем операции над матрицей')
        print(result)
        current_i += 1
        current_j += 1

    matrix_determinant = 1
    for i in range(0, matrix_len_i):
        matrix_determinant *= result[i, i]
    print(f'\nDeterminant = {matrix_determinant}')
    return matrix_determinant


def main():
    print('\nПодсчет определителя встроенной функцией:')
    print(f'Determinant = {np.linalg.det(A)}')
    print('\nОтвет: 1) Метод понижения порядка')
    calc_det_first()
    print('\nОтвет: 2) Метод приведения определителя к треугольному виду')
    calc_det_second()


if __name__ == '__main__':
    main()