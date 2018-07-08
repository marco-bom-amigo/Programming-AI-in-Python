import pandas as pd

df_pimas = pd.read_csv("pima-data-norm-2.csv", index_col=0)
print(df_pimas.head(5))

df_pimas_city = pd.read_csv("pima-data-city.csv", sep=";", index_col=0)
print(df_pimas_city.head(5))

df_pimas_data_city = pd.merge(df_pimas, df_pimas_city, left_index=True, right_index=True)
print(df_pimas_data_city.head(5))

df_pimas_data_city.to_csv("pima-data-norm-city.csv")