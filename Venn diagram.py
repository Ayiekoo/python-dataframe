#!/usr/bin/env python
# coding: utf-8

# In[3]:


from matplotlib_venn import venn3
import matplotlib.pyplot as plt


# In[7]:


# Create the sets
Protein_A = set([1, 2, 3, 4, 5, 6, 7])
Protein_B = set([3, 4, 5, 6, 7, 9, 10])
Protein_C = set([1, 2, 5, 6, 7, 8, 9, 10])

# Create the Venn diagram
venn = venn3([Protein_A, Protein_B, Protein_C], set_labels=('Protein A', 'Protein B', 'Protein C'))

# Customize the Venn diagram
venn.get_label_by_id('100').set_text('Protein A')
venn.get_label_by_id('010').set_text('Protein B')
venn.get_label_by_id('001').set_text('Protein C')

# Display the Venn diagram
plt.title('Proteins')
plt.show()


# In[2]:



 


# In[ ]:




