from pandas import Series
import pandas as pd
import numpy as np

series_1 = Series([1, 2, 3], index=['A', 'B', 'C'])
series_2 = Series([4, 5, 6], index=['C', 'D', 'E'])
print(series_2, series_1)

print(pd.concat([series_1, series_2]))
print(pd.concat([series_1, series_2], keys = ["chave_1", "chave_2"]))

print(pd.concat([series_1, series_2], axis = 1))
print(pd.concat([series_1, series_2], axis = 1, keys = ["chave_1", "chave_2"]))

data_frame_1 = pd.DataFrame(np.random.randn(4, 3), columns = ['A', 'B', 'C'])
data_frame_2 = pd.DataFrame(np.random.randn(3, 3), columns = ['D', 'E', 'F'])
print(data_frame_1, data_frame_2)

print(pd.concat([data_frame_1, data_frame_2]))
print(pd.concat([data_frame_1, data_frame_2], ignore_index = True))