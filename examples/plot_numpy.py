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

a = np.arange(10)
print(a)

print(type(a))

#%%
# You can also use 'start, stop, step':

a = np.arange(-1, 1, 0.1)
print(a)

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
# .. image:: https://raw.githubusercontent.com/leriomaggio/numpy-euroscipy/7e308233843ddb6b4fe40a9ff6baf813909bb881/images/ndarray_with_details.png
#

#%%
# Broadcasting
# ============
#
# Start from the end of each array and start comparing, 2 dimensions are
# compatible if equal or one is equal to 1. The size of the resulting array
# is the size that is not 1 along each axis of the inputs.
#
# If shape of one is less than the other, assume 1 for the 'missing' axes.
# E.g., the following arrays are compatible:
#
#   Array A: 8 x 8 x 3
#   Array B:         3
#
# Indexing
# ========
#
# Ref: `Numpy docs <https://numpy.org/doc/stable/reference/arrays.indexing.html#indexing>`_,
# `advanced indexing <https://towardsdatascience.com/numpy-indexing-explained-c376abb2440d>`_
#
# Basic slicing
# -------------
#
# Notation: ``N`` = number of dimensions, ``n`` = number of elements in dim
# being sliced.
#
# * Occurs when you use slice object (start:stop:step notation), integer or
#   tuple of slice objects and integers.
# * Always creates view of original array.
# * Slice object defaults: start(0):stop(n):step(1)
# * If number of objects is less than ``N``, ``:`` assumed for all subsequent
#   dimensions.

a = np.arange(12).reshape((3,4))
a[:1].shape

# * Eliipsis expands to the number of ``:`` objects needed for the selection
#   tuple to index all dimensions.
# * ``newaxis`` expands by one unit-length dimension.
# * An integer returns the element at that index. It reduces the dimensionality
#   of the returned object (to prevent single dimensions staying around). If
#   you wish to keep the dimension you can do ``i:i+1`` instead.
# * If there is more than one non ``:`` entry, it acts like repeated
#   application of slicing. ``x[ind1,...,ind2,:]`` = ``x[ind1][...,ind2,:]
#
# NaNs
# ====
#
# NaN = result of calculation that does not have a sensible numerical answer.
# Also commonly used for missing data. ``NaN``s compare as different to
# everything, including other ``NaN``s.

np.NaN != np.NaN

# %%
# Reasoning, you generally cannot say that ``NaN`` producing calculations
# are equal to each other so the safest thing to do is set them to be not
# equal.

np.sqrt(-1) == (np.inf - np.inf)

# %%
# You can have -ve ``NaN`` - it is a bit pattern and the sign bit can be
# -ve or +ve. There is also a 'quiet' signalling bit - if set, CPU sets flag
# that raises exception. Quiet ``NaN``s propagate along quietly.
#
# Memory usage
# ============
#
# Doing multi-step calculations via arrays will use large amount of memory.
# For example:

size = [100]
a = np.ones(size, dytpe=np.float32)
b = np.full(size, 5.0, dytpe=np.float32)
c = np.full(size, np.pi, dytpe=np.float32)
output = np.add(a, np.multiply(b, c))

# %%
# All arrays are the same size. Peak memory usage is 5x size of the array. The
# result of the first multiply calculation will be sitting in memory as
# un-named array. This intermediate array will be sitting in memory. Although
# it will disappear after the last line finished, the peak memory usage is
# still 5x array size.
#
# Data from ``b`` and ``c`` will get pulled in from memory, do multipication,
# back out to memory, pull this and ``a`` back through CPU to do addition.
# Movement between CPU and memory, impossible to avoid. Cython or Numba
# can loop over individual values and put things straight into ``output``.
#
# C and Fortran perform better in this regard.