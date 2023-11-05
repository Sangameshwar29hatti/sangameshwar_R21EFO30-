#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns



# In[12]:


df=pd.read_csv("classic_champions.csv")


# In[5]:


plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['champion_award'], marker='o', color='b')
plt.title('Prize Money Over the Years')
plt.xlabel('Year')
plt.ylabel('Prize Money ($)')
plt.grid(True)
plt.show()


# In[9]:


plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['champion_award'], marker='o', color='b')
plt.title('Prize Money Over the Years')
plt.xlabel('Year')
plt.ylabel('Prize Money ($)')
plt.grid(True)
plt.show()


# In[17]:


total_prize_by_country = df.groupby('represented_country_cham')['champion_award'].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.barh(total_prize_by_country['represented_country_cham'], total_prize_by_country['champion_award'])
plt.title('Total Prize Money by Champion\'s Country')
plt.xlabel('Total Prize Money ($)')
plt.ylabel('Country')


# In[21]:


plt.figure(figsize=(10, 5))
champion_counts = df['represented_country_cham'].value_counts()
plt.bar(champion_counts.index, champion_counts.values)
plt.title('Count of Champions by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)


# In[ ]:





# In[26]:


total_prize_by_country = df.groupby('represented_country_cham')['champion_award'].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.barh(total_prize_by_country['represented_country_cham'], total_prize_by_country['champion_award'])
plt.title('Total Prize Money by Champion\'s Country')
plt.xlabel('Total Prize Money ($)')
plt.ylabel('Country')


# In[27]:


plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['champion_award'], marker='o')
plt.title('Prize Money by Year')
plt.xlabel('Year')
plt.ylabel('Prize Money ($)')
plt.grid(True)


# In[29]:


cumulative_prize = df.groupby('year')['champion_award'].cumsum()
plt.figure(figsize=(10, 5))
plt.fill_between(df['year'], cumulative_prize, alpha=0.6)
plt.title('Cumulative Prize Money Over the Years')
plt.xlabel('Year')
plt.ylabel('Cumulative Prize Money ($)')


# In[30]:


plt.figure(figsize=(10, 5))
df.boxplot(column='champion_award', by='year')
plt.title('Prize Money Distribution by Year')
plt.xlabel('Year')
plt.ylabel('Prize Money ($)')


# In[31]:


plt.figure(figsize=(10, 5))
plt.scatter(df['year'], df['champion_award'], c='blue', marker='o')
plt.title('Scatter Plot of Champion Awards Over the Years')
plt.xlabel('Year')
plt.ylabel('Champion Award ($)')



# In[32]:


plt.figure(figsize=(10, 5))
plt.hist(df['champion_award'], density=True, color='skyblue', edgecolor='black', bins=10)
df['champion_award'].plot(kind='kde', color='red', linewidth=2)
plt.title('KDE of Champion Awards')
plt.xlabel('Champion Award ($)')
plt.ylabel('Density')

plt.show()


# In[33]:


plt.figure(figsize=(10, 5))
plt.hist(df['champion_award'], density=True, color='skyblue', edgecolor='black', bins=10)
df['champion_award'].plot(kind='kde', color='red', linewidth=2)
plt.title('Histogram and KDE of Champion Awards')
plt.xlabel('Champion Award ($)')
plt.ylabel('Density')


# In[ ]:




