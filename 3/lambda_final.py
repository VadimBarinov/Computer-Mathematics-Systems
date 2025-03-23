import sympy as sp


# Определение переменных
x1, x2, x3, lam = sp.symbols('x1 x2 x3 lam')


def check_solution(A, X):
    check = A * X
    print("A * X =")
    for i in check:
        print(i)


# Системы уравнений
def equations(value):
    return [
        sp.Eq((value + 3)*x1 + 2*x2 + 5*x3, 0),
        sp.Eq(2*x1 - 7*x2 + 4*x3, 2),
        sp.Eq(6*x1 + 12*value*x2 + 13*x3, 4),
    ]


# Матрица коэффициентов системы уравнений
def get_a(value):
    return sp.Matrix([
        [(value + 3), 2, 5],
        [2, -7, 4],
        [6, 12*value, 13],
    ])


# Матрица коэффициентов системы уравнений
A = sp.Matrix([
    [(lam + 3), 2, 5],
    [2, -7, 4],
    [6, 12*lam, 13],
])
# Вектор значений
B = sp.Matrix([0, 2, 4])

try:
    linsolve_a = [lamb for lamb in sp.solve(A.det(), lam)]

    # Решение системы с помощью метода наименьших квадратов
    print("\nРешение методом наименьших квадратов:")

    for lambda_i in range(len(linsolve_a)):
        eq = get_a(linsolve_a[lambda_i].evalf())
        solution = eq.solve_least_squares(B)

        print(f"\n{lambda_i+1}-ое решение:")
        for i in range(solution.shape[0]):
            print(f"x{i+1} = {solution[i]}")

        print("Проверка:")
        check_solution(
            eq,
            sp.Matrix([i for i in solution])
            )

    # Решение системы с помощью .solve() (символьное)
    print("\nРешение методом .solve (символьное):")
    for lambda_i in range(len(linsolve_a)):
        eq = equations(linsolve_a[lambda_i])
        solution = sp.solve(eq, (x1, x2, x3))

        print(f"\n{lambda_i+1}-ое решение:")
        if len(solution) > 0:
            for key, value in solution.items():
                print(f"{key} = {value}")
            if len(solution) < len(eq):
                print("Система имеет бесконечно много решений!")
        else:
            print("Система несовместна!")

except ValueError as e:
    print(e)
