from interpolation import lagrange, newton_equal, newton_unequal, spline
import matplotlib.pyplot as plt


def read_file(filename):
    with open(filename) as f:
        data = (f.read()).split('\n')
    xs_ = [float(row.split()[0]) for row in data]
    ys_ = [float(row.split()[1]) for row in data]
    return xs_, ys_


def write_file(filename):
    with open(filename, "w") as f:
        f.writelines('\n'.join(f"({round(outputX[i], 2)}; {round(outputY[i], 2)})"
                               for i in range(len(outputX))))


def plot_show(name):
    _, ax = plt.subplots()
    plt.plot(inputX, inputY, 'gray', linestyle='--')
    ax.set_title(name)
    plt.grid()
    plt.plot(outputX, outputY, 'k', linewidth=3)
    plt.plot(inputX, inputY, 'ko')
    plt.show()


step = 0.01


# ================ Lagrange =================

inputX, inputY = read_file("input/lagrange.txt")
outputX, outputY = [], []

x = inputX[0]
while x <= inputX[-1]:
    outputX.append(x)
    outputY.append(lagrange(inputX, inputY, x))
    x += step

write_file("output/lagrange.txt")
plot_show('Lagrange polynomial')


# ========= Newton Equal Interval ==========

inputX, inputY = read_file("input/newton_equal.txt")
outputX, outputY = [], []

x = inputX[0]
while x <= inputX[-1]:
    outputX.append(x)
    outputY.append(newton_equal(inputX, inputY, x))
    x += step

write_file("output/newton_equal.txt")
plot_show('Newton polynomial (Equal Interval)')


# ======== Newton Unequal Interval =========

inputX, inputY = read_file("input/newton_unequal.txt")
outputX, outputY = [], []

x = inputX[0]
while x <= inputX[-1]:
    outputX.append(x)
    outputY.append(newton_unequal(inputX, inputY, x))
    x += step

write_file("output/newton_unequal.txt")
plot_show('Newton polynomial (Unequal Interval)')


# ================ Spline =================

inputX, inputY = read_file("input/spline.txt")
outputX, outputY = [], []

b = 1
for i in range(len(inputX)-1):
    x = inputX[i]
    ys, b = spline(inputX, inputY, i, b, step)
    for y in ys:
        x += step
        outputX.append(x)
        outputY.append(y)

write_file("output/spline.txt")
plot_show('Spline')
