#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[34]:


df=pd.read_csv(r"C:\Users\User\Desktop\python\dailyActivity_merged.csv")


# In[35]:


df.info()


# In[36]:


cols= ['Id','ActivityDate','TotalSteps','VeryActiveMinutes','FairlyActiveMinutes','LightlyActiveMinutes','SedentaryMinutes','Calories']
df=df[cols]


# In[37]:


df


# In[38]:


df=df.rename(columns={'ActivityDate':'Date'})


# In[39]:


df


# In[40]:


df['TotalMinutes']= df.VeryActiveMinutes+df.FairlyActiveMinutes+df.SedentaryMinutes+df.LightlyActiveMinutes


# In[41]:


df['TotalHours']= df['TotalMinutes']/60


# In[42]:


df


# In[43]:


df.Date=pd.to_datetime(df.Date)


# In[44]:


df


# In[45]:


df.info()


# In[47]:


import datetime as dt
df['DayOfWeek']= df.Date.dt.day_name()


# In[48]:


df


# In[49]:


df.isnull().sum()


# In[50]:


df.duplicated().sum()


# In[51]:


df.describe()


# In[57]:


plt.figure(figsize=((6,4)))
plt.hist(df.DayOfWeek,bins=7,color='lightskyblue',width=.6)
plt.grid(True)
plt.xlabel('day of week')
plt.ylabel('freq')
plt.title('freq by day of week')
plt.show()


# In[60]:


df.info()


# In[63]:


sns.heatmap(df.corr(numeric_only=True))


# In[66]:


plt.figure(figsize = ((8,6)))
plt.scatter(df.TotalSteps,df.Calories ,c= df.Calories)
plt.xlabel('steps')
plt.ylabel('calories')
plt.title('calories / steps relationship')
plt.show()


# In[69]:


plt.figure(figsize = ((8,6)))
plt.scatter(df.TotalHours,df.Calories ,c= df.Calories)
plt.xlabel('hours')
plt.ylabel('calories')
plt.title('calories / hours relationship')
median_hours= 24
median_calories=2134

plt.axhline(median_calories,color='blue',label='median of calories')
plt.axvline(median_hours,color='red',label='median of hours')

plt.show()


# In[73]:


very_active_minutes = df['VeryActiveMinutes'].sum()
fairly_active_minutes = df['FairlyActiveMinutes'].sum()
lightly_active_minutes = df['LightlyActiveMinutes'].sum()
sedentary_minutes = df['SedentaryMinutes'].sum()

minutes = [
    very_active_minutes,
    fairly_active_minutes,
    lightly_active_minutes,
    sedentary_minutes
]

labels = [
    'Very Active',
    'Fairly Active',
    'Lightly Active',
    'Sedentary'
]

plt.pie(minutes, labels=labels, autopct='%1.1f%%')
plt.title('Activity Minutes Distribution')
plt.show()


# In[74]:


df.to_csv('Final_Fitness.csv', index=False)


# In[ ]:




