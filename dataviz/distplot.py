import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df_pimas = pd.read_csv("../pandas read/pima-data-norm-city.csv", index_col=0)
print(df_pimas.head(5))

plt.hist(df_pimas["num_preg"])
plt.show()

sns.distplot(df_pimas["num_preg"])
plt.show()

sns.distplot(df_pimas["age"])
plt.show()

sns.distplot(df_pimas["diab_pred"])
plt.show()

sns.countplot(df_pimas["diabetes"])
plt.show()

sns.countplot(data=df_pimas, x="city", hue="diabetes")
plt.show()

sns.distplot(df_pimas["skin"])
plt.show()

sns.distplot(df_pimas["bmi"])
plt.show()
