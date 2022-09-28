#!/usr/bin/env python
# coding: utf-8

# # practical 1 numpy practicals

# In[1]:


import numpy as np

array1d = np.array([1,2,3,4,5,6])
array2d = np.array([[1,2,3],[4,5,6]])

print(array1d)

print("-"*10)
print(array2d)


# # practical 2

# In[9]:


import numpy as np

array1d = np.array([1,2,3,4,5,6,7])
print(array1d.ndim)

array2d = np.array([[1,2,3],[4,5,6]])
print(array2d.ndim)

array3d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array3d = array3d.reshape(2, 3, 2)
print(array3d.ndim)


# # practical 3

# In[10]:


import numpy as np

array1d = np.array([1,2,3,4,5,6,7])
print(array1d.ndim)

array2d = np.array([[1,2,3],[4,5,6]])
print(array2d.ndim)

array3d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array3d = array3d.reshape(2, 3, 2)
print(array3d.ndim)


# # practical 4

# In[9]:


import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([1.5,2.5,0.5,6])
arr3 = np.array(['a','b','c'])
arr4 = np.array(["canada","Australia"],dtype='U5')
arr5 = np.array([555,666],dtype=float)

print("data type of array1 is:",arr1.dtype)
print("data type of array2 is:",arr2.dtype)
print("data type of array3 is:",arr3.dtype)
print("data type of array4 is:",arr4.dtype)
print("data type of array5 is:",arr5.dtype)


# # practial 5 

# In[7]:


import numpy as np

array1d = np.array([1, 2, 3, 4, 5, 6])
array2d = np.array([[1, 2, 3], [4, 5, 6]])
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("shape of array1 is:",array1d.shape)
print("shape of array2d is:",array2d.shape)
print("shape of array3d is:",array3d.shape)


# # practical 6

# In[2]:


import numpy as np

array1d = np.array([1, 2, 3, 4, 5, 6])
array2d = np.array([[1, 2, 3], [4, 5, 6]])
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("dimension of array1d is:",array1d.ndim)
print("dimension of array2d is:",array2d.ndim)
print("dimension of array3d is:",array3d.ndim)


# # practical 7

# In[10]:


import numpy as np

array1d = np.array([1, 2, 3, 4, 5, 6])
array2d = np.array([[1, 2, 3], [4, 5, 6]])
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#resize
print("dimension of array1d is:",array1d.size)
print("dimension of array2d is:",array2d.size)
print("dimension of array3d is:",array3d.size)

print("-"*10)

#reshape
print("shape of array1 is:",array1d.shape)
print("shape of array2d is:",array2d.shape)
print("shape of array3d is:",array3d.shape)


# # practical 8

# In[13]:


import numpy as np
 
thelist = [1, 2, 3]
print(type(thelist))  # <class 'list'>
 
array1 = np.array(thelist)
print(type(array1))  # <class 'numpy.ndarray'>

thetuple = ((1, 2, 3))
print(type(thetuple))  # <class 'tuple'>
 
array2 = np.array(thetuple)
print(type(array2))  # <class 'numpy.ndarray'>
 
array3 = np.array([thetuple, thelist, array1])
print(array3)


# # practical 9

# In[5]:

import numpy as np

array1d = np.array([1,2,3,4,5,6])

#get first value
print(array1d[0])
#print last value
print(array1d[-1]) #print(array1d[5])
#print forth value from first
print(array1d[3])
#print 5th value from last
print(array1d[-5]) #print(array1d[1])
#print multiple values
print(array1d[[1,-2]])


# # practical 10

# In[11]:


import numpy as np

array2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (array2d)
print("-"*10)
#print first row first col
print(array2d[0, 0])
#print first row sec col
print(array2d[0, 1])
#print fisrt row third col
print(array2d[0, 2])

#print first row second col
print(array2d[0, 1])
#print sec row sec col
print(array2d[1, 1])
#print third row sec col
print(array2d[2, 1])


# # practical 11

# In[12]:


import numpy as np
 
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array3d)
 
print(array3d[0, 0, 0])
print(array3d[0, 0, 1])
print(array3d[0, 0, 2])
 
print(array3d[0, 1, 0])
print(array3d[0, 1, 1])
print(array3d[0, 1, 2])
 
print(array3d[1, 0, 0])
print(array3d[1, 0, 1])
print(array3d[1, 0, 2])
 
print(array3d[1, 1, 0])
print(array3d[1, 1, 1])
print(array3d[1, 1, 2])


# # practical 12

# In[19]:


#Single Dimensional Slicing Operations
import numpy as np

array1d=([0,1,2,3,4,5,6,7,8,9])

#from index4 to last index
print(array1d[4:])
#from index0 to 4 index
print(array1d[:4])
#from index4 upto index 7
print(array1d[4:7])
#excluded last element
print(array1d[:-1])
#upto second last index
print(array1d[:-2])
#from last to first in reverse order
print(array1d[::-1])
#all odd no. in reversed order
print(array1d[::-2])
#all even no. in reversed order
print(array1d[-2::-2])
#all elements
print(array1d[::])


# # practical 13

# In[35]:


#Multidimensional Dimensional Slicing Operations 

array2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2d)

print("-"*10)
#2nd and 3rd col
print(array2d[:,1:3])

print("-"*10)
#2nd and 3rd row
print(array2d[1:3,0:3])

print("-"*10)
#reverse an array
print(array2d[-1::-1, -1::-1])


# # practical 14

# In[37]:


import numpy as np

array2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Permute the dimensions of an array.
arrayT = np.transpose(array2d)
print(arrayT)
 
print("-" * 10)
    
# Flip array in the left/right direction.
arrayFlr = np.fliplr(array2d)
print(arrayFlr)

print("-" * 10)

# Flip array in the up/down direction.
arrayFud = np.flipud(array2d)
print(arrayFud)
 
print("-" * 10)
    
# Rotate an array by 90 degrees in the plane specified by axes.
arrayRot90 = np.rot90(array2d)
print(arrayRot90)
 


# # prcatical 15

# In[41]:


import numpy as np

array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[7,8,9],[10,11,12]])

#Stack arrays in sequence horizontally (column wise).
arrayH=np.hstack((array1,array2))
print(arrayH)

print("-" * 10)

#Stack arrays in sequence vertically (row wise)
arrayV=np.vstack((array1,array2,))
print(arrayV)

print("-"*10)

#Stack arrays in sequence depth wise (along third axis)
arrayD=np.dstack((array1,array2))
print(arrayD)

print("-"*10)

#Appending arrays after each other, along a given axis
arrayC=np.concatenate((array1,array2))
print(arrayC)

print("-"*10)

#Append values to the end of an array
arrayA=np.append(array1,array2, axis=0)
print(arrayA)

print("-"*10)
arrayA=np.append(array1,array2, axis=1)
print(arrayA)


# # practical 16

# In[43]:


#Arithmetic Operations 

import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

#add
print(array1+array2)

print("-" * 20)

#sub
print(array1-array2)

print("-" * 20)

#multi
print(array1*array2)

print("-" * 20)

#div
print(array2/array1)

print("-" * 20)

#exponent
print(array1 ** array2)


# # practical 17

# In[2]:


#scalar arithmetic operations
import numpy as np

array1 = np.array([[10,20,30],[40,50,60]])

print(array1+2)
print("-" * 20)
print(array1-5)
print("-" * 20)
print(array1*2)
print("-" * 20)
print(array1/5)
print("-" * 20)
print(array1**2)


# # practical 18

# In[6]:


import numpy as np

array1=np.array([[10,20,30],[40,50,60]])

print(np.sin(array1))
print("-" * 40)
print(np.cos(array1))
print("-" * 40)
print(np.tan(array1))
print("-" * 40)
print(np.sqrt(array1))
print("-" * 40)
print(np.exp(array1))
print("-" * 40)
print(np.log10(array1))


# # practical 19

# In[10]:


import numpy as np

array1 = np.array([[10, 20, 30], [40, 50, 60]])
array2 = np.array([[2, 3, 4], [4, 6, 8]])
array3 = np.array([[-2, 3.5, -4], [4.05, -6, 8]])

#add
print(array1+array2)

print("-" * 40)

#multi
print(array1*array2)

print("-" * 40)

#power
print(array1**array2)


# # practical 20

# In[12]:


import numpy as np

array1=np.array([[10,20,30],[40,50,60]])

#mean
print(np.mean(array1))

print("-" * 40)

#standard deviation
print(np.std(array1))

print("-" * 40)

#variance
print(np.var(array1))

print("-" * 40)

#sum of array elements
print(np.sum(array1))

print("-" * 40)

#product of array elements
print(np.prod(array1))


# # practical 22

# In[23]:


import numpy as np

thearray = np.array([[10, 20, 30], [14, 24, 36]])

#logical_or
arr = np.logical_or(thearray<10, thearray>14)
print(thearray[arr])

#logical_and
arr1= np.logical_and(thearray<10, thearray>15)
print(thearray[arr1])

#logical_not
arr2=np.logical_not(thearray<20)
print(thearray[arr2])


# # practical 23

# In[26]:


#set operations

import numpy as np

array1 = np.array([[10, 20, 30], [14, 24, 36]])
array2 = np.array([[20, 40, 50], [24, 34, 46]])

#union
print(np.union1d(array1,array2))

#intersection
print(np.intersect1d(array1,array2))

#set difference
print(np.setdiff1d(array1,array2))


# In[ ]:




