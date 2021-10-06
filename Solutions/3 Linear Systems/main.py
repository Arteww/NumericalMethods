from linear_systems import *

matrix1 = [[7,   2,  3,  15],
           [5,  -3,  2,  15],
           [10, -11, 5,  36]]

matrix2 = [[10,  1,  1,  12],
           [2,   10, 1,  13],
           [2,   2,  10, 14]]

gaussSolution = gauss(matrix1)
iterativeSolution = iterative(matrix2)
seidelSolution = seidel(matrix2)

print("Gaussian elimination:")
for i in range(len(gaussSolution)):
    print(f"x[{i + 1}] = {round(gaussSolution[i])}")

print("\nIterative method:")
for i in range(len(iterativeSolution)):
    print(f"x[{i + 1}] = {round(iterativeSolution[i], 4)}")

print("\nSeidel method:")
for i in range(len(iterativeSolution)):
    print(f"x[{i + 1}] = {round(seidelSolution[i], 4)}")
