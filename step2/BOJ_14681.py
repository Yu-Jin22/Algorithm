#!/usr/bin/env python
# coding: utf-8

# In[26]:


#14681

x=int(input())
y=int(input())
#map사용하니까 런타임에러뜸

if x > 0 :
    print(1 if y > 0 else 4)
else :
    print(2 if y > 0 else 3)

