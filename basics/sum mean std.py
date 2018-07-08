import numpy as np

array = np.array([[1,2,3]
                 ,[4,5,6]
                 ,[7,8,9]
                 ])
print(array)
print(array.sum())
print("Vertical  ", array.sum(0))
print("Horizontal", array.sum(1))
print("Média     ", array.mean())
print("Desv. Pad.", array.std())

array_boolean = np.array([True, True, False, True, True])
print(array_boolean.any())
print(array_boolean.all())