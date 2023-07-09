#!/usr/bin/env python
# coding: utf-8

# In[9]:


import seaborn as sns
import pandas as pd


# In[11]:


Planets = pd.read_csv("C:/Users/Ayieko/Documents/MACHINE LEARNING TUTORIALS\ML/LOGISTIC REGRESSION/planets/archive/planets.csv")
print(Planets)


# In[12]:


Planets.head()


# In[14]:


### simple aggreegation in pandas
import numpy as np


# In[15]:


rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser

## aggregation returns reduced version of data


# In[16]:


ser.sum()


# In[17]:


ser.mean


# In[18]:


df = pd.DataFrame({'A': rng.rand(5),
                  'B': rng.rand(5)})
df


# In[19]:


df.mean()


# In[20]:


df.mean(axis='columns') # specifying the axis argument aggregates each row


# In[21]:


Planets.dropna().describe() # includes aggregates like minimum, maximum, standard deviation, 25%, 50% AND 75% PERCENTILES


# In[ ]:


### GroupBy: Split, Apply, Combine
# split functions breaks and groups a dataframe based on the value of the specified key
# apply function involves filtering, transformation within individual groups
## combine step merges the outcomes of the two operations above


# In[28]:


## let's create a dataframe and practice an example

df = pd.DataFrame({'Key': ['A', 'B', 'C', 'A', 'B', 'C'],
                  'Data': range(6)}, columns=['Key', 'Data'])
df.reset_index(inplace=True)
df.rename(columns={'index':'Index'}, inplace=True)
df


# In[26]:


df.groupby('Key') ## this code cannot compute the split-apply-combine operation with the groupby() function


# In[29]:


df.groupby('Key').sum() # applying the DataFrameGroupBy object produces a result


# In[43]:


# AGGREGATE, FILTER, TRANSFORM, APPLY
rng = np.random.RandomState(0)
df = pd.DataFrame({'Key': ['A', 'B', 'C', 'A', 'B', 'C'],
                  'Data1': range(6),
                  'Data2': rng.randint(0, 10, 6)},
                 columns = ['Key', 'Data1', 'Data2'])
df


# In[44]:


### aggregation
df.groupby('Key').aggregate(['min', np.median, max]) ### combining and computing the 3 aggregates
# prints the aggregations of the two dataframes separately


# In[45]:


df.groupby('Key').aggregate({'Data1': 'min',
                            'Data2': 'max'})
# prints the 'min' of Data1, and 'max' of Data2


# In[46]:


# filtering

"""
filter drops data based on group featires
example, we might need to keep all groups in which the standard deviation
is larger than some critical value
"""
def filter_func(x):
    return x['Data2'].std() > 4

print(df); print(df.groupby('Key').std());
print(df.groupby('Key').filter(filter_func))


# In[47]:


### transformation
# transformation returns tanformed version of the full data to recombine
# the output is in the shape as the input

# example
df.groupby('Key').transform(lambda x: x - x.mean())


# In[48]:


## The apply() method
# this is an arbitrary function to the group results

def norm_by_Data2(x):
    # x is the DataFrame of group values
    x['Data1'] /= x['Data2'].sum()
    return x


# In[49]:


print(df); print(df.groupby('Key').apply(norm_by_Data2))

# this function changes a DataFrame and returns it to either an object or a scalar


# In[50]:


# we have been spliting a dataframe using a single column name
# we can split using a key, which can be any list, series
L = [0, 1, 0, 1, 2, 0]
print(df); print(df.groupby(L).sum())


# In[51]:


## we can group by df.groupby('key')
print(df); print(df.groupby(df['Key']).sum())


# In[52]:


# a dictionary pr series mapping index to group
df2 = df.set_index('Key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
print(df2); print(df2.groupby(mapping).sum())


# In[53]:


# also, we can pass any python function that wil input index value and output group
print(df2); print(df2.groupby(str.lower).mean())


# In[54]:


## a list of valid keys
##### preceding key choices can be combined to a group on a multi-index
df2.groupby([str.lower, mapping]).mean()


# In[ ]:





# In[ ]:




