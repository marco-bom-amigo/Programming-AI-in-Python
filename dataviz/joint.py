import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data_set_3 = np.random.randn(4000)
data_set_4 = np.random.randn(4000)
sns.jointplot(data_set_3, data_set_4)
plt.show()

sns.jointplot(data_set_3, data_set_4, kind="hex")
plt.show()

sns.jointplot(data_set_3, data_set_4, kind="kde")
plt.show()
