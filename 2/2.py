import numpy as np


# исходная матрица
A = np.array([
    [1, 1, 1, 1],
    [1, 4, 2, 3],
    [1, 10, 3, 6],
    [6, 10, 1, 4],
])


def calc_inverse_matrix(m):
    n = m.shape[0]
    # получаем расширенную матрицу
    matrix = np.hstack((m, np.eye(n)))
    print('\nРасширенная матрица:')
    print(matrix)

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
    with np.printoptions(precision=2):
        print(matrix)

    # проход в обратную сторону
    for nrow in range(len(matrix)-1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            upper_row -= upper_row[nrow] * row

    print('\nРасширенная матрица при проходе вверх:')
    with np.printoptions(precision=2):
        print(matrix)

    print('\nРезультат: ')
    return matrix[:, n:].copy()


def splitting_into_blocks_solve(matrix):
    a1 = np.array([
        [matrix[0, 0], matrix[0, 1]],
        [matrix[1, 0], matrix[1, 1]]
    ])
    a2 = np.array([
        [matrix[0, 2], matrix[0, 3]],
        [matrix[1, 2], matrix[1, 3]]
    ])
    a3 = np.array([
        [matrix[2, 0], matrix[2, 1]],
        [matrix[3, 0], matrix[3, 1]]
    ])
    a4 = np.array([
        [matrix[2, 2], matrix[2, 3]],
        [matrix[3, 2], matrix[3, 3]]
    ])
    # вывод полученных блоков
    print('\nA1:')
    print(a1)
    print('\nA2:')
    print(a2)
    print('\nA3:')
    print(a3)
    print('\nA4:')
    print(a4)
    n = np.linalg.inv(np.add(a4, -(np.dot(np.dot(a3, np.linalg.inv(a1)), a2))))
    l = np.dot((np.dot(np.linalg.inv(a1), -(a2))), n)
    m = np.dot(np.dot(n, -(a3)), np.linalg.inv(a1))
    k = np.dot(np.linalg.inv(a1), np.add(np.eye(2), -(np.dot(a2, m))))
    # вывод полученных обращенных блоков
    print('\nN:')
    print(n)
    print('\nL:')
    print(l)
    print('\nM:')
    print(m)
    print('\nK:')
    print(k)

    print('\nРезультат:')
    return np.vstack((np.hstack((k, l)), np.hstack((m, n))))


def main():
    print('\nИсходная матрица:')
    print(A)
    print(f'\nОпределитель матрицы = {round(np.linalg.det(A))}')
    print('\nОбратная матрица, используя функцию numpy.linalg.inv():')
    print(np.linalg.inv(A))
    print('\nОбратная матрица при помощи элементарных преобразований:')
    print(calc_inverse_matrix(A))
    print('\nОбратная матрица при помощи разбиения на блоки:')
    print(splitting_into_blocks_solve(A))


if __name__ == '__main__':
    main()
