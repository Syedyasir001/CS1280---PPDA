import numpy as np

array = np.random.randint(1, 21, size=(3, 3))
print("Random Array:")
print(array)

mean_value = np.mean(array)
print("\nMean:", mean_value)

array[array < 10] = 0
print("\nafter replacing elements less than 10 with 0:")
print(array)
