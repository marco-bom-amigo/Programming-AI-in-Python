import pandas as pd
import numpy as np

data_frame_excel = pd.read_excel("exemplo.xlsx")
print(data_frame_excel)

data_frame_excel = pd.read_excel("exemplo.xlsx", shee_tname = "Fonte_1")
print(data_frame_excel)

data_frame_1 = pd.DataFrame({"chave": ['A', 'B', 'B', 'C'], "data_frame_1": np.arange(4)})
data_frame_2 = pd.DataFrame({"chave": ['C', 'D', 'E']     , "data_frame_2": [4, 5, 6]})
print(data_frame_1)
print(data_frame_2)

print(pd.merge(data_frame_1, data_frame_2))
print(pd.merge(data_frame_1, data_frame_2, on = "chave", how = "left"))
print(pd.merge(data_frame_1, data_frame_2, on = "chave", how = "right"))
print(pd.merge(data_frame_1, data_frame_2, on = "chave", how = "outer"))

data_frame_1 = pd.read_excel("exemplo_merge.xlsx", sheet_name = "Fonte_1")
data_frame_2 = pd.read_excel("exemplo_merge.xlsx", sheet_name = "Fonte_2")
print(data_frame_1)
print(data_frame_2)

print(pd.merge(data_frame_1, data_frame_2, on = ["Filme", "Estado"], how = "outer"))
print(pd.merge(data_frame_1, data_frame_2, on = ["Filme", "Estado"], how = "outer", suffixes=("_Fonte_1", "_Fonte_2")))