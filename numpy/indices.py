import numpy as np

array = np.arange(0, 11)

print(array)
print(array[2])
print(array[1:6])
print(array[:4])

array[1:6] = 99
slice_array = array[6:]
slice_array[:] = 100
print(slice_array)
print(array)

array_copy = array.copy()
array_copy[:] = 99
print(array_copy)
print(array)