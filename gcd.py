#!/usr/bin/env python
# coding: utf-8

# In[14]:


a,b = input().split()
i=1
GCD=0
while i<=int(a) and i<=int(b):
    if(int(a)%i)==0 and (int(b)%i)==0 :
        GCD=i
    i=i+1    
print(GCD)    


# In[ ]:





# In[ ]:




