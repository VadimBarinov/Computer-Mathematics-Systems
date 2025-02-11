import numpy as np

A = np.array(
    [[3, 1],
     [2, 1]]
)
B = np.array(
    [[2, 1],
     [-1, 0],
     [1, 0]]
)
C = np.array(
    [[2, 1, 0],
     [-2, -1, 0],
     [3, 2, -1]]
)
E = np.array(
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
)

def calc_d():
    d = np.dot(np.dot(np.linalg.inv(A), np.transpose(B)), np.add(C, E))
    return d

def main():
    print('\nОтвет: D =')
    print(calc_d())

if __name__ == "__main__":
    main()