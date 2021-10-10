from math import fabs
from inspect import stack


def gauss(matrix):
    n = len(matrix)
    solution = [None]*n

    for k in range(0, n):
        temp = matrix[k][k]
        for j in range(k, n + 1):
            matrix[k][j] /= temp
        for i in range(k + 1, n):
            temp = matrix[i][k]
            for j in range(k, n + 1):
                matrix[i][j] -= temp * matrix[k][j]

    solution[n - 1] = matrix[-1][n]
    for k in range(n - 2, -1, -1):
        sum_ = 0
        for j in range(k + 1, n):
            sum_ += matrix[k][j] * solution[j]
        solution[k] = matrix[k][n] - sum_

    return solution


def iterative(matrix, eps=.01):
    n = len(matrix)
    solution = []

    alpha = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            alpha[i][j] = -matrix[i][j] / matrix[i][i] if i != j else 0

    max_ = 0
    for i in range(n):
        sum_ = 0
        for j in range(n):
            sum_ += fabs(alpha[i][j])
        if sum_ > max_:
            max_ = sum_

    delta = (1 - max_) / max_ * eps
    beta = []

    for i in range(n):
        beta.append(matrix[i][n] / matrix[i][i])
    for i in range(n):
        solution.append(beta[i])

    while True:
        max_diff = 0
        old = []
        for i in range(n):
            old.append(solution[i])
        for i in range(n):
            solution[i] = beta[i]
            for j in range(n):
                if i != j:
                    if stack()[1][3] == "seidel":
                        solution[i] += alpha[i][j] * solution[j]
                    else:
                        solution[i] += alpha[i][j] * old[j]
        for i in range(n):
            diff = fabs(old[i] - solution[i])
            if diff > max_diff:
                max_diff = diff
        if max_diff <= delta:
            break

    return solution


def seidel(matrix):
    return iterative(matrix)
