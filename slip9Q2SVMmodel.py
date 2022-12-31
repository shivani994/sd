#ass3setc slip9Q2
# write a python program to build an SVM model to cancer dataset .The Dateset is availble in the
#scikit-learn libeary.Check the accuracy of model with precision and recall


#import scikit-learn dataset library
from sklearn import datasets

#load dataset
cancer=datasets.load_breast_cancer()
#print the name of 13 features
print("Features:",cancer.feature_names)

#print data(feature)shape
cancer.data.shape

#print the cancer data feature(top 5 record)
print(cancer.data[0:5])

#print the cancer labels(0:malignant,1:benign)
print(cancer.target)

#import train_test_split function
from sklearn.model_selection import train_test_split

#split dataset into training set and test set
X_train,X_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)
#import svm model
from sklearn import svm

#create a svm classifier
clf=svm.SVC(kernel='linear')

#train the model using the training sets
clf.fit(X_train,y_train)

#predict the respose for test datset
y_pred=clf.predict(X_test)

#import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#model Accuracy: how often is the classifier correct
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))