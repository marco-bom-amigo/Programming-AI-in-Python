import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_set_1 = np.random.randn(200)
data_set_2 = np.random.randn(200)
sns.boxplot(data=[data_set_1, data_set_2])
plt.show()

sns.boxplot(data=[data_set_1, data_set_2],whis=np.inf)
plt.show()

data_frame_1 = pd.read_excel("../pandas read/exemplo.xlsx")
sns.boxplot(data=data_frame_1)
plt.show()

data_frame_1_norm = data_frame_1.copy()
data_frame_1_norm["Custo"] = data_frame_1["Custo"].div(data_frame_1_norm["Custo"].sum(), axis=0)
data_frame_1_norm["Avaliação"] = data_frame_1["Avaliação"].div(data_frame_1_norm["Avaliação"].sum(), axis=0)
print(data_frame_1_norm)

sns.boxplot(data=data_frame_1_norm)
plt.show()

fig, ax = plt.subplots()
fig.set_size_inches(18, 6)
sns.boxplot(ax=ax, data=data_frame_1_norm, y="Custo", x="Filme")
sns.despine()
plt.show()