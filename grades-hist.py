#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#07/10/2022

import math
import matplotlib.pyplot as plt
import numpy as np
#i used xlrd module since we are not allowed to use pandas in class
import xlrd
import scipy.stats as stats
from scipy.stats import norm

# opening the workbook as the use of xlrd module
workbook = xlrd.open_workbook("data1.xlsx")

# opening the worksheet 
worksheet = workbook.sheet_by_index(0)
mt1 = []
mt2 = []
fin = []
lab = []
hw = []
att = []
# considering the datasheet as a big matrix
# i split it by column-wise as below and simply append the values
for i in range(1,worksheet.nrows): #rowmt1.append(worksheet.cell_value(i,0))
	mt2.append(worksheet.cell_value(i,1))
	fin.append(worksheet.cell_value(i,2))
	lab.append(worksheet.cell_value(i,3))
	hw.append(worksheet.cell_value(i,4))
	att.append(worksheet.cell_value(i,5))
#print(mt1)
#print (len(mt1)) I'VE CHECKED THE READING IS CORRECT

'''import pandas as pd
data = pd.read_excel('data1.xlsx')
print (data)'''
bins = 20
#n=289 #length of all arrays
fig, axs = plt.subplots(1,1, figsize = (9,6))
# Hocam I added my name as watermark just to try
# and also i tried some artistic manners only in the first plot
fig.text(0.9, 0.15, 'Delfin HW#1',
	fontsize=12,
	color='crimson',
	ha='right',
	va='top',
	alpha=0.5)

axs.grid(
	color ='pink',
	linestyle= 'solid',
	linewidth=0.5,
	alpha= 0.7)

######################### MT1 
mean1=np.mean(mt1)
std1=np.std(mt1)

n, bins, patches= plt.hist(mt1, bins, alpha=0.5, density=True) #this is the syntax 
plt.title('MT1 Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
#density true means that result is shown as probability density function in the bin
fit = stats.norm.pdf(np.linspace(np.max(mt1), np.min(mt1), len(mt1)), mean1, std1) #gaus fit by using np mean and np std
plt.plot(np.linspace(np.max(mt1), np.min(mt1), 289), fit, 'r-')
plt.grid(True)
plt.show()

######################## MT2
mean2=np.mean(mt2)
std2=np.std(mt2)

n, bins, patches= plt.hist(mt2, bins, alpha=0.5, density=True)
plt.title('MT2 Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
#density true means that result is shown as probability density function in the bin
fit = stats.norm.pdf(np.linspace(np.max(mt2), np.min(mt2), len(mt2)), mean2, std2) 
plt.plot(np.linspace(np.max(mt2), np.min(mt2), 289), fit, 'r-')
plt.grid(True)
plt.show()

####################### FINAL
meanfin=np.mean(fin)
stdfin=np.std(fin)

n, bins, patches= plt.hist(fin, bins, alpha=0.5, density=True)
plt.title('Final Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
#density true means that result is shown as probability density function in the bin
fit = stats.norm.pdf(np.linspace(np.max(fin), np.min(fin), len(fin)), meanfin, stdfin)
plt.plot(np.linspace(np.max(fin), np.min(fin), 289), fit, 'r-')
plt.grid(True)
plt.show()

####################### LAB
meanlab=np.mean(lab)
stdlab=np.std(lab)

n, bins, patches= plt.hist(lab, bins, alpha=0.5, density=True)
plt.title('Lab Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
#density true means that result is shown as probability density function in the bin
fit = stats.norm.pdf(np.linspace(np.max(lab), np.min(lab), len(lab)), meanlab, stdlab)
plt.plot(np.linspace(np.max(lab), np.min(lab), 289), fit, 'r-')
plt.grid(True)
plt.show()

###################### HW
meanhw=np.mean(hw)
stdhw=np.std(hw)

n, bins, patches= plt.hist(hw, bins, alpha=0.5, density=True)
plt.title('Homework Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
#density true means that result is shown as probability density function in the bin
fit = stats.norm.pdf(np.linspace(np.max(hw), np.min(hw), len(hw)), meanhw, stdhw)
plt.plot(np.linspace(np.max(hw), np.min(hw), 289), fit, 'r-')
plt.grid(True)
plt.show()

####################### ATTENDACE
meanatt=np.mean(att)
stdatt=np.std(att)

n, bins, patches= plt.hist(att, bins, alpha=0.5, density=True)
plt.title('Attendance Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
#density true means that result is shown as probability density function in the bin
fit = stats.norm.pdf(np.linspace(np.max(att), np.min(att), len(att)), meanatt, stdatt)
plt.plot(np.linspace(np.max(att), np.min(att), 289), fit, 'r-')
plt.grid(True)
plt.show()