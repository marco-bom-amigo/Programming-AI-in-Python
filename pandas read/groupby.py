from pandas import DataFrame
import numpy as np

data_frame_1 = DataFrame({ "Coluna 1": ["A", "A", "B", "B", "C"]
                         , "Coluna 2": [1, 2, 1, 2, 1]
                         , "Coluna 3": np.random.randn(5), "Coluna 4": np.random.randn(5)})
print(data_frame_1)

group_1 = data_frame_1["Coluna 3"].groupby(data_frame_1["Coluna 1"])
print("\nMean\n", group_1.mean())
print("\nMax\n", group_1.max())

print("\n",data_frame_1.groupby(["Coluna 1"]).mean())

group_dict = dict(list(data_frame_1.groupby("Coluna 1")))
print(group_dict)
print(group_dict["A"])

coluna_2_group = data_frame_1.groupby(["Coluna 1", "Coluna 2"])[["Coluna 4"]]
print(coluna_2_group.mean())
