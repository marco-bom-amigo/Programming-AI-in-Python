import numpy as np

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [10, 11, 12, 13, 14]

lista_3 = [lista_1, lista_2]

np_array_2 = np.array(lista_3)

print(np_array_2)
print(np_array_2.shape)
print(np_array_2.dtype)

matriz_zeros_2 = np.zeros([4, 2])
matriz_uns_1 = np.ones([2, 3])
matriz_id = np.eye(5)

print(matriz_zeros_2)
print(matriz_uns_1)
print(matriz_id)