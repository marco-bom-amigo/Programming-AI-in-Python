from pandas import DataFrame
import numpy as np

data_frame = DataFrame([ [     1,      2,      3,      4]
                       , [     5, np.nan,      7, np.nan]
                       , [np.nan, np.nan, np.nan,     10]
                       , [np.nan, np.nan, np.nan, np.nan]
                       ]
                      ,columns = ['A', 'B', 'C', 'D']
                      )
print(data_frame)

print(data_frame.fillna(data_frame.mean()))
print(data_frame.fillna(data_frame.max()))
print(data_frame.fillna(data_frame.min()))

print(data_frame.fillna({'A': 1, 'B': 2, 'C': 3, 'D': 4}))
print(data_frame['A'].fillna(data_frame['A'].mean(), inplace = True))