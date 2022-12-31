#ASS5 SETAQ2 SLIP7Q2 and slip18
#consider the following observation data and apply simple linear regression and find out
#estimate coefficent b1 and b1 also analyse theperformance of  the model
#(use skelearn package)
#x=np.array([1,2,3,4,5,6,7,8)]
#y=np.array([7,14,15,18,19,21,26,23])

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([7,14,15,18,19,21,26,23])
slope, intercept, r, p, std_err = stats.linregress(x,y)
def myfunc(x):
     return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x,y)
plt.plot(x, mymodel) 
plt.show()    