#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#04/11/2022

import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import random


n_sample=[1,2,5,10,15,20,50]
m=[] 
for n in n_sample:
	arr=np.zeros(1000) #dummy array
	for i in range (1000): #number of experiments is 1000 'm'
		exp_pdf=random.exponential(1, n) # creating exponential pdf array a=1:scale(given), size=n=from 1 to 50 
		mean=np.mean(exp_pdf) #calculating mean of chosed values
		arr[i]=mean
	m.append(arr)


fig, axs = plt.subplots(2,3)
fig.tight_layout(pad=2.0) #adjusting the space btw plots
axs[0,0].set_title('n=1')
axs[0,0].set_xlabel('mean')
axs[0,0].set_ylabel('frequency')
n, bins, patches= axs[0,0].hist(m[0], 100, alpha=1.0, density=True, color='maroon') #this is the syntax 
axs[0,0].grid(True)

axs[0,1].set_title('n=2')
axs[0,1].set_xlabel('mean')
axs[0,1].set_ylabel('frequency')
n, bins, patches= axs[0,1].hist(m[1], 100, alpha=1.0, density=True, color='maroon') #this is the syntax 
axs[0,1].grid(True)

axs[0,2].set_title('n=5')
axs[0,2].set_xlabel('mean')
axs[0,2].set_ylabel('frequency')
n, bins, patches= axs[0,2].hist(m[2], 100, alpha=1.0, density=True, color='maroon') #this is the syntax 
axs[0,2].grid(True)

axs[1,0].set_title('n=10')
axs[1,0].set_xlabel('mean')
axs[1,0].set_ylabel('frequency')
n, bins, patches= axs[1,0].hist(m[3], 100, alpha=1.0, density=True, color='maroon') #this is the syntax 
axs[1,0].grid(True)

axs[1,1].set_title('n=20')
axs[1,1].set_xlabel('mean')
axs[1,1].set_ylabel('frequency')
n, bins, patches= axs[1,1].hist(m[5], 100, alpha=1.0, density=True, color='maroon') #this is the syntax 
axs[1,1].grid(True)

axs[1,2].set_title('n=50')
axs[1,2].set_xlabel('mean')
axs[1,2].set_ylabel('frequency')
n, bins, patches= axs[1,2].hist(m[6], 100, alpha=1.0, density=True, color='maroon') #this is the syntax 
axs[1,2].grid(True)
plt.show()
