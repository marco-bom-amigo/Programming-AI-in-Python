import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
df_pimas = pd.read_csv("../pandas read/pima-data-norm-city.csv", index_col=0)
print(df_pimas.head(5))

sns.lmplot("age", "num_preg", df_pimas)
plt.show()

sns.lmplot("age", "diab_pred", df_pimas)
plt.show()

sns.lmplot("age", "glucose_conc", df_pimas)
plt.show()

sns.lmplot("diab_pred", "glucose_conc", df_pimas, order=2)
plt.show()

sns.lmplot("insulin", "glucose_conc", df_pimas)
plt.show()

sns.lmplot("insulin", "diab_pred", df_pimas)
plt.show()

sns.lmplot("bmi", "diab_pred", df_pimas)
plt.show()