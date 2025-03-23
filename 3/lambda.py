import sympy as sp


def check_solution(A, X):
    check = A * X
    print("A * X =")
    for i in check:
        print(i)


def print_solution(solutions):
    for i, sol in enumerate(solutions, start=1):
        print(f"x{i}: {sol}")


# Определение переменных
x1, x2, x3, lam = sp.symbols('x1 x2 x3 lam')
# Определение системы уравнений
equations = [
    sp.Eq((lam + 3)*x1 + 2*x2 + 5*x3, 0),
    sp.Eq(2*x1 - 7*x2 + 4*x3, 2),
    sp.Eq(6*x1 + 12*lam*x2 + 13*x3, 4),
]
# Матрица коэффициентов системы уравнений
A = sp.Matrix([
    [(lam + 3), 2, 5],
    [2, -7, 4],
    [6, 12*lam, 13],
])
# Вектор значений
B = sp.Matrix([0, 2, 4])

try:
    linsolve_a = [lamb.evalf() for lamb in sp.solve(A.det(), lam)]
    general_solution = sp.solve(equations, (x1, x2, x3))
    all_solutions = []
    for i in linsolve_a:
        temp = {}
        temp["lambda_value"] = i
        for key, value in general_solution.items():
            temp[key] = value.subs(lam, i)
        all_solutions.append(temp)

    # Вывод результатов
    print("\nРешение численным методом:")
    for i in range(len(all_solutions)):
        print(f"\n{i+1}-ое решение:")
        current_solution = all_solutions[i]

        for key, value in current_solution.items():
            print(f"{key} = {value}")

        lambda_value = current_solution.get("lambda_value")
        del current_solution["lambda_value"]

        print(f"\nПроверка {i+1}-го решения:")
        check_solution(
            sp.Matrix(A.subs(lam, lambda_value)),
            sp.Matrix([i for _, i in current_solution.items()])
            )
except ValueError as e:
    print(e)
