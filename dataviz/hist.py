import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
data_set_1 = np.random.randn(200)
plt.hist(data_set_1)
plt.show()

data_set_2 = np.random.randn(100)
plt.hist(data_set_2, color="orange")
plt.show()

plt.hist(data_set_1, color="blue", alpha=0.5, bins=20, density=True)
plt.hist(data_set_2, color="orange", alpha=0.5, bins=20, density=True)
plt.show()
