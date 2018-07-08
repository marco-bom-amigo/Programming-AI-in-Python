from pandas import DataFrame
import numpy as np
import pandas as pd

data_frame_1 = pd.read_excel("exemplo_crosstabulation.xlsx")
print(data_frame_1)

print(pd.crosstab(data_frame_1.Tipo, data_frame_1.Condição, margins=True))

print(pd.crosstab(data_frame_1.Tipo, data_frame_1.Condição, margins=False))

