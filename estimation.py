#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#11/11/2022

#import math
#import matplotlib.pyplot as plt
import numpy as np


infile=open('city.txt','r') #reading txt file
lines=infile.readlines()
house_no=[]
sell_price=[]
house_size=[]



for line in lines: #creating data as separate arrays
    p=line.split()
    house_no.append((int(p[0])))
    sell_price.append(int(p[1]))
    house_size.append(int(p[2]))
#print ('mean1',np.mean(sell_price))

arr3=np.zeros(len(house_no)) #arr3 is a new array of price/size
for i in range (len(house_no)):
	arr3[i]=sell_price[i]/house_size[i]
#print ('new array tl/m2',arr3)
#print('mean2', np.mean(arr3))


def margin_error(arr,n): #margin error with 1.96 since we are asked 95% confidence interval
	margin_err=1.96*((np.std(arr))/(n**(0.5)))
	return margin_err

def Interval_Estimation(arr,n): #interval estimation function
	x_bar=np.mean(arr) #average
	m=[x_bar-margin_error(arr,n),x_bar+margin_error(arr,n)] #+- error
	return m


print ('(Point Estimation) Estimated average of houses in the city: ',
       f'{np.mean(sell_price):.4}') #taking 4 significant figures
print ('(Point Estimation) Estimated average of houses of price per area in the city: '
       ,f'{np.mean(arr3):.4}')
print ('(Interval Estimation 95%) Estimated selling price ',
       f'{Interval_Estimation(sell_price,len(sell_price))[0]:.4}', '< should be < ', 
       f'{Interval_Estimation(sell_price,len(sell_price))[1]:.4}',' for all similar houses in the city')
print ('(Interval Estimation 95%) Estimated selling price per area ',
       f'{Interval_Estimation(arr3,len(arr3))[0]:.4}', '< should be < ', 
       f'{Interval_Estimation(arr3,len(arr3))[1]:.4}',' for all similar houses in the city')
