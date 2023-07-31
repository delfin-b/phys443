#!/usr/bin/python
#python 3.8.
#Delfin Bengisu Gürkan
#2212868
#25/11/2022

import math
import matplotlib.pyplot as plt
import numpy as np

datat=np.loadtxt('data.txt', skiprows=1)#excluding the first row that indicates the titles
data=np.transpose(datat) #taking the transpose 
#print (data)

column1, column2=data[0],data[1]
#column1.sort()
#print (column1)

plt.scatter(column1,column2, color='maroon')
plt.title('Scatter Plot')
plt.xlabel('column1')
plt.ylabel('column2')
plt.show()

def Sigma(x,y): #in the sake of simplicity i directly wrote a function for SS values
    sigma=np.sum(x*y)-(np.sum(x)*np.sum(y))/len(x)
    return sigma
S_xx=Sigma(column1,column1)
S_yy=Sigma(column2,column2)
S_xy=Sigma(column1,column2)

#print('doğru mu', S_xx)
#print(S_yy)
#print(S_xy)

beta = S_xy/S_xx
alpha = np.mean(column2)-beta*np.mean(column1)
#print (alpha,beta)

fit=np.array(alpha + beta*column1) #linear fit equation
#print (fit)


plt.plot(column1,column2, 'co')
plt.plot(column1, fit, '-r', label='fit=a+Bx')
plt.title('Scatter Plot')
plt.xlabel('column1')
plt.ylabel('column2')
plt.legend()
plt.savefig('scatter.pdf', format='pdf')#save figure as pdf format
plt.show()


def Anova(x,y,reg_df,n): #reg df is regression df
    SSR=Sigma(x,y)**2/Sigma(x,x)
    SSE=Sigma(y,y)-SSR
    r_squared=1-SSE/Sigma(y,y)
    var=math.sqrt(SSE/n)
    MSR=SSR/reg_df
    MSE=SSE/(n-2) #n-2 is error df
    F_val=MSR/MSE
    m=[SSR,SSE,r_squared,var,MSR,MSE,F_val] #in order to caöö the values i have in the function, i returned them as array elements
    return m

Anov=Anova(column1,column2,1,len(column1)) #regression df is 1 here
#print(Anov)
print('Source\t\t','df\t','SS\t\t','MS\t\t','F\n',
      'Regression\t','1\t', f'{Anov[0]:.3}','\t', f'{Anov[4]:.3}','\t', f'{Anov[4]/Anov[5]:.3}','\n' 
      'Error\t\t',len(column1)-2,'\t',f'{Anov[1]:.3}','\t',f'{Anov[6]:.3}','\n',
      'Total\t\t',len(column1-1),'\t',f'{S_xx:.3}','\n')
#printing as if a table