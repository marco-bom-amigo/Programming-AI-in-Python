from pandas import Series
import pandas as pd
import numpy as np

data_frame_1 = pd.read_excel("exemplo_pivoting.xlsx")
print(data_frame_1)

print(data_frame_1.pivot("Data", "Candidato", "Votos"))

print(pd.pivot_table(data_frame_1, values="Votos", index=["Candidato"], aggfunc=np.sum))