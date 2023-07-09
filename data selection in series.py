#!/usr/bin/env python
# coding: utf-8

# In[2]:


### data selection in series
import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                index=['a', 'b', 'c', 'd'])
data


# In[3]:


'a' in data


# In[4]:


list(data.items())


# In[5]:


# series as a 1D array
### slicing by explicit index
data['a':'c']


# In[6]:


# slicing by implicit integer index
data[0:2] # selects item 2 to the last


# In[7]:


# masking
data[(data > 0.3) & (data < 0.8)] # selects and prints data > 0.3 to < 0.8


# In[10]:


# INDEXERS; loc, iloc, and ix
data = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
data


# In[13]:


Ayiekos = pd.Series(['Wycliffe', 'Alex', 'Elphas', 'Angela'], index=[1, 2, 3, 4])
Ayiekos

## create  a dataset and indexes the data from 1


# In[14]:


## explicit index when indexing
data[1] # gets the first item in the dataset


# In[15]:


## explicit index when indexing
Ayiekos[2]  ## gets the second item in the dataset


# In[16]:


# implicit index when indexing
data[1:3] ## gets the second and the third object in the dataset


# In[ ]:




