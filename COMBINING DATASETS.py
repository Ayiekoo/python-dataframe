#!/usr/bin/env python
# coding: utf-8

# In[1]:


# many-to-one joins
"""
contains many/duplicate entries
"""
import pandas as pd
import numpy as np


# In[16]:


df1 = pd.DataFrame({'Employee': ['Jake', 'Bob', 'Lisa', 'Sue'],
             'Group': ['Accounting', 'Engineering', 'Engineering', 'HR']}) ## has a column key; "employee"

df2 = pd.DataFrame({'Employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                   'Hire_date': [2004, 2008, 2012, 2014]}) # has a column key; "employee"
print(df1); print(df2)


# In[ ]:





# In[30]:


df2 = pd.DataFrame({'Employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                   'Hire_date': [2004, 2008, 2012, 2014]}) # has a column key; "employee"
df2


# In[29]:


df1 = pd.DataFrame({'Employee': ['Jake', 'Bob', 'Lisa', 'Sue'],
             'Group': ['Accounting', 'Engineering', 'Engineering', 'HR']}) ## has a column key; "employee"
df1


# In[17]:


df3 = pd.merge(df1, df2)
df3


# In[18]:


df4 = pd.DataFrame({'Group': ['Accounting', 'Engineering', 'HR'],
                   'Supervisor': ['Carly', 'Guido', 'Steve']})
print(df3); print(df4); print(pd.merge(df3, df4))


# In[19]:


## MANY-TO-MANY JOINS
df5 = pd.DataFrame({'Group': ['Accounting', 'Accounting', 
                             'Engineering', 'Engineering', 'HR', 'HR'],
                  'Skills': ['Math', 'Spreadsheets', 'Coding', 'Linux',
                            'Spreadsheets', 'Organization']})
print(df1); print(df5); print(pd.merge(df1, df5))


# In[26]:


print(df1); print(df5); print(pd.merge(df1, df5))


# In[20]:


df5.head()


# In[ ]:


## WE CAN SPECIFY THE COLUMN WHEN MERGING


# In[22]:


print(df1); print(df2); print(pd.merge(df1, df2, on='Employee'))


# In[23]:


## THE__ON AND THE RIGHT__ON KEYWORDS
# we can merge two datasets with different column names
# we use the left_on and right_on keywords when specifying the column names
df3 = pd.DataFrame({'Name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                   'Salary': [70000, 80000, 120000, 90000]})
print(df1); print(df3)


# In[24]:


df3.head()


# In[25]:


print(pd.merge(df1, df3, left_on="Employee", right_on="Name"))


# In[27]:


## this produces a redundant column
### we can drop the redundant column
pd.merge(df1, df3, left_on="Employee", right_on="Name").drop('Name', axis=1)

# dropping the redundant column(Name) leaves the employee column


# In[33]:


# specifying set arithmetic for joins
df6 = pd.DataFrame({'Name': ['Peter', 'Paul', 'Mary'],
                   'Food': ['Fish', 'Beans', 'Bread']},
                   columns=['Name', 'Food'])


# In[37]:


print(df6)


# In[34]:


df7 = pd.DataFrame({'Name': ['Mary', 'Joseph'],
                   'Drink': ['Wine', 'Beer']},
                  columns=['Name', 'Drink'])


# In[38]:


print(df7)


# In[39]:


print(pd.merge(df6, df7))


# In[40]:


print(pd.merge(df6, df7, how='inner')) ## the default joining method


# In[41]:


print(pd.merge(df6, df7, how='outer')) ## fills missing values with NaN


# In[42]:


df6 = pd.DataFrame({'Name': ['Peter', 'Paul', 'Mary'],
                   'Food': ['Fish', 'Beans', 'Bread']},
                   columns=['Name', 'Food'])
df7 = pd.DataFrame({'Name': ['Mary', 'Joseph'],
                   'Drink': ['Wine', 'Beer']},
                  columns=['Name', 'Drink'])

print(df6); print(df7); print(pd.merge(df6, df7))


# In[43]:


print(pd.merge(df6, df7, how='left')) ## joins over the left entry


# In[44]:


print(pd.merge(df6, df7, how='right')) # joins over the right entry


# In[51]:


### OVERLAPPING COLUMN NAMES
## the suffix keyword
df8 = pd.DataFrame({'Name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                  'Rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'Name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                   'Rank': [3, 1, 4, 2]})
print(df8); print(df9); print(pd.merge(df8, df9, on='Name')) # the dataframe will conflict in names


# In[52]:


"""
Because the output would have two conflicting column names, 
the merge function
automatically appends a suffix _x or _y to make the output columns unique. 
If these
defaults are inappropriate, 
it is possible to specify a custom suffix using the suffixes
keyword:
"""


# In[53]:


print(df8); print(df9)
print(pd.merge(df8, df9, on='Name', suffixes=["_L", "_R"]))


# In[3]:


## NOW, LET'S DO AN EXERCISE ON JOINING THREE DATASETS
import pandas as pd


# In[5]:


pop = pd.read_csv("C:/Users/Ayieko/Desktop/VENN/1/04232015altfuelstations.csv")
print(pop)


# In[7]:


inflation = pd.read_csv("C:/Users/Ayieko/Desktop/VENN/1/aggregate-household-income-in-the-past-12-months-in-2015-inflation-adjusted-dollars.csv")
print(inflation)


# In[8]:


ChronicDisease = pd.read_csv("C:/Users/Ayieko/Desktop/VENN/1/U.S._Chronic_Disease_Indicators__CDI_.csv")
print(ChronicDisease)


# In[3]:





# In[ ]:




