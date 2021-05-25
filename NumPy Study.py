#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Create one, two and three dimentional array and check their type

# In[2]:


arr_1d=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr_1d
print(type(arr_1d))


# In[3]:


arr_2d=np.array([[1,2,3],[4,5,6]])
arr_2d
print(type(arr_2d))


# In[4]:


arr_3d=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
arr_3d
print(type(arr_3d))


# # Check the dimention of Array return the dimention e.g 1 dim, 2 dim, 3 dim

# In[5]:


arr_1d.ndim


# In[6]:


arr_2d.ndim


# In[7]:


arr_3d.ndim


# # Press a or A to add  new cell above selected cell
# # Press b or B to add new cell below selected cell
# # Press (dd) double dd to delete selected cell

# # Check the size of array gives total  number of element of array

# In[8]:


arr_1d.size


# In[9]:


arr_2d.size


# In[10]:


arr_3d.size


# # Check the shape of array return tuple() first is row and second is column

# In[11]:


arr_1d.shape


# In[12]:


arr_2d.shape


# In[13]:


arr_3d.shape


# # Check the data type of array returns the data type of array elements

# In[14]:


arr_1d.dtype


# In[15]:


arr_2d.dtype


# In[16]:


arr_3d.dtype


# In[17]:


mx_1s=np.array([[1,1,1],[1,1,1],[1,1,1]])
mx_1s


# In[18]:


mx_once=np.ones(5)
mx_once


# In[19]:


mx_once.dtype


# # np.once() method gives matrix of 1
# # np.once() need one parameter that is tuple for shape of matrix (2,3) means two rows and three columns
# # We can check arguments of any methode by click in between the braces() 
# # and shift + tab there will be + button to expand the panel and we can see how much parameter it require and types of them, 
# 
# # All aboe np.once() is same for np.zeros()
# 
# # Shift + Enter we can execute the cell

# In[20]:


mx_once34=np.ones((3,4),dtype=int,)


# In[21]:


mx_once34


# In[22]:


mx_once34=np.ones((3,4),dtype=int)


# In[23]:


mx_once34


# In[24]:


mx_zeros=np.zeros((3,4))


# In[25]:


mx_zeros


# In[26]:


mx_zeros=np.zeros((3,4),dtype=bool)


# In[27]:


mx_zeros


# # In python bool data type False = 0 and True = 1

# In[28]:


mx_zeros=np.zeros((3,4),dtype=str)


# In[29]:


print(mx_zeros)


# # We can create empty matrix using following code

# In[30]:


mx_empty=np.empty((3,3))


# In[31]:


mx_empty


# # Third Video

# # Create 1d array by giving range start index, end index and interval

# In[32]:


arr_arange=np.arange(1,13,1)


# In[33]:


arr_arange


# In[34]:


arr_arange=np.arange(13)


# In[35]:


arr_arange


# In[36]:


arr_arange=np.arange(1,13,)


# In[37]:


arr_arange


# # linespace :- linespace create 1d array by providing start , end in equal part

# In[38]:


np_linespace=np.linspace(1,2,10)


# In[39]:


np_linespace


# # reshape :- reshape function convert 1d array to multi dimentional array

# In[40]:


arr_1d.reshape(3,4)


# In[41]:


arr_1d.reshape(4,3)


# In[47]:


arr_arange_reshape=np.arange(1,13).reshape(3,4)


# In[48]:


arr_arange_reshape


# # ravel :- ravel function convert multi dimentional array to 1d array

# In[44]:


arr_arange_reshape.ravel()


# # flattern  also convert multi dimentional array to 1d array

# In[46]:


arr_arange_reshape.flatten()


# # Transpose :- to convert Row to column we can use transpose or .T

# In[49]:


arr_arange_reshape


# In[50]:


arr_arange_reshape.transpose()


# In[51]:


arr_arange_reshape.T


# In[ ]:




