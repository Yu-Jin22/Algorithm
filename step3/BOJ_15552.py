#!/usr/bin/env python
# coding: utf-8

# In[34]:


#15552
import sys

t = int(input())

for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)

