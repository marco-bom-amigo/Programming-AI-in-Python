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

serie_2[serie_2 > 3] = 40
print(serie_2)

data_frame_1 = DataFrame( np.arange(16).reshape((4, 4))
                        , index = ["Brasil", "Peru", "Argentina", "Chile"]
                        , columns = ["2018", "2017", "2016", "2015"]
                        )
print(data_frame_1)
print(data_frame_1[["2018", "2016"]])
print(data_frame_1["2018"])
print(data_frame_1[data_frame_1["2018"] > 8])

print(data_frame_1 > 8)
print(data_frame_1.loc["Chile"])
print(data_frame_1.isnull())

serie_1 = Series([0, 1, 2], index=['a', 'b', 'c'])
serie_2 = Series([3, 4, 5], index=['a', 'c', 'f'])
print(serie_1)
print(serie_1 + serie_2)

data_frame_1 = DataFrame(np.arange(4).reshape((2, 2)), columns = list("AB") , index = ["SPO", "RJO"]       )
data_frame_2 = DataFrame(np.arange(9).reshape((3, 3)), columns = list("ADC"), index = ["RGN", "RJO", "SPO"])
print(data_frame_2)
print(data_frame_1)
print(data_frame_1 + data_frame_2)
print(data_frame_2.add(data_frame_1, fill_value = 0))
