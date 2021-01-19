#!/usr/bin/env python
# coding: utf-8

# In[54]:


#2588

a= int(input())
b= input()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))


# In[59]:


a= int(input())
b= input()
for i in range(2,-1,-1) :
    print(a*int(b[i]))
print(a*int(b))

