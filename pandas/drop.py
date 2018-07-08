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
print(data_frame.dropna())
print(data_frame.dropna(how = "all"))
print(data_frame.dropna(thresh = 1))

data_frame_1 = DataFrame({"Coluna 1":["A"]*3 + ["B"]*2, "Coluna 2":[1,2,2,3,3]})
print(data_frame_1)
print(data_frame_1.duplicated())
print(data_frame_1.drop_duplicates())
print(data_frame_1.drop_duplicates(["Coluna 1"]))
print(data_frame_1.drop_duplicates(["Coluna 2"]))
print(data_frame_1.drop_duplicates(keep="last"))
