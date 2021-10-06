from diff_equations import euler


# y' = y + x
def f(x, y): return y + x


a, b, h = 0, 1, 0.2

yEuler = euler(f, a, b, h)

# Вывод результата (набор точек).
x_ = a
for i in range(len(yEuler)):
    print(f"({x_}; {yEuler[i]})")
    x_ += h
