#!/usr/bin/env python
# coding: utf-8

# In[1]:


# motivating pivot tables
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


Titanic = pd.read_csv("C:/Users/Ayieko/Documents/MACHINE LEARNING TUTORIALS/soon/titanic/Titanic-Dataset.csv")
print(Titanic)


# In[3]:


Titanic.head()


# In[5]:


# let's begin by grouping by gender, survival status
Titanic.groupby('Sex')[['Survived']].mean() ## prints the mean of males and females that survived


# In[8]:


Titanic.groupby('Survived')[['Age']].mean() # prints the mean age of survivors


# In[9]:


Titanic.groupby('Pclass')[['Survived']].mean() ## prints the mean of the passenger class that survived


# In[15]:


Titanic.groupby(['Sex', 'Pclass'])['Survived'].aggregate('mean').unstack()
## groups sex and passengerclass
## apply mean aggregate

## prints the mean aggregate of males and females who survived in the passenger classess


# In[17]:


## A 2D GroupBy IS CONVENIENT
## THE PIVOT_TABLE HANDLES MULTIDIMENSIONAL AGGREGATION
Titanic.pivot_table('Survived', index='Sex', columns='Pclass')


# In[21]:


### multilevel pivot tables
Age = pd.cut(Titanic['Age'], [0, 18, 80])
Titanic.pivot_table('Survived', ['Sex', Age], 'Pclass')
## checks age as a 3D dimension
#### we bin age using the pd.cut function


# In[22]:


## we can also use the pd.cut function when working with columns
#### we can add info on fare paid using the pd.qcut to automatically compute the quantiles
Fare = pd.qcut(Titanic['Fare'], 2)
Titanic.pivot_table('Survived', ['Sex', Age], [Fare, 'Pclass'])


# In[23]:


## we can call the signature of the pivot_table method of DataFrame
# call signature as pandas
DataFrame.pivot_table(data, values=None, index=None, columns=None,
                     aggfunc='mean', fill_value=None, margins=False,
                     dropna=True, margins_name='All')


# In[ ]:




