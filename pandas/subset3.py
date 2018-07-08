import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_pimas = pd.read_csv("pima-data-norm.csv", index_col = 0)
print(df_pimas.head(5))
print(df_pimas.describe())

corr = df_pimas.corr()
print(corr)

print(corr[corr > 0.8])

df_pimas.drop(["thickness"], axis = 1, inplace = True)
print(df_pimas.head(5))

df_pimas.to_csv("pima-data-norm-2.csv")

sns.heatmap(df_pimas.corr())
plt.show()
