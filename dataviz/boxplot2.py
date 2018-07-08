import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
df_pimas = pd.read_csv("../pandas read/pima-data-norm-city.csv", index_col=0)
print(df_pimas.head(5))

sns.boxplot(df_pimas["num_preg"])
plt.show()

sns.violinplot(df_pimas["num_preg"], inner="quartile")
plt.show()

sns.boxplot(df_pimas["glucose_conc"])
plt.show()

sns.violinplot(df_pimas["glucose_conc"], inner="quartile")
plt.show()

sns.boxplot(df_pimas["diastolic_bp"])
plt.show()

sns.violinplot(df_pimas["diastolic_bp"], inner="quartile")
plt.show()

sns.boxplot(df_pimas["bmi"])
plt.show()

sns.violinplot(df_pimas["bmi"], inner="quartile")
plt.show()

sns.boxplot(df_pimas["diab_pred"])
plt.show()

sns.violinplot(df_pimas["diab_pred"], inner="quartile")
plt.show()

sns.boxplot(df_pimas["age"])
plt.show()

sns.violinplot(df_pimas["age"], inner="quartile")
plt.show()

sns.boxplot(df_pimas["skin"])
plt.show()

sns.violinplot(df_pimas["skin"], inner="quartile")
plt.show()
