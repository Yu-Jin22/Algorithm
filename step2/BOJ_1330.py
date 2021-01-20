#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1330

a,b = map(int, input().split())

if a>b :
    print('>')
elif a<b :
    print('<')
else : 
    print('==')

