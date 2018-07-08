import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib

df_beer = pd.read_excel("beer_consumption.xlsx")
print("Head\n",df_beer.head(10))
print("\nDesc\n",df_beer.describe())
print("\nCount\n", df_beer.count())
print("\nP. Cor\n", df_beer.corr())
sns.heatmap(df_beer.corr())
plt.show()

plt.show()
sns.lmplot( "beer_consumption"
          , "temp_avg"
          , df_beer
          , scatter_kws = {   "marker":"x", "color":   "blue"}
          , line_kws    = {"linewidth":  1, "color": "orange"}
          )
plt.show()

sns.lmplot( "beer_consumption"
          , "temp_max"
          , df_beer
          , scatter_kws = {   "marker":"x", "color":   "blue"}
          , line_kws    = {"linewidth":  1, "color": "orange"}
          )
plt.show()

sns.lmplot( "precip"
          , "beer_consumption"
          , df_beer
          , scatter_kws ={   "marker":"x", "color":   "blue"}
          , line_kws    ={"linewidth":  1, "color": "orange"}
          )
plt.show()

class_weekend = {True: 1, False: 0}
df_beer["weekend"] = df_beer["weekend"].map(class_weekend)

print(df_beer.head(5))

print(df_beer.isnull().any())

print(df_beer[df_beer["temp_avg"].isnull()])

print(df_beer[df_beer["temp_min"].isnull()])

print(df_beer[df_beer["temp_max"].isnull()])

print(df_beer[df_beer["weekend"].isnull()])

df_beer_temp_avg_null = df_beer[df_beer["temp_avg"].isnull()].copy()
print(df_beer_temp_avg_null)

df_beer_temp_avg_null["temp_avg"] = (df_beer["temp_max"] + df_beer["temp_min"])/2
print(df_beer_temp_avg_null)

df_beer["temp_avg"] = df_beer["temp_avg"].replace(np.nan,(df_beer["temp_max"] + df_beer["temp_min"])/2)
print(df_beer.loc[[168,181,309,314]])

df_beer["temp_min"] = df_beer["temp_min"].replace(np.nan,df_beer["temp_min"].mean())
print(df_beer.loc[[7,116]])

df_beer["temp_max"] = df_beer["temp_max"].replace(np.nan,df_beer["temp_max"].mean())
print(df_beer.loc[[98, 165, 237]])

df_beer["weekend"] = df_beer["weekend"].replace(np.nan,df_beer["weekend"].mode()[0])
print(df_beer.loc[[21,27]])

print(df_beer["weekend"].mode()[0])
print(df_beer.isnull().any())
print((df_beer == 0).any())
print(df_beer[df_beer["temp_avg"] == 0])
print(df_beer[df_beer["temp_min"] == 0])
print(df_beer[df_beer["temp_max"] == 0])
print(df_beer[df_beer["precip"] == 0].head(10))
print(df_beer[df_beer["weekend"] == 0].head(10))

df_beer["temp_avg"] = df_beer["temp_avg"].replace(0,(df_beer["temp_max"] + df_beer["temp_min"])/2)
df_beer["temp_min"] = df_beer["temp_min"].replace(0,df_beer["temp_min"].mean())
df_beer["temp_max"] = df_beer["temp_max"].replace(0,df_beer["temp_max"].mean())

print((df_beer == 0).any())

feature_col_names     = ['temp_max', 'precip', 'weekend']
predicted_class_names = ['beer_consumption']

X = df_beer[    feature_col_names].values
y = df_beer[predicted_class_names].values

split_test_size = 0.30

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = split_test_size, random_state = 42)
print("{0:0.2f}% in training set".format((len(X_train)/len(df_beer.index)) * 100))
print("{0:0.2f}% in test set".format((len(X_test)/len(df_beer.index)) * 100))

lr_model = linear_model.LinearRegression()
lr_model.fit(X_train, y_train.ravel())

y_pred = lr_model.predict(X_test)

print('R² score: %.2f' % r2_score(y_test, y_pred))
print('R² score: %.2f' % lr_model.score(X_test, y_test))

predict_value = [[35, 0, 1]]
print(lr_model.predict(predict_value))

predict_value = [[35, 0, 0]]
print(lr_model.predict(predict_value))

predict_value = [[35, 20, 0]]
print(lr_model.predict(predict_value))

predict_value = [[10, 20, 0]]
print(lr_model.predict(predict_value))


joblib.dump(lr_model, 'lr_model.pkl')
lr_model_loaded = joblib.load('lr_model.pkl')

predict_value = [[10, 20, 0]]
print(lr_model_loaded.predict(predict_value))