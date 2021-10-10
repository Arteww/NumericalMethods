
def lagrange(xs, ys, arg):
    assert(len(xs) == len(ys))

    polynomial = 0
    for i in range(len(xs)):
        monomial = ys[i]
        for j in range(len(xs)):
            if i != j:
                monomial *= (arg - xs[j]) / (xs[i] - xs[j])
        polynomial += monomial
    return polynomial


def newton_equal(xs, ys, arg):
    assert(len(xs) == len(ys))

    h = xs[1] - xs[0]
    polynomial = ys[0]
    for i in range(1, len(xs)):
        polynomial += (finite_difference(ys, i, 0) *
                       generalized_power(xs, i, arg) /
                       (fact(i) * pow(h, i)))
    return polynomial


def newton_unequal(xs, ys, arg):
    assert(len(xs) == len(ys))

    polynomial = ys[0]
    for i in range(1, len(xs)):
        polynomial += (divided_difference(xs, ys, i, 0) *
                       generalized_power(xs, i, arg))
    return polynomial


def spline(xs, ys, i, b, step):
    assert(len(xs) == len(ys))

    output_x, output_y = [], []

    h = xs[i+1] - xs[i]
    new_z = 2*(ys[i+1] - ys[i]) / h
    new_b = new_z - b

    x = xs[i]
    while x <= xs[i + 1]:
        c = (new_b - b) / (2 * h)
        s = (ys[i] + b * (x - xs[i]) + c * pow(x - xs[i], 2))
        output_y.append(s)
        x += step

    return output_y, new_b


# secondary functions


def divided_difference(xs, ys, order, i):
    if order == 1:
        return (ys[i+1] - ys[i]) / (xs[i+1] - xs[i])
    return ((divided_difference(xs, ys, order - 1, i + 1) -
            divided_difference(xs, ys, order - 1, i)) /
            (xs[order + i] - xs[i]))


def finite_difference(ys, order, i):
    if order == 1:
        return ys[i+1] - ys[i]
    return (finite_difference(ys, order - 1, i + 1) -
            finite_difference(ys, order - 1, i))


def generalized_power(xs, i, x):
    result = 1
    for index in range(i):
        result *= (x - xs[index])
    return result


def fact(a):
    if a == 0:
        return 1
    return fact(a - 1) * a
