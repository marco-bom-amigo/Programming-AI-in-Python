import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data_frame_1 = pd.read_excel("../pandas read/exemplo.xlsx")
print(data_frame_1)

sns.lmplot(data=data_frame_1, y="Avaliação",x="Custo")
plt.show()

data_frame_2 = pd.read_excel("bilheteria.xlsx")
print(data_frame_2)

fig, ax = plt.subplots()
fig.set_size_inches(18, 8)
plt.plot(data_frame_2["Data"], data_frame_2["Bilheteria"])
plt.show()
