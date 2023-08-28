#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import re


# In[34]:


df = pd.read_csv('movie.csv')


# In[35]:


df["name"] = df['title'].str.extract(r'(.*(?=\s[(][0-9]{4}))')
df["year"] = df['title'].str.extract(r'((?<=[()])[0-9]{4})')


# In[50]:


df["genre"] = df["genres"].str.split("|")


# In[51]:


df2 = df[["movieId", "genre"]]
df2 = df2.explode("genre")
df2["genre"] = df2["genre"].replace("(no genres listed)", "")


# In[57]:


df2.to_csv("genre.csv",index=False)


# In[59]:


df = df[["movieId", "name", "year"]]


# In[61]:


df.to_csv("movie.csv",index=False)

