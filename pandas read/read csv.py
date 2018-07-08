import pandas as pd

data_frame_csv = pd.read_csv("exemplo.csv")
print(data_frame_csv)

data_frame_csv = pd.read_csv("exemplo.csv", sep = ";")
print(data_frame_csv)

data_frame_csv = pd.read_csv("exemplo.csv", sep = ";", header = None)
print(data_frame_csv)

data_frame_csv = pd.read_csv("exemplo.csv", sep = ";", header = None, nrows = 3)
print(data_frame_csv)

data_frame_csv = pd.read_csv("exemplo.csv", sep = ";", names = ["Ano", "Livros","Jogos", "Cadernos"], skiprows = 2)
print(data_frame_csv)
print(data_frame_csv.describe())