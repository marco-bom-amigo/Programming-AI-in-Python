from pandas import Series
import numpy as np

series_1 = Series(range(4), index=["a", "d", "b", "c"])
print(series_1)
print(series_1.sort_index())
print(series_1.sort_values())

series_2 = Series(np.random.randn(10))
print(series_2.sort_values())
print(series_2.rank())

