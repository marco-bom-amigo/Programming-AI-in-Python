import numpy as np

array = np.random.randn(8)
print(array)

array.sort()
print(array)

nomes = np.array(["José", "Alice", "Beatriz", "Zacarias", "Yves", "Xavantes", "Yves"])
print(np.unique(nomes))
print(np.in1d(["Alice", "José"], nomes))