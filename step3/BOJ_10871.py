#!/usr/bin/env python
# coding: utf-8

# In[59]:


#10871 -1

n,x = map(int, input().split())
a = list(map(int, input().split()))

for i in a :
    if i < x :
        print(i, end=" ")
# 이렇게 풀면 n을 입력받는 의미가 없다


# In[63]:


#10871 -2

n,x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n) :
    if a[i] < x :
        print(a[i], end=" ")
# for문에 n을 활용하여 풀어봄

