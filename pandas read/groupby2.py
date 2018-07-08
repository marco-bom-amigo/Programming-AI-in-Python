import pandas as pd

df_pimas = pd.read_csv("pima-data-norm-city.csv", index_col=0)
print(df_pimas.head(5))

df_filtered = df_pimas[(df_pimas["diabetes"]==True) & (df_pimas["age"] >= 20) & (df_pimas["age"] <=50)]
print(df_filtered.head(5))

group_age = df_filtered["diabetes"].groupby(df_filtered["age"])
print(group_age.count())

df_filtered = df_pimas[(df_pimas["diabetes"]==True) & (df_pimas["age"] <=30)]
print(df_filtered.head(5))

group_age_preg = df_filtered["num_preg"].groupby(df_filtered["age"])
print(group_age_preg.sum())

df_filtered = df_pimas[(df_pimas["diabetes"]==True)]
print(df_filtered.head(5))

group_diab_state = df_filtered["diabetes"].groupby(df_filtered["state"])
print(group_diab_state.count())

print(df_pimas[(df_pimas["diabetes"]==True) & (df_pimas["state"] == "Bihar")])

group_diab_city_bp = df_pimas["diastolic_bp"].groupby(df_pimas["city"])
print(group_diab_city_bp.mean())