from pandas import Series
import pandas as pd
import numpy as np

data_frame_1 = pd.DataFrame( np.arange(8).reshape(2,4)
                           , index = pd.Index(["SP", "RJ"]
                           , name  = "Cidade")
                           , columns = pd.Index( ["Casa", "Prédio", "Mercado", "Oficina"]
                                               , name = "Estabelecimentos"
                                               )
                           )
print(data_frame_1)

data_frame_1_stack = data_frame_1.stack()
print(data_frame_1_stack)
print(data_frame_1_stack.unstack())
print(data_frame_1_stack.unstack("Cidade"))

serie_1 = Series([1, 2, 3], index=["A", "B", "C"])
serie_2 = Series([4, 5, 6], index=["D", "E", "F"])
serie_3 = pd.concat([serie_1, serie_2], keys=["Grupo 1", "Grupo 2"])
print(serie_3)

data_frame_2 = serie_3.unstack()
print(data_frame_2)

print(data_frame_2.stack())
print(data_frame_2.stack(dropna = False))
