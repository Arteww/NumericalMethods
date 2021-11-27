from diff_equations import runge


def f(x, y): return 0.0980724253 * (20.0 - y)


a, b, h, y0 = 0, 30, 0.2, 100.0

yRunge = runge(f, a, b, h, y0)

# Вывод результата (набор точек).
x_ = a
for i in range(len(yRunge)):
    print(f"({round(x_,2)}; {round(yRunge[i], 4)})")
    x_ += h
