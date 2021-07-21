#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[7]:


url = 'https://www.cbinsights.com/research-unicorn-companies'
df = pd.io.html.read_html(url)
df = df[0]


# In[8]:


df['Valuation ($B)'] = df['Valuation ($B)'].str.replace('$', '', regex=True).astype(float)


# In[9]:


df


# In[10]:


df.to_csv('UnicornList.csv', index=False)


# In[ ]:




