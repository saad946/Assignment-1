#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Saadullah Khan warsi
#Qs No:5

print("Press C to convert from Fahrenhiet to Celsius")
print("Press F to convert from Celsius to Fahrenhiet")
A=str(input('Your choice: '))
if(A=='F'):
	c=int(input('Please Enter the temperature in Celsius: '))
	f=(((c*9)/5)+32)
	print("The temperature in Fahrenhiet is",f,)
if(A=='C'):
	f=int(input('please enter temperature in fahrenhiet: '))
	v= (((f-32)*5)/9)
	print("The temperature in Celsius is",v,)

