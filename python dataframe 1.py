#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


##### dataset ####
data = {
    'student': ["Amit", "John", "Jacob", "David", "Steve"],
    'ranks': [1, 4, 3, 5, 2],
    'marks': [95, 70, 80, 60, 90]
}
res = pd.DataFrame(data)
print("Student Records\n\n", res)


# In[ ]:




