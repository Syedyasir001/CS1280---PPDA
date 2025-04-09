import numpy as np
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

matrix_sum =np.add(matrix_A, matrix_B)
print("Matrix Addtion (A+ B):")
print(matrix_sum)

matrix_product_elementwise = np.multiply(matrix_A, matrix_B)
print("\nElement-wise Matrix Multiplication (A * B):")
print(matrix_product_elementwise)

matrix_dot_product =np.dot(matrix_A, matrix_B)
print("\nMatrix Dot Product (A . B):")
print(matrix_dot_product)

matrix_transpose =np.transpose(matrix_A)
print("\Transpose of Matrix A:")
print(matrix_transpose)
