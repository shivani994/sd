
#ASS2setbQ1write a python program to rescal the data between 0 and 1.(use inbult dataset)
# normalized data attribute for the iris dataset
from sklearn import preprocessing
from sklearn.datasets import load_iris

#load the iris dataset
iris=load_iris()
print(iris.data.shape)
#separete data from target attribute
X=iris.data
y=iris.target
#normalize the data attribute
normalized_X =preprocessing.normalize(X)