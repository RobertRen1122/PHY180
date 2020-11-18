import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt
import math
import pandas as pd


# change this if your filename is different
path="C:/Users/asus/Desktop/PHY180_Lab 2-4_Python_data/"
filename = "PHY180_lab_4.xlsx"
data=pd.read_excel(path+filename,sheet_name = 'Sheet2')


xlabel = "Mass (grams)"
ylabel = "Residual of Period (seconds)"


xdata=data['x']
ydata=data['y']
xerror=data['dx']
yerror=data['dy']


def T(L0):
    return 2*((0.3+L0*0.01)**0.5)

def my_func(xdata, k, b):
    return k * xdata**2 + b


popt, pcov = optimize.curve_fit(my_func, xdata, ydata)
# we have the best fit values in popt[], while pcov[] tells us the uncertainties

k=popt[0]
b=popt[1]
# best fit values are named nicely

u_k=pcov[0,0]**(0.5)
u_b=pcov[1,1]**(0.5)
# uncertainties of fit are named nicely

def fitfunction(xdata):
    return k * xdata**2 + b
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(xdata)
stop=max(xdata)
xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata)

plt.rcParams["figure.figsize"] = (10,6)
# Change the size of your plot - numbers are inches because USA

# add triple quotes here to generate loglog plot

plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".", label = 'Residuals with error bars')
# plot the data, fmt makes it data points not a line
plt.plot(xs, curve, label = "Line of best fit")
# plot the best fit curve on top of the data points as a line

plt.xlabel(xlabel, fontsize=14)
plt.ylabel(ylabel, fontsize=14)
plt.title("Relationship between mass and residuals of period", fontsize = 14)
# HERE is where you change how your graph is labelled!

plt.legend(loc="lower right", fontsize = 10)

plt.show()
# show the graph


print("k:", k, "+/-", u_k)
print("b:", b, "+/-", u_b)
# prints the various values with uncertainties

plt.rcParams["figure.figsize"] = (10,3)
# Change the size of your plot - numbers are inches because USA
