from interpolation import lagrange

with open("input.txt") as f:
    data = f.read()

data = data.split('\n')

inputX = [int(row.split()[0]) for row in data]
inputY = [int(row.split()[1]) for row in data]

step = 0.25  # Шаг
# 0, 0.25, 0.5, 0.75, 1, ..., 5

outputX, outputY = [], []

x = inputX[0]
while x <= inputX[-1]:
    outputX.append(x)
    outputY.append(lagrange(inputX, inputY, x))
    x += step

with open("output.txt", "w") as f:
    f.writelines('\n'.join(f"({outputX[i]}; {outputY[i]})"
                           for i in range(len(outputX))))
