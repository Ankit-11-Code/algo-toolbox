#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a,b=map(int,input().split())
def euclid_gcd(a, b):
    if b == 0:
        return a
    c = a%b
    return euclid_gcd(b, c)

if a>b:
    gcd = euclid_gcd(a, b)
else:
    gcd = euclid_gcd(b, a)

print(a*b//gcd)


# In[ ]:





# In[ ]:




