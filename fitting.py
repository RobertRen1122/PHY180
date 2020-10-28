# -*- coding: utf-8 -*-
"""
This program imports data from the file specified by the string filename
The first line of the file is ignored (assuming it's the name of the variables)
After that the data file needs to be formatted: 
number space number space number space number newline
Do NOT put commas in your data file!!
The data file should be in the same directory as this python file
The data should be in the order:
x_data y_data x_uncertainty y_uncertainty

Then this program tries to fit a function to the data points
It plots the data as dots with errorbars and the best fit line
It then prints the best fit information
After that, it plots the "residuals": ydata - fittedfunction(xdata)
That is it subtracts your fitted ideal values from your actual data to see 
what is "left over" from the fit
Ideally your residuals graph should look like noise, otherwise there is more
information you could extract from your data (or you used the wrong fitting
function)

If you want to change the graph labels, look for the plt.xlabel() commands
If you want to change the file name, that's the next line below this comment
"""
filename="test1.txt"
# change this if your filename is different


import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt


data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)
# load filename, take columns 0 & 1 & 2 & 3, skip 1 row, unpack=transpose x&y

xdata=data[0]
ydata=data[1]
xerror=data[2]
yerror=data[3]
# finished importing data, naming it sensibly

def my_func(theta,T0,B,C):
    T = T0 + B*theta + C*theta*theta
    return T

# this is the function we want to fit. the first variable must be the
# x-data (time), the rest are the unknown constants we want to determine

popt, pcov = optimize.curve_fit(my_func, xdata, ydata, maxfev=10000)
# we have the best fit values in popt[], while pcov[] tells us the uncertainties
T0 = popt[0]
B = popt[1]
C = popt[2]
# a=popt[0]
# tau=popt[1]
# T=popt[2]
# best fit values are named nicely
u_T0=pcov[0,0]**(0.5)
u_B=pcov[1,1]**(0.5)
u_C=pcov[2,2]**(0.5)
# uncertainties of fit are named nicely


def fitfunction(theta):
    T = T0 + B * theta + C * theta * theta
    return T
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(xdata)
stop=max(xdata)    
xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata) 

plt.rcParams["figure.figsize"] = (10,6)
# Change the size of your plot - numbers are inches because USA

plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".")
# plot the data, fmt makes it data points not a line
plt.plot(xs,curve)
# plot the best fit curve on top of the data points as a line
# plt.xlim(0, 50)
plt.ylim((1, 2))
plt.ylabel("time(s)")
plt.xlabel("amplitude(radians)")
plt.title("Period versus amplitude graph")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph


print("T0:", T0, "+/-", u_T0)
print("B:", B, "+/-", u_B)
print("C:", C, "+/-", u_C)
# print("phi:", phi, "+/-", u_phi)
# prints the various values with uncertainties

plt.rcParams["figure.figsize"] = (10,3)
# Change the size of your plot - numbers are inches because USA

residual=ydata-fitfunction(xdata)
# find the residuals
zeroliney=[0,0]
zerolinex=[start,stop]
# create the line y=0

plt.errorbar(xdata,residual,yerr=yerror,xerr=xerror,fmt=".")
# plot the residuals with error bars
plt.plot(zerolinex,zeroliney)
# plotnthe y=0 line on top

plt.xlabel("time(s)")
plt.ylabel("residuals of amplitude(radians)")
plt.title("Residuals of the best-fit curve")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph