#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Saadullah khan
#Qs No 2:
A=int(input('What is the order Amount :'))
s=str(input('What is the state: '))
if(s== 'WI'):
	r=0.055
	F=A*r
	T=(A+(A*r))
	print("The tax is $",F,)
	print("The total is $",T,)
else:
	print("The Total is $",A,)

