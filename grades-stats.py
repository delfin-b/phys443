#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#07/10/2022

import math
import matplotlib.pyplot as plt
import numpy as np


infile=open('data1.txt','r') #reading txt file
lines=infile.readlines()
mt1=[]
mt2=[]
fin=[]
lab=[]
hw=[]
att=[]

for line in lines:
	p=line.split()
	mt1.append((p[0]))
	mt2.append((p[1]))
	fin.append((p[2]))
	lab.append((p[3]))
	hw.append((p[4]))
	att.append((p[5]))
del mt1[0] #removing the first elements which are the titles
del mt2[0]
del fin[0]
del lab[0]
del hw[0]
del att[0]
#print(mt1,len(mt1))
infile.close()	

def mean(x):
	L=len(x)
	summ=0
	for i in range(0,L):
		summ=float(x[i])+summ
	mean=summ//L
	return mean

def mode(x):
	arr=max([x.count(a) for a in x])
	if arr > 1 :
		return [d for d in x if x.count(d)==arr] [0]
	else:
		return None

def median(x):
	sort_arr=sorted(x)
	L=len(x)
	if L%2 == 0:
		median=(sort_arr[int((L/2)-1)]+sort_arr[int(L/2)])/2
	else:
		median=sort_arr[int((L+1)/2)-1]
	return median

def std(x):
	L=len(x)
	std1=0
	for i in range(0,L):
		std1=(float(x[i])-mean(x))**2 + std1
	std=math.sqrt((std1)//float(L-1))
	return std
def skew(x):
	L=len(x)
	skew1=0
	for i in range (0,L):
		skew1= (float(x[i])-mean(x))**3 + skew1
		skew=(skew1)//(100*std(x))
		return skew
print('Mean_mt1: ', mean(mt1))
print('Mean_mt2: ', mean(mt2))
print('Mean_fin: ', mean(fin))
print('Mean_lab: ', mean(lab))
print('Mean_hw: ', mean(hw))
print('Mean_att: ', mean(att))

print ('mode_mt1: ', mode(mt1))
print ('mode_mt2: ', mode(mt2))
print ('mode_fin: ', mode(fin))
print ('mode_lab: ', mode(lab))
print ('mode_hw: ', mode(hw))
print ('mode_att: ', mode(att))


print('median_mt1: ', median(mt1))
print('median_mt2: ', median(mt2))
print('median_fin: ', median(fin))
print('median_lab: ', median(lab))
print('median_hw: ', median(hw))
print('median_att: ', median(att))

print('standard_deviation_mt1: ', std(mt1))
print('standard_deviation_mt2: ', std(mt2))
print('standard_deviation_fin: ', std(fin))
print('standard_deviation_lab: ', std(lab))
print('standard_deviation_hw: ', std(hw))
print('standard_deviation_att: ', std(att))

print('location_mt1: ', skew(mt1))
print('location_mt2: ', skew(mt2))
print('location_fin: ', skew(fin))
print('location_lab: ', skew(lab))
print('location_hw: ', skew(hw))
print('location_att: ', skew(att))


#here is how i convert data1 excel file to text file hocam
'''import xlrd
import scipy.stats as stats
from scipy.stats import norm

# opening the workbook as the use of xlrd module
workbook = xlrd.open_workbook("data1.xlsx")

# opening the worksheet 
worksheet = workbook.sheet_by_index(0)

numb_rows=worksheet.nrows - 1
numb_cells= worksheet.ncols -1
Arr= np.empty([worksheet.nrows-1,worksheet.ncols])
curr_row=-1
while curr_row< numb_rows:
	curr_row+=1
	row= worksheet.row(curr_row)
	if curr_row > 0:
		for col_ind, el in enumerate(row):
			Arr[curr_row-1,col_ind]= el.value
#print (type(Arr))
#print(len(Arr))

with open('data1.txt','w+') as txt_file:
	data=txt_file.read()
	txt_file.write(str(Arr))'''