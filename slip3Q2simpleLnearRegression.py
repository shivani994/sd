#ass5 seta q1 slip3Q2
#consider the following observation/ data And apply simple linear regression and find out
# estimated coefficent b0 and b1.(use numpy package)
# x=[0,1,2,3,4,5,6,7,8,9,11,13]
# y=[1,3,2,5,7,8,8,9,10,12,16,18]
import matplotlib.pyplot as plt
import numpy as np


def estimate_coe(x,y):
#number of observation/ point  
 n=np.size(x)

#mean of x,y vecto
 m_x=np.mean(x)
 m_y=np.mean(y)

# caculating cross- deviation and deviation about x
 SS_xy=np.sum(y*x)-n*m_y*m_x
 SS_xx=np.sum(x*x)-n*m_x*m_x

#calculating regression coefficients
 b_1=SS_xy/SS_xx
 b_0=m_y-b_1*m_x
 return(b_0,b_1)
def plot_regression_line(x,y,b):
    #plotting the actual points as scatter plot
    plt.scatter(x,y,color="m",
      marker="o",s=30)
    #predicted response vector
    y_pred=b[0]+b[1]*x

    #plotting the regression line
    plt.plot(x,y_pred,color="g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plot
    plt.show()
def main():
    #observation/data
    x=np.array([0,1,2,3,4,5,6,7,8,9,11,13])    
    y=np.array([1,3,2,5,7,8,8,9,10,12,16,18])  
    
    #estimate coefficient
    b=estimate_coe(x,y)
    print("Estimate coefficient:\nb_0={}\nb_1={}".format(b[0],b[1]))

    #plotting regression line
    plot_regression_line(x,y,b)
__name__ =="__main__"
main()    


