import pandas as pd

df_pimas = pd.read_csv("pima-data-norm-city.csv", index_col=0)
print(df_pimas.head(5))

class_map = {True: 1, False: 0}
city_map = {"Agra": 1, "Bangalore": 2, "Hyderabad": 3, "Lucknow": 4, "Mumbai": 5, "Patna": 6}
state_map = {"Bihar": 1, "Kamataka": 2, "Maharashtra": 3, "Telangana": 4, "Uttar Pradesh": 5}

df_pimas["diabetes"] = df_pimas["diabetes"].map(class_map)
df_pimas["city"] = df_pimas["city"].map(city_map)
df_pimas["state"] = df_pimas["state"].map(state_map)

print(df_pimas)

df_pimas.to_csv("pima-data-norm-city-map.csv")