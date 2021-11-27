from integration import *


def f1(x): return 6 * pow(x, 2) + (2 * x)


def f2(x): return 4 * x + 5


a, b = 0, 5

trapIntegralResult1 = trap_integral(f1, a, b)
print(f"Trapezoid Integral 6t^2 + 2t = {round(trapIntegralResult1)}")
trapIntegralResult2 = trap_integral(f2, a, b)
print(f"Trapezoid Integral 4t + 5 = {round(trapIntegralResult2)}")

simpsonIntegralResult1 = simpson_integral(f1, a, b)
print(f"\nSimpson Integral 6t^2 + 2t = {round(simpsonIntegralResult1)}")
simpsonIntegralResult2 = simpson_integral(f2, a, b)
print(f"Simpson 4t + 5 = {round(simpsonIntegralResult2)}")

s = abs(trapIntegralResult1 - trapIntegralResult2)
print(f"\nS = {round(s)}")
