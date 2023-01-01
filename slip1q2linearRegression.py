#slip1q2 aas5setaq3
#consider the student dara set . it can be  downloaded from:
#https://drive.google.com/open?id=loakZCv7g3mlmCSdv9J8kdSaqO 5 6dIOw
#write a program in pyhton to apply simple linear regression and find out mean absolute error, mean square error and root mean square error
 # Importing the libraries 

# Importing the libraries 
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import r2_score 

# Loading the dataset 
data = pd.read_csv('student1.csv') 

# Separating the features and target variable 
X= data.iloc[:, 0:1].values 
y = data.iloc[:, 0:1].values 

# Fitting the Linear Regression model to the dataset 
regressor = LinearRegression() 
regressor.fit(X, y) 
# Predicting the results 
y_pred = regressor.predict(X) 

# Calculating the errors 
MAE = mean_absolute_error(y, y_pred) 
MSE = mean_squared_error(y, y_pred) 
RMSE = np.sqrt(MSE) 

# Printing the errors 
print("Mean Absolute Error:", MAE) 
print("Mean Squared Error:", MSE) 
print("Root Mean Squared Error:", RMSE)