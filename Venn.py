#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
get_ipython().system('pip install matplotlib-venn')


# In[8]:





# In[30]:





# In[29]:





# In[11]:





# In[28]:





# In[13]:


pip install matplotlib_venn


# In[16]:


from matplotlib_venn import venn3
import matplotlib.pyplot as plt


# In[17]:


# Create the sets
set_A = set([1, 2, 3, 4, 5])
set_B = set([3, 4, 5, 6, 7])
set_C = set([5, 6, 7, 8, 9])

# Create the Venn diagram
venn = venn3([set_A, set_B, set_C], set_labels=('Set A', 'Set B', 'Set C'))

# Customize the Venn diagram
venn.get_label_by_id('100').set_text('Set A')
venn.get_label_by_id('010').set_text('Set B')
venn.get_label_by_id('001').set_text('Set C')

# Display the Venn diagram
plt.title('Venn Diagram - Three Sets')
plt.show()


# In[18]:


from matplotlib_venn import venn2
import matplotlib.pyplot as plt



# In[19]:


# Create the sets
set_L0S4 = set(range(1, 238))
set_L04S4 = set(range(1, 1403))

# Create the Venn diagram
venn = venn2([set_L0S4, set_L04S4], set_labels=('L0S4', 'L04S4'))

# Display the Venn diagram
plt.title('Venn Diagram - L0S4 vs L04S4')
plt.show()


# In[23]:


get_ipython().system('pip install matplotlib-venn')


# In[25]:


from matplotlib_venn import venn4


# In[26]:


# Define the sets
set_A = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
set_B = set([3, 4, 5, 6, 11, 12, 13, 14])
set_C = set([5, 6, 7, 8, 13, 14])
set_D = set([2, 3, 5, 8, 11, 12, 13, 14, 15])

# Create the Venn diagram
venn = venn4([set_A, set_B, set_C, set_D], set_labels=('A', 'B', 'C', 'D'))

# Customize the Venn diagram
venn.get_label_by_id('1000').set_text('Set A')
venn.get_label_by_id('0100').set_text('Set B')
venn.get_label_by_id('0010').set_text('Set C')
venn.get_label_by_id('0001').set_text('Set D')

# Display the Venn diagram
plt.title('Venn Diagram - Four Circles')
plt.show()


# In[27]:


import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define the sizes of Circle A and Circle B
circle_a_size = 20
circle_b_size = 34
intersection_size = 15

# Create the Venn diagram
venn2(subsets=(circle_a_size, circle_b_size, intersection_size),
      set_labels=("Circle A", "Circle B"),
      set_colors=("dodgerblue", "darkorange"))

# Add a title
plt.title("Venn Diagram - Circle A vs Circle B")

# Display the plot
plt.show()


# In[ ]:




