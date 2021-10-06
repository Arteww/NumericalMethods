from interpolation import lagrange
import numpy as np
import matplotlib.pyplot as plt

with open("lagrange_input.txt") as f:
    data = f.read()

data = data.split('\n')

inputX = [int(row.split()[0]) for row in data]
inputY = [int(row.split()[1]) for row in data]

step = 0.25

# ============== Lagrange ===============

outputX, outputY = [], []

x = inputX[0]
while x <= inputX[-1]:
    outputX.append(x)
    outputY.append(lagrange(inputX, inputY, x))
    x += step

with open("lagrange_output.txt", "w") as f:
    f.writelines('\n'.join(f"({outputX[i]}; {outputY[i]})"
                           for i in range(len(outputX))))

plt.plot(inputX, inputY, 'gray', linestyle='--')
plt.plot(outputX, outputY, 'k', inputX, inputY, 'ko', linewidth=3)
plt.grid(True)
plt.show()

# ============== Newton ===============

outputX, outputY = [], []

x = inputX[0]
while x <= inputX[-1]:
    outputX.append(x)
    outputY.append(lagrange(inputX, inputY, x))
    x += step

with open("lagrange_output.txt", "w") as f:
    f.writelines('\n'.join(f"({outputX[i]}; {outputY[i]})"
                           for i in range(len(outputX))))

plt.plot(inputX, inputY, 'gray', linestyle='--')
plt.plot(outputX, outputY, 'k', inputX, inputY, 'ko', linewidth=3)
plt.grid(True)
plt.show()
