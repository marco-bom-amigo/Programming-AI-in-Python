import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
df_pimas = pd.read_csv("../pandas read/pima-data-norm-city.csv", index_col=0)
print(df_pimas.head(5))


