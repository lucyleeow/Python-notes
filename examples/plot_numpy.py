# -*- coding: utf-8 -*-
"""
Numpy
#######

Fundamental package for scientific computing.
"""

#%%
# Introduction 
# ============
#
# Memory-efficient container that provides fast numerical operations. Also 
# known as 'array oriented computing'. Implemented in C and Fortran - thus the
# speed.
#
# Main idea is vectorisation - not for loops.
#
# Numpy arrays:
# 
# * only one data type
# * structure must be determined (shape)
# * statically typed (data type and shape are pre-determined)
# * dimensions are called axes
# * number of axes is called rank
# * supports linear functions e.g. dot product
# 
# Not as flexible as Python list but more efficient in numerical operations.
#
# Help
# ====
# 
# * Access help file with ``<np.function_name>?``
# * Look for function with ``np.lookfor('<search term>')``
# * Glob search with ``<np.fun_start>*``
#
# Creating arrays
# ================
#
# You can create an array of a specific size filled with zero's or one's. 
# Specify shape by giving the shape as a tuple.

import numpy as np

np.ones((3,3))
np.zeros((3,3))

#%%
# The ``np.empty()`` just gives you 'rubbish':

np.empty(10)
# Interestingly, numpy may re-use numpy array already in memory:
a = np.ones((3,3))
A = np.empty(9)
A

#%%
# In the above case, there was already an array of size '9', so numpy reuses
# the data saved in this memory.

#%%
#  You can also use ``np.arange``:

ra = np.arange(10) 
print(ra)

print(type(ra))

#%%
# You can also use 'start, stop, step':

raf = np.arange(-1, 1, 0.1)  
print(raf) 

#%%
# There 2 similar functions, ``np.linspace`` and ``np.logspace``:

# start, end, number of elements
np.linspace(0, 10, 20)

# same but in log scale
np.logspace(0, np.e**2, 10, base=np.e)

#%%
# Generate numpy array with random numbers:

np.random.rand(10)
# random numbers from a standard normal distribution
np.random.randn(10)

#%%
# Diagonal Matrices:

# produces the numbers 1, 2 and 3 along diagonal
np.diag([1,2,3])
# adds offset
np.diag([1,2,3], k=-1)
# reverses order
np.diag([1,2,3], k=-1)


#%%
# A numpy array can also be created from a Python list object:

np.array([1,2,3,4])
np.array([[1,2],[3,4]])

#%%
# What happens here?

np.array([[1,2],[3,4,5]])

#%%
# Note that the ``dytpe=object``. This means ANY Python object and is difficult
# to work with. Here the numpy array is made of lists, it is of shape:

np.array([[1,2],[3,4,5]]).shape

#%%
# Numpy array object
# ===================
# An array object is composed of three parts:
# 
# * the data, usually in a contiguous chunk in memory
# * metadata about the data (ref: `SO 
#   <https://stackoverflow.com/questions/22053050/difference-between-numpy-array-shape-r-1-and-r`)`_`
#
#    * ``.flags`` - True, False flags about C_contiguous, writable etc
#    * ``.dtype`` - the data type e.g. int64
#    * ``.strides`` - discussed below
#    * ``.shape`` - the dimensions of the array, discussed more below
#
# .. image:: https://raw.githubusercontent.com/leriomaggio/numpy-euroscipy/7e308233843ddb6b4fe40a9ff6baf813909bb881/images/ndarray_with_details.png#
# 

#%%
# Broadcasting
#
# Start from the end of each array and start comparing
# good if equal or one is equal to 1
# 
# If shape of one is less than the other, assume 1