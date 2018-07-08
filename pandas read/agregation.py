from pandas import DataFrame
import numpy as np

def max_to_min(arr):
    return arr.max() - arr.min()

data_frame_1 = DataFrame({ "Coluna 1": ["A", "A", "B", "B", "C"]
                         , "Coluna 2": [1, 2, 1, 2, 1]
                         , "Coluna 3": np.random.randn(5), "Coluna 4": np.random.randn(5)})

group_2 = data_frame_1.groupby(["Coluna 1"])

print(group_2.agg(max_to_min))

print(group_2.agg("mean"))