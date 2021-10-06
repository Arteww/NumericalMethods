from equations import dichotomy


# x^2 - 34 = 0
def f(x): return x * x - 34


a, b = 0, 8

xDichotomy = dichotomy(f, a, b)
print(f"x = {xDichotomy}")
