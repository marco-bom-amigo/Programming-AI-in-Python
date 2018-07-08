import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')

df_stock = pd.read_excel("data_akbilgic.xlsx")
print(df_stock.head(10))

df_stock_pivoted = df_stock.pivot("month_year","day","BOVESPA")
print(df_stock_pivoted.head(5))

fig, ax = plt.subplots()
fig.set_size_inches(18, 8)
sns.heatmap(df_stock_pivoted)
plt.show()