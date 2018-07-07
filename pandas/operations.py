from pandas import Series, DataFrame
import numpy as np

serie_1 = Series(np.arange(3), index = ['a', 'b', 'c'])
print(serie_1)
print(serie_1.drop('c'))

data_frame_1 = DataFrame(np.arange(9).reshape((3, 3)), index = ["Desktop", "Phone", "Tablet"], columns = ["Brasil", "Chile", "Peru"])
print(data_frame_1)
print("Remoção por índice, linha")
print(data_frame_1.drop("Phone"))

print("Remoção por coluna")
print(data_frame_1.drop("Chile", axis = 1))

serie_1 = Series(np.arange(4), index=['a', 'b', 'c', 'd'])
print(serie_1)

serie_2 = serie_1 * 2
print(serie_2)
print(serie_2['b'])
print(serie_2[serie_2 > 3])
print(serie_2[['a','c']])
print(serie_2[1:3])