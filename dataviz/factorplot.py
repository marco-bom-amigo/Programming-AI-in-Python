import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white")
planetas = sns.load_dataset("planets")
print(planetas.head(5))
g = sns.factorplot(x="year", data=planetas, kind="count",palette="BuPu", size=6, aspect=1.5)
g.set_xticklabels(step=2)
plt.show()

