#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#09/12/2022


import math
import matplotlib.pyplot as plt
import numpy as np


datat=np.loadtxt('data8.txt', skiprows=0, usecols=(1,2,3,4,5,6,7,8,9,10), unpack=False)#excluding the first row that indicates the titles
#print(datat)
arr_i=datat[0]
n=len(arr_i)
t_i=datat[1]
N_i=datat[2]
Ln_Ni=datat[3] #y_i=Ln_Ni

'''def Alpha(x,y):
	alpha=(np.sum(y)*np.sum(x**2)-np.sum(x*y)*np.sum(x))/(len(x)*np.sum(x**2)-(np.sum(x))**2)
	return alpha
'''

def Beta(x,y,n):#calculating the slope
	beta= (n*np.sum(x*y)-np.sum(y)*np.sum(x))/(n*np.sum(x**2)-(np.sum(x))**2)
	return beta

def Alpha(x,y):#calculating the alpha value
	alpha=np.mean(y)-Beta(x,y,n)*np.mean(x)
	return alpha

def var_square(x):# calculating sigma. no need for writing it as a function though...
	return 1/x


#reconstructing the variables alpha and beta as C and D
D=Beta(t_i, Ln_Ni,n)
C=Alpha(t_i,Ln_Ni)
tau=-1/D


upp=np.sum(1/var_square(N_i))
loww=np.sum(1/var_square(N_i))*np.sum((t_i**2)/var_square(N_i)) - (np.sum(t_i/var_square(N_i)))**2
err_beta= upp/loww #error on beta

err_tau = math.sqrt(err_beta) * (1/D**2) #error on lifetime
#print ((np.sum(1/var_square(N_i))))

#fit_y=math.log(C)-math.e**(-t_i/tau)

A=math.e**C #tha constant value needed for the chi square calculation

CHI_SQR=[]
for i in range (n): #constructing chi square here
	CHI_SQR.append(((N_i[i]-A*(math.e**(-t_i[i]/tau)))**2)/(A*math.e**(-t_i[i]/tau)))
dof=8 #10-2
if np.sum(CHI_SQR)/dof <=1:
	print('Fit is correlated with data, dof=', dof, 'chi square= ', np.sum(CHI_SQR), 'error on beta= ', err_beta)
else:
	print('Fit is NOT correlated with data, dof=', dof, 'chi square= ', np.sum(CHI_SQR), 'error on beta= ', err_beta, '. Change your fit.')


upp=np.sum(1/var_square(N_i))
loww=np.sum(1/var_square(N_i))*np.sum((t_i**2)/var_square(N_i)) - (np.sum(t_i/var_square(N_i)))**2
err_beta= upp/loww #error on beta

err_tau = math.sqrt(err_beta) * (1/D**2) #error on lifetime
#print ((np.sum(1/var_square(N_i))))

x_axis=np.linspace(0, 135, 1000) #creating new axis arrays so that can plot the linear fit
y_axis=C+D*x_axis
sigma=[]
for i in range (n):
	sigma.append(abs(Ln_Ni[i]-y_axis[i]))


#plotting
plt.scatter(t_i, Ln_Ni, color='maroon')
plt.plot(x_axis, y_axis, '-r', label='Fit')
plt.errorbar(t_i, Ln_Ni, yerr=sigma, fmt='-o', label='Values with error, sigma')
plt.title('t vs N')
plt.xlabel('t')
plt.ylabel('N')
plt.grid(True)
plt.legend()
plt.show()