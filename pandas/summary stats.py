from pandas import DataFrame
import pandas as pd
import numpy as np

linhas = np.array([[1, 2, 3, np.nan],[5, np.nan, 7, 8], [9, 10, 11, 12]])
data_frame_1 = DataFrame(linhas, index = ['a', 'b', 'c'], columns = ["col1", "col2", "col3", "col4"])
print(data_frame_1)
print(data_frame_1.idxmax())
print(data_frame_1.idxmin())

print("\nPor linha\n", data_frame_1.sum(axis = 1))
print("\nPor coluna\n", data_frame_1.sum())
