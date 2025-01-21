#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr= np.arange(0,10)


# In[3]:


arr


# In[4]:


arr+5


# In[5]:


arr*arr


# In[6]:


arr-arr


# In[7]:


arr/arr


# In[8]:


np.sqrt(arr)


# In[9]:


np.log(arr)


# In[10]:


arr.sum()


# In[11]:


arr.mean()


# In[12]:


arr.max()


# In[13]:


arr.var()


# In[15]:


arr2d=np.arange(0,25).reshape(5,5)


# In[16]:


arr2d


# In[17]:


arr2d.sum()


# In[27]:


arr2d.sum(axis=1) #axis 0=columns 1=rows


# In[ ]:




