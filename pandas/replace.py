from pandas import DataFrame, Series
import numpy as np

serie_1 = Series([1,2,3,4,5,6])
print(serie_1)
print(serie_1.replace([2,3],[200,300]))
print(serie_1.replace(1,np.nan))
print(serie_1.replace({4: np.nan}))

