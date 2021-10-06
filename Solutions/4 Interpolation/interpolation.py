
def lagrange(x, y, arg):
    assert(len(x) == len(y))

    polynomial = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (arg - x[i])
                p2 = p2 * (x[j] - x[i])
        polynomial = polynomial + y[j] * p1 / p2
    return round(polynomial, 1)


def newton(x, y, arg):
    assert(len(x) == len(y))

    polynomial = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (arg - x[i])
                p2 = p2 * (x[j] - x[i])
        polynomial = polynomial + y[j] * p1 / p2
    return round(polynomial, 1)

