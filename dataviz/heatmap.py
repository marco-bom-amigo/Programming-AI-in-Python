import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

voos = sns.load_dataset("flights")
print(voos.head(5))

voos_pivoted = voos.pivot("month", "year", "passengers")
print(voos_pivoted.head(5))

fig, ax = plt.subplots()
fig.set_size_inches(18, 8)
sns.heatmap(voos_pivoted)
plt.show()

plt.subplots(figsize=(18, 8))
sns.heatmap(voos_pivoted, annot=True, fmt="d")
plt.show()

plt.subplots(figsize=(18, 8))
sns.heatmap(voos_pivoted, annot=True, fmt="d", center=voos_pivoted.loc["January", 1955])
plt.show()

sns.clustermap(voos_pivoted, figsize=(20,15))
plt.show()
