#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#30/12/2022



import math
import matplotlib.pyplot as plt
import numpy as np
import random



N=10000 #number of mc expereiments
nBins=100 #number of hist bins

data_x1, data_y1, pdf1 = [], [], [] #dummy array for x and y for Pa

for i in range(N):
	x_P_a= random.uniform(0.0, 1.0) #random uniform array
	P_a= (2*math.e**(-2*x_P_a))/(1-math.e**-2)  #function1
	##int_P_a= (2*e**(-2*x))/(-2*(1-e**-2))
	
	y1 = (-1/2)*(math.log(abs(math.e**(-2)-1)*x_P_a)) #solved for x 
	data_x1.append(x_P_a) #x array
	data_y1.append(y1) #y array that consist of inverted pdf
	pdf1.append(P_a) #array of function (y)


data_x2, data_y2, pdf2 = [], [], [] #dummy array for x and y for Pb

for j in range(N):
	x_P_b=random.uniform(0.0, 1.0) #random uniform array
	P_b= 3*x_P_b**3 #function2
	
	y2 = x_P_b**(1/3) #inverted version in terms of x
	data_x2.append(x_P_b) #x array
	data_y2.append(y2) #y array that consist of inverted pdf
	pdf2.append(P_b) #array of function (y)




fig= plt.figure(figsize= (13,5)) #plot object
fig_y1= fig.add_subplot(2,3,1) #subplot for y1
fig_y2= fig.add_subplot(2,3,2) #subplot for y2

fig_y1.hist(data_y1, nBins, color= 'maroon') #histogram plot for y1 (nBins=100)
fig_y1.set_ylabel('x(r) for Pa')

fig_y2.hist(data_y2, nBins, color= 'cyan')
fig_y2.set_ylabel('x(r) for Pb')

fig_combined1= fig.add_subplot(2,3,3) #plot object for y1 and y2 would be on the same graph
fig_combined1.hist(data_y1, nBins, color= 'maroon')
fig_combined1.hist(data_y2, nBins, color= 'cyan')
fig_combined1.set_ylabel('x(r) for Pa and Pb')
fig_combined1.set_xlim([0.0,1.0])

fig_Pa= fig.add_subplot(2,3,4)
fig_Pa.scatter(data_x1, pdf1, c='maroon')
fig_Pa.set_title('pdf Pa')

fig_Pb= fig.add_subplot(2,3,5)
fig_Pb.scatter(data_x2, pdf2, c='cyan')
fig_Pb.set_title('pdf Pb')

fig_combined2= fig.add_subplot(2,3,6) #plot object for y1 and y2 would be on the same graph
fig_combined2.scatter(data_x1, pdf1, c='maroon')
fig_combined2.scatter(data_x2, pdf2, c='cyan')
fig_combined2.set_title('pdf Pa and Pb')
fig_combined2.set_xlim(0.0,1.0)

plt.show()


