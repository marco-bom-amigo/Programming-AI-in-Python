import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data_frame_1 = pd.read_excel("../pandas read/exemplo.xlsx")
print(data_frame_1)

sns.lmplot(data=data_frame_1, y="Avaliação",x="Custo")
plt.show()