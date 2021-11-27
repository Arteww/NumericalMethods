def trap_integral(f, a, b, step_count=100):
    step = (b - a) / (1.0 * step_count)
    sum = 0.0
    for i in range(1, step_count):
        sum += f(a + i * step)
    sum += (f(a) + f(b)) / 2
    sum *= step
    return sum


def simpson_integral(f, a, b, step_count=50):
    width = (b - a) / step_count
    sum = 0
    for step in range(step_count):
        x1 = a + step * width
        x2 = a + (step + 1) * width
        sum += (x2 - x1) / 6.0 * (f(x1) + 4.0 * f(0.5 * (x1 + x2)) + f(x2))
    return sum
