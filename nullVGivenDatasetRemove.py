import pandas as pd
dataset= pd.read_csv("data1.csv")
dataset
dataset.isnull()
dataset.isnull().head(10)
dataset.isnull().sum()
dataset.isnull().head().sum()
modifieddataset=dataset.fillna("")

dataset=dataset.dropna()


