import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6])
print("1D Array:")
print(array_1d)

array_2d = array_1d.reshape(2, 3)
print("\nReshaped to 2d Array (2x3):")
print(array_2d)

print("\nElement at possition(1,2):", array_2d[1, 2])

array_2d[0, 1] = 10
print("\nModified Array(After changing the position of element(0,1) to 10):")
print(array_2d)

array_sum = np.sum(array_2d)
print("\nSum of all elements in the array:", array_sum)
