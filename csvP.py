import pandas as pd
import sklearn
from sklearn import preprocessing as per
df=pd.read_csv("dataSurvey.csv")
print(df.head())
scaler=per.MinMaxScaler(feature_range=(0,1))
rescaleData=scaler.fit_transform(df)
rescaleData=pd.DataFrame(rescaleData,index=df.index,columns=df.columns)
print(rescaleData)