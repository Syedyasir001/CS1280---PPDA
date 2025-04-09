import numpy as np
matrix1 = np.random.randint(1, 11, size=(3, 3))
matrix2 = np.random.randint(1, 11, size=(3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

subtraction_result = matrix1 - matrix2
print("\nMatrix Subtraction:")
print(subtraction_result)

division_result = matrix1 / matrix2
print("\nElement-wise Division:")
print(division_result)
