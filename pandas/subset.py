import pandas as pd

df_pimas = pd.read_csv("pima-data.csv")

print(df_pimas.head(5))
print(df_pimas.isnull().any())
print(df_pimas[df_pimas.isnull().any(axis = 1)])

print(df_pimas[df_pimas["glucose_conc"].isnull()])
print(df_pimas[df_pimas["thickness"].isnull()])
print(df_pimas[df_pimas["glucose_conc"] == 0].head(5))
print(df_pimas[df_pimas["thickness"] == 0].head(5))

print("Glucose conc - mean: ", df_pimas["glucose_conc"].mean())
print("Glucose conc - max: ", df_pimas["glucose_conc"].max())
print("Glucose conc - min: ", df_pimas["glucose_conc"].min())

print("Thickness - mean: ", df_pimas["thickness"].mean())
print("Thickness - max: ", df_pimas["thickness"].max())
print("Thickness - min: ", df_pimas["thickness"].min())