#!/usr/bin/env python
# coding: utf-8

# # Levenshtein distance
# ## Implementation in Python and application on dog names

# ##### Daniele Rizzo

# In[1]:


import numpy as np
import pandas as pd 


# In[2]:


def compute_matrix(string1, string2):
    
    '''Returns a matrix (2D Numpy array) matrix 
    with first row with values from 0 to the length 
    of the first string and column with values 
    from 0 to the length of the second string.'''

    len1 = len(string1)
    len2 = len(string2)
    lev_mat = np.zeros((len1 + 1, len2 + 1))
  
    for i in range(len1 + 1):
        lev_mat[i,0] = i
  
    for i in range(len2 + 1):
        lev_mat[0,i] = i

    return lev_mat





def levenshtein_distance(string1, string2):
    
    '''Compute the matrix according to the Levenshtein algorithm
    to find the the least number of edit operations that 
    are necessary to modify one string to obtain another one,
    this number is also called edit distance.'''
    
    lev_mat = compute_matrix(string1, string2)
    for i in range(len(string1)):
        for j in range(len(string2)):
            
            if(string1[i] == string2[j]):
                k = 0
            else:
                k = 1
    
            lev_mat[i+1,j+1] = min(lev_mat[i,j+1] + 1, lev_mat[i+1,j] + 1, lev_mat[i,j] + k)

    return lev_mat[-1,-1]


#  # Application on the dog names in Zurich dataset

# Application of the previously defined function to find, in the dataset of dog names in Zurich, all names that have a Levenshtein distance of 1 to "Luca" 

# In[3]:


hunde = pd.read_csv("https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv")
hunde.head()


# In[4]:


lucalike = set()

for name in hunde.HUNDENAME:
    if(levenshtein_distance("Luca", name) == 1.):
        lucalike.add(name)


# In[5]:


lucalike

