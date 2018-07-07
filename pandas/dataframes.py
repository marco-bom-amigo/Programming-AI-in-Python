from pandas import Series, DataFrame
import numpy as np

serie_1 = Series(         [  1,   2,   3,   4,   5]
                , index = ["a", "b", "c", "d", "e"]
                )

print(serie_1)

serie_2 = serie_1.reindex( ["a", "b", "c", "d", "e", "f", "g", "h"])
print(serie_2)

serie_2 = serie_1.reindex( ["a", "b", "c", "d", "e", "f", "g", "h"]
                         , fill_value = 0
                         )
print(serie_2)

serie_3 = Series(         ["Santa Catarina", "Santo André", "Santo Antônio"]
                , index = [               0,             5,               8]
                )
print(serie_3)

index_range = range(15)

serie_4 = serie_3.reindex(index_range, method = "ffill")
print(serie_4)

serie_4 = serie_3.reindex(index_range, method = "bfill")
print(serie_4)

serie_4 = serie_3.reindex(index_range, method = "nearest")
print(serie_4)

data_frame = DataFrame( np.random.randn(25).reshape((5,5))
                      , index   = ["a", "b", "d", "e", "f"]
                      , columns = ["col_1", "col_2", "col_3", "col_4", "col_5"]
                      )
print(data_frame)

data_frame_2 = data_frame.reindex( columns    = ["col_1", "col_2", "col_3", "col_4", "col_5", "col_6"]
                                 , fill_value = 5
                                 )
print(data_frame_2)
print()
