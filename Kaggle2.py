#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


url='https://drive.google.com/file/d/1Sw9HbbKB_7XXz0JtmvPUBGViJOhVqq7A/view?usp=sharing'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url2)
print(df)


# In[5]:


df.shape


# In[7]:


df.head(5)


# In[18]:


df.tail(6)


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[16]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[17]:


df.isnull().sum()


# In[19]:


df.head(5)


# In[20]:


df.tail(5)


# In[30]:


missing_value_per=df.isnull().sum()/df.shape[0]*100 # give missing data in percentage


# In[31]:


missing_value_column_gre_20=missing_value_per[missing_value_per>20].keys()
missing_value_column_gre_20


# In[33]:


df2_drop_clm=df.drop(columns=missing_value_column_gre_20)


# In[35]:


df2_drop_clm.shape


# In[43]:


df_num=df2_drop_clm.select_dtypes(include=['int64','float64'])


# In[45]:


df_num.head()


# In[46]:


plt.figure(figsize=(25,25))
sns.heatmap(df_num.isnull())


# In[47]:


df_num[df_num.isnull().any(axis=1)]


# In[48]:


df_num.isnull().sum()


# In[49]:


missing_num_var=[var for var in df_num.columns if df_num[var].isnull().sum()>0]
missing_num_var


# In[56]:


plt.figure(figsize=(10,10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df_num[var], bins=20, kde_kws={'linewidth':5,'color':'#DC143C'})


# In[57]:


df4_num_mean=df_num.fillna(df_num.mean())


# In[58]:


df4_num_mean.isnull().sum().sum()


# In[59]:


df4_num_mean


# In[61]:


plt.figure(figsize=(10,10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df_num[var], bins=20, kde_kws={'linewidth':5,'color':'red'},label='Original')
    sns.distplot(df4_num_mean[var], bins=20, kde_kws={'linewidth':5,'color':'green'},label='Mean')
    plt.legend()


# In[62]:


df5_num_median=df_num.fillna(df_num.median())


# In[63]:


df5_num_median


# In[64]:


df5_num_median.isnull().sum().sum()


# In[66]:


plt.figure(figsize=(10,10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df5_num_median[var], bins=20, kde_kws={'linewidth':5,'color':'#DC143C'})


# In[69]:


plt.figure(figsize=(10,10))
sns.set()
for i, var in enumerate(missing_num_var):
    plt.subplot(2,2,i+1)
    sns.distplot(df_num[var], bins=20,hist=False, kde_kws={'linewidth':8,'color':'red'},label='Original')
    sns.distplot(df4_num_mean[var], bins=20,hist=False, kde_kws={'linewidth':5,'color':'green'},label='Mean')
    sns.distplot(df5_num_median[var], bins=20,hist=False, kde_kws={'linewidth':3,'color':'k'},label='Median')
    plt.legend()


# In[73]:


for i, var in enumerate(missing_num_var):
    plt.figure(figsize=(20,20))
    plt.subplot(3,1,1)
    sns.boxplot(df_num[var])
    plt.subplot(3,1,2)
    sns.boxplot(df4_num_mean[var])
    plt.subplot(3,1,3)
    sns.boxplot(df5_num_median[var])


# In[74]:


df_concanat=pd.concat([df_num[missing_num_var],df4_num_mean[missing_num_var],df5_num_median[missing_num_var]],axis=1)


# In[76]:


df_concanat[df_concanat.isnull().any(axis=1)]


# In[ ]:




