#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#21/10/2022

import math
import matplotlib.pyplot as plt
import numpy as np


infile=open('supernovae.txt','r') #reading txt file
lines=infile.readlines()
event_no=[]
interval_no=[]



for line in lines: #creating arrays
	p=line.split()
	event_no.append((int(p[0])))
	interval_no.append(int(p[1]))
#print(event_no)
#print (interval_no)
#print(type(event_no[0]))
infile.close()	

def weighted_mean(x): #defining weighted mean, lambda
	up_sum=0
	low_sum=0
	for i in range(0,len(x)):
		up_sum=(float(x[i])*i)+up_sum
		low_sum=float(x[i])+low_sum
	return up_sum/low_sum

#print (weighted_mean(interval_no))

def Poisson(n,x,y): #n is lambda in poisson distribution formula
	m=[]
	summ=0
	for i in range(0,len(y)):
		summ=summ + float(y[i])
	for i in range(0, len(x)):
		poisson=(math.exp((-1*n))*((n)**i))/math.factorial(i)
		m.append(poisson*summ)
	return m


Lambda= weighted_mean(interval_no) #defining variables that will be plotted
expectation=Poisson(Lambda, event_no, interval_no)
#print(expectation)


#step plot is used in order to get piece-wise constant plot
fig, (axs1,axs2) = plt.subplots(1,2)

axs1.set_title('Poisson Distribution')
axs1.set_xlabel('Number of Events')
axs1.set_ylabel('Number of Intervals')
axs1.step(event_no, expectation, where='mid', color='maroon', label='Expectation')
axs1.grid(True)
axs1.scatter(event_no, expectation,label='data') #shows data as points
axs1.legend()

axs2.set_title('Poisson Distribution')
axs2.set_xlabel('Number of Events')
axs2.set_ylabel('Prediction (Fitted with poisson)')
axs2.step(event_no, interval_no, where='mid', color='maroon', label='Raw data')
axs2.grid(True)
axs2.scatter(event_no, interval_no,label='data')
axs2.legend()
axs2.set_yscale('log') #converting the base of y axis
#plt.legend()
plt.show()