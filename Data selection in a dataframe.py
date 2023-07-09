#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


### Data selection in dataframe
# DataFrame as a dictionary

# example
area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
data = pd.DataFrame({'Area': area, 'pop':pop})
data


# In[5]:


## accessing individual series in the coliumns
# use dictionary-like indexing
data['Area']


# In[6]:


# we can use an attribute-like style to access column names that are strings
data.Area


# In[8]:


## the attribute-style can access the specific object like the dictionary-style above
data.Area is data['Area']


# In[9]:


data.pop is data['pop']


# In[11]:


# we can modify objects in the series using the dictionary-style syntax
data['Density'] = data['pop'] / data['Area']
data


# In[ ]:


### we shall learn more operations in pandas


# In[12]:


data.values ## views the dataframe as an enhanced 2D
            ## THIS EXAMINES THE RAW UNDERLYING DATA USING THE VALUE ATTRIBUTE


# In[13]:


data.T
# TRANSPOSES THE FULL DATAFRAME TO SWAP ROWS AND COLUMS


# In[14]:


data.values[0]


# In[15]:


data.iloc[:3, :2] # iloc syntax indexes underlying array


# In[16]:


data.loc[:'Illinois', :'pop']


# In[27]:





# In[38]:


data.loc[data.Density > 100, ['pop', 'density']] # loc indexer can combine masking and fancy indexing


# In[39]:


data.iloc[0, 2] = 90 # prints population equivalent to 90
data


# In[29]:


## ADDITIONAL CONVENTIONS
data['Florida':'Illinois'] ## access the data on the two states
                            ## slicing rows


# In[30]:


data[1:3] ## slices can refer to rows by number rather than by index


# In[31]:


data[data.Density > 100]  ## direct masking operation interpreted row-wise rather than column-wise


# In[33]:


Compensation = pd.Series({'Alex': 30000, 'Jomo': 40000, 'Kennedy': 10000, 'Professor': 5000, 'Jack': 20000})
Hours = pd.Series({'Alex': 10, 'Jomo': 5, 'Kennedy': 150, 'Professor': 250, 'Jack': 100})
data = pd.DataFrame({'Compensation': Compensation, 'Hours': Hours})
data

# prints a table for the compensation of the 5 employees


# In[34]:


data['Rate'] = data['Compensation'] / data['Hours']
data # prints hourly rate for the employees


# In[35]:


data.T ## transposes the data in the table


# In[37]:


data.iloc[0, 2] = 2000
data


# In[ ]:




