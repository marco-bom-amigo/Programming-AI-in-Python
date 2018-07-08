import pandas as pd
import numpy as np

df_pimas = pd.read_csv("pima-data.csv")

print(df_pimas.head(5))
print(df_pimas.isnull().any())

df_pimas["diastolic_bp"] = df_pimas["diastolic_bp"].replace(np.nan, df_pimas["diastolic_bp"].mean())
df_pimas[   "thickness"] = df_pimas[   "thickness"].replace(np.nan, df_pimas[   "thickness"].mean())
df_pimas[     "insulin"] = df_pimas[     "insulin"].replace(np.nan, df_pimas[     "insulin"].mean())

print(df_pimas.isnull().any())
print(df_pimas.isin([0]).sum())

df_pimas["glucose_conc"] = df_pimas["glucose_conc"].replace(0, df_pimas["glucose_conc"].mean())
df_pimas[         "bmi"] = df_pimas[         "bmi"].replace(0, df_pimas[         "bmi"].mean())
df_pimas[        "skin"] = df_pimas[        "skin"].replace(0, df_pimas[        "skin"].mean())

print(df_pimas.isin([0]).sum())

df_pimas.index.rename("id", inplace = True)
print(df_pimas.head(5))

df_pimas.to_csv("pima-data-norm.csv")