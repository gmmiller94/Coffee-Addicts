#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


## Set Working Directory

import os
os.chdir("/Users/georg/Documents/GitHub/Coffee-Addicts")


# In[3]:


## import dataset
caffeine = pd.read_csv("Data/caffeine.csv")
caffeine.head()


# In[4]:


caffeine.info()


# In[ ]:


# Data Wrangling


# In[5]:


## rename columns

caffeine.rename(columns={'Volume (ml)' : 'Volume'}, inplace=True)
caffeine.rename(columns={'Caffeine (mg)' : 'Caffeine'}, inplace=True)
caffeine.rename(columns={'drink' : 'Drink'}, inplace=True)
caffeine.rename(columns={'type' : 'Type'}, inplace=True)


# In[6]:


caffeine.head()


# In[7]:


# I am not interested in water caffeinated drinks, so I will drop that

## drop row

index_names = caffeine[ caffeine['Type'] == 'Water'].index

caffeine.drop(index_names, inplace = True)


# In[8]:


caffeine.info()


# In[9]:


## I want to get a better look at correlation and look for outliers

g=sns.pairplot(caffeine,hue='Type')
g.fig.set_figheight(10)
g.fig.set_figwidth(20)
plt.show() 


# In[10]:


#I am looking at the drinks with the highest level of caffeine

## I start with putting them in descending order
caff1=caffeine[['Drink','Caffeine']]
caff1=caff1.sort_values('Caffeine',ascending=False)
caff1[0:20]


# In[11]:


## Total Caffeine Ranking Graph

fig = px.bar(caff1[0:30], x='Drink', y='Caffeine',title="Total Caffeine Ranking")
fig.show()


# In[ ]:


# The first question I would like to answer with this data is, which top 10 drinks give me the most caffeine in the smallest volume?

## I will explore more in R


# In[ ]:


# The second question I want to answer is, what is the healthiest caffeinated beverage in terms of highest caffeine content to lowest calorie/volume ratio?


# In[ ]:


# The third question I want to answer is, does volume affect caffeine quantity?

