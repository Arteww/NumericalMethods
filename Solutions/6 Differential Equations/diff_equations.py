
def runge(f, a, b, h, y0):
    y = [y0]
    i = 0
    x = a + h
    while x <= b:
        i += 1
        k1 = h * f(x - h, y[i-1])
        k2 = h * f(x, y[i-1] + k1)
        y.append(y[i-1] + (k1 + k2) / 2)
        x += h
    return y
