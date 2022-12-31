#ass5 setbq1 slip12q2 and slip19
#write a python program to impement linear regression model for a car dataset.
#dataset can be dwonloaded from
#http://www.w3schools.com/python/python_ml_multiple_regression.asp
import pandas
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

df = pandas.read_csv('data3.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr =LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
test_y=regr.predict(X)
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)