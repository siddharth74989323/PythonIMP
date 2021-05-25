#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


df=pd.read_csv(r'H:\PythonProject\Kaggle\Data\HousePrediction\HousePred\train.csv')
print(df)


# In[9]:


df.shape


# In[10]:


df.head(6)


# In[24]:


lstcolumns=df.columns
print(lstcolumns)


# In[28]:


pd.set_option('display.max_columns',None)


# In[29]:


df.head(6)


# In[30]:


pd.set_option('display.max_rows',None)


# In[31]:


df.head(6)


# In[32]:


df.tail(6)


# In[33]:


df.info()


# In[36]:


df.isnull().sum()


# In[37]:


df.isnull().sum().sum()


# In[38]:


plt.figure(figsize=(25,25))
sns.heatmap(df.isnull())


# In[39]:


df.isnull().sum()/df.shape[0]*100 # give missing data in percentage


# In[87]:


df.isnull().sum()/df.shape[0]*100


# In[90]:


drop_column=nul_var[nul_var>17].keys()


# In[91]:


drop_column


# In[92]:


df2_drop_clm=df.drop(columns=drop_column)


# In[93]:


df2_drop_clm.shape


# In[95]:


plt.figure(figsize=(25,25))
sns.heatmap(df2_drop_clm.isnull())


# In[96]:


df2_drop_row=df2_drop_clm.dropna()


# In[97]:


df2_drop_row.shape


# In[98]:


plt.figure(figsize=(25,25))
sns.heatmap(df2_drop_row.isnull())


# In[99]:


df2_drop_row.isnull().sum()


# In[100]:


df2_drop_row.isnull().sum().sum()


# In[106]:


df3_drop_row=df2_drop_row


# In[105]:





# In[107]:


df3_drop_row.columns


# In[108]:


df3_drop_row.select_dtypes(include=['int64','float64']).columns


# In[113]:


sns.displot(df['MSSubClass'])
sns.displot(df3_drop_row['MSSubClass'])


# num_var=['Id', 'MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
#        'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
#        'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
#        'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
#        'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
#        'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
#        'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
#        'MoSold', 'YrSold', 'SalePrice']
# 
# plt.figure(figsize=(25,25))
# for i,var in enumerate(num_var):
#         plt.subplot(9,4,i+1)
#         sns.displot(df['MSSubClass'],bins=20)
#         sns.displot(df3_drop_row['MSSubClass'],bins=20)

# In[116]:


num_var=['MSSubClass', 'LotArea', 'OverallQual', 'OverallCond', 
         'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 
         'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 
         'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 
         'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 
         'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 
         'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 
         'MoSold', 'YrSold', 'SalePrice']

plt.figure(figsize=(25,25)) 
for i,var in enumerate(num_var): 
    plt.subplot(9,4,i+1) 
    sns.displot(df[var],bins=20) 
    sns.displot(df3_drop_row[var],bins=20)


# In[117]:


df3_drop_row.select_dtypes(include=['object']).columns


# In[118]:


lstcatcol=df3_drop_row.select_dtypes(include=['object']).columns


# In[119]:


lstcatcol


# In[121]:


df['MSZoning'].value_counts()/df.shape[0]*100


# In[134]:


pd.concat([df['MSZoning'].value_counts()/df.shape[0]*100,
          df3_drop_row['MSZoning'].value_counts()/df3_drop_row.shape[0]*100],
          axis=1,keys=['MSZoning_old','MSZoning_Clean','MSZoning_diff'])


# In[146]:


def Cat_var_dis(var):
    return pd.concat([df['MSZoning'].value_counts()/df.shape[0]*100,
          df3_drop_row['MSZoning'].value_counts()/df3_drop_row.shape[0]*100],
          axis=1,keys=['MSZoning_old','MSZoning_Clean','MSZoning_diff'])


# In[140]:


Cat_var_dis('MSZoning')


# In[142]:


lstcatcol


# In[148]:


for var in lstcatcol: 
    print(var)
    Cat_var_dis('MSZoning')


# In[ ]:




