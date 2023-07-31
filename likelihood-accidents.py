#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#02/12/2022

import math
import matplotlib.pyplot as plt
import numpy as np


#statistics 
acdts, freq = np.loadtxt('data6.txt', skiprows = 1, unpack = True) #syntax for reading txt file
bin=500
lambd_a = np.linspace(0.01, 0.50, num = bin) #defining lambda
LnL_array = [] #dummy array
n=647 

def LnL(n, freq, lambd_a):
	holder=1
	for i in range (len(freq)):
		holder = math.factorial(freq[i]) * holder
		LnL = (-len(freq) * lambd_a) + (math.log(lambd_a * n)) - math.log(holder)
	return LnL

def plot(x,y): #i wrote plot function
	plt.xlabel('lambda')
	plt.ylabel('Ln-likelihood')
	plt.title('Ln-likelihood Plot')
	plt.plot(x, y, 'o-')
	plt.plot(0.393, - 2963.16, 'r*', label='1 sigma') #by looking at the file, we can see that max ln is -2962.66 which related to 0.167 lambda
	#1 sigma related to 0.393 lambda which is -2963.16 ln
	plt.legend()
	plt.show()


for i in range (bin):
	L=lambd_a[i]
	LnL_array.append(LnL(n, freq, L))
print ('1_sigma=',  max(LnL_array) - 0.5)
plot(lambd_a, LnL_array)