from linear_systems import gauss

matrix = [[7, 2, 3, 15],
          [5, -3, 2, 15],
          [10, -11, 5, 36]]

gaussSolution = gauss(matrix)

# Вывод решения
for i in range(len(gaussSolution)):
    print(f"x[{i + 1}] = {gaussSolution[i]}")

