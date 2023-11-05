#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np




# In[6]:


df=pd.read_csv("classic_champions.csv")


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.shape


# In[12]:


df.columns


# In[13]:


df.info


# In[14]:


df.isin(['?']).sum()


# In[15]:


df.isnull().sum()


# In[24]:


df.describe()


# In[25]:


df.loc[0]


# In[26]:


df.iloc[0,0]


# In[27]:


df.iloc[[3,4]]


# In[28]:


x=df.iloc[:,:-1]
x


# In[29]:


y=df.iloc[:,:-1]
y


# In[31]:


df=df.drop_duplicates()


# In[ ]:





# In[ ]:




