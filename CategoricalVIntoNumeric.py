#A2 setAq2
# Write a python program the Categorical values in numeric format for a given dataset

import numpy as np
#ass2setaQ.2write a python program the categorical values in numeric format for agiven  dataset


import pandas as pd
dataset = pd.read_csv("WeatherData.csv")
dataset
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
dataset['Outlook'] = le.fit_transform(dataset.Outlook)
dataset['Temp'] = le.fit_transform(dataset.Temp)
dataset['Humidity'] = le.fit_transform(dataset.Humidity)
dataset['Playgolf'] = le.fit_transform(dataset.Playgolf)
dataset['Windy'] = le.fit_transform(dataset.Windy)
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:5].values
from sklearn.preprocessing import StandardScaler
st_x=StandardScaler()
x1=st_x.fit_transform(x)
print(x1)

