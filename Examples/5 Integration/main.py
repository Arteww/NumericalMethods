from integration import left_rectangles


# ∫ 5x^2 + x
def f(x): return 5 * x * x + x


a, b = 0, 8

leftRectanglesResult = left_rectangles(f, a, b)
print(f"Integral 5x^2 + x = {leftRectanglesResult}")
