#!/usr/bin/env python
# coding: utf-8

# In[3]:


#10952 -1

while True :
    a,b = map(int, input().split())
    if a ==0 and b==0 :
        break
    print(a+b)


# In[63]:


#10952 -2

while True :
    n = sum(map(int, input().split()))
    if n ==0 :
        break
    print(n)

