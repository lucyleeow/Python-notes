# -*- coding: utf-8 -*-
"""
pandas
#######

Library for working with heterogeneous data (not just numerical).
"""

#%%
# Data structures
# ***************
#
# Series
# ======
#
# 1D, values (``.values()``) with associated index ('data labels'; ``.index```).
# Can be thought of as fixed length ordered dictionary. Default index is
# integers starting from 0. You can use index to select values::
#
#   my_series['a']
#   my_series[['a', 'b']]
#
# You can also use values::
#
#   my_series[my_series < 0]
#
# Can be used like dictionary. Below will return ``True`` if that index exists
# in the series::
#
#   'a' in my_series
#
# You can also convert a dictionary to a series. This will result in a series
# with the index sorted (alphabetically/numerically). You can specify order by
# using the arugment ``index``.
#
# Dataframe
# =========
#
# Has both row and column index.
#
# You can create a dataframe using a dictionary::
#
#   df = {'colname1': [<data>]
#         'colname2': [<data>]}
#
# You can specify column order with argument ``columns`` which takes a list of
# columm names (indicies).
#
# You can also use a nested dictionary. The outer dictionary specifies the
# column indicies and the inner specifies the row indicies::
#
#   df = ({'colname1': {'row1': 2.3, 'row2': 4.5}})
#
# Access a column using ``df.colname`` or ``df['colname']``. The former is not
# possible for columns with spaces or punctuation. This will return a series
# with the same index as the df. The series returned is a view on the data,
# so changes will also result in changes to the original dataframe.
#
# Useful functions:
#
# * ``df.T`` - transpose a df.
# * ``.values()`` - gives you values as array. There is only one dtype of the
#   resulting array - the 'highest' dytpe, like 'coercion' in R.
#
# Index objects
# =============
#
# * Index objects hold axis labels and axis names (e.g., name of the column and
# rows).
# * They are immutable, making it safer to share among data structures.
# * Can contain duplicate labels
# * Behaves like a set and set logic (intersection, union)
#
# ``reindex()`` - creates a new object, with the data conformed to the new index:
#

import pandas as pd

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2

#%%
# Indexing
# ********
#
# **Series**
#
# * Using integer position ``[start:stop:step]``.
# * Using row labels ``[start:stop]``. End point is inclusive.
# * Using boolean e.g., ``[series < 2]``
#
# Note you can set (assign new values) with indexing as well.
#
# **Dataframe**
#
# * Using integer position: ``df[start:stop:step]`` allows row selection. This
#   is the only way that integer position can be used.
# * Using column labels: ``df['col1']`` or ``df[['col1', 'col2']]``.
# * Using boolean: ``df < 0`` will return a boolean array same shape as the df,
#   thus ``df[df < 5]`` will allow you to subset the whole df. This will only
#   work if your df is only numerical.
#
# loc and iloc
# ============
#
# * **loc** - used for subsetting by label e.g.,
#   ``df.loc['col1', ['row1', 'row2']]``
#
#   * single label or list of labels selects rows
#   * ``df.loc[:, 'col']`` selects columns
#
# * **iloc** - used for subsetting by integer position e.g.,
#   ``df.iloc[2, [2,4]]``, ``df.iloc[2, 2:4]``
#
#   * single integer selects rows
#
# **Boolean**
#
# ``loc`` will take a Pandas series of boolean values and 'merge' using index.
# Thus if you performed a comparison on a column then changed the order (e.g.
# sort descending) of the resulting boolean series, it would subset according
# to the original index.
#
# ``iloc`` on the other hand will NOT take a pandas series, but only a list
# of booleans (if you were performing a comparison on a column of the df,
# you would neet to use ``tolist()``). The idea behind this is to inform the
# user that this set of booleans is completely separate from the df.
#
# Number indexes
# ===============
#
# There may be ambiguity when row labels are integer numbers. Are you specifying
# the xth position or the row label x? To be consistent, data selection is
# always by row label. Use ``loc`` and ``iloc`` to be more specific.
#
# Arthimetic operations
# *********************
#
# Arthimetic operations will be performed after aligning by index. E.g., when
# adding one series to another, the indicies are aligned first, and the
# operation is performed on matching indicies. This is also done for dataframes
# (e.g., ``df1 + df2``)
# on column and row labels. If the row or column label is not common to the
# two dataframes, the result for that row or column will be all ``NaN``s.
#
# You can use ``fill_value`` argument to use a default value that is not
# ``NaN``::
#
#   df1.add(df2, fill_value=0)
#
# There are functions with similar arguments for other basic operations
# (e.g., ``div()``, ``mul()``)
#
# Operations with dataframe and series
# ************************************
#
# When using ``+`` or ``-`` etc pandas matches index of series with column
# labels of df and the
# operation is performed on each row. If a column is not found, the df and
# series will be re-indexed to form the union. If you use the operation
# function (e.g., ``add()``), you can specify ``axis``.
#
# Numpy functions (e.g., ``np.abs()``) also work on series and df.
#
# The ``apply()`` function lets you apply a function to a column of data
# (default, think of this as applying to the 'rows' of a column) or row of
# data (``axis=1``). The function can return 1 value or a series of multiple
# values::

import numpy as np
df = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

df.apply(f)

#%%
# To perform an operation on all elements in a df use ``applymap()``.-
#
# Essential functions
# *******************
#
# * ``drop()`` to remove an element from series or a row/column (col: ``axis=1``)
#   from df
# * ``sort_index()`` sort lexigraphically by index
# * ``sort_values()`` use ``by`` to specify the column(s) if df
# * ``rank()`` gives you the ranking order of the series/df

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj.rank() # split ranking for same values

#%%
# Split apply combine
# *******************
#
# ``groupby()``
#
# * Results in a groupby object. It has not computed anything except
#   intermediate data about the group key.
#   data about the groupby key. The index of the grouped object is the key(s)
#   used to groupby.
# * You can use a external array (of the correct length) to groupby.
# * By default the numerical columns only are aggregated, and the transformation
#   applied to these columns only.
# * ``.size()`` returns the count of each group.
# * ``NA``s in the groupby key will result in that row being excluded.
# * Supports iteration, generating sequence of length 2 tuples
#   ``((<group key1>, <group key2>), <data of group>)``.
# * Groups axis=0 (rows) by default but you can groupby columns (``axis=1``)
# * To select specific columns use 'indexing'. Returned object will be either
#   grouped series or grouped df::
#
#   df.groupby('key1')['data1']
#   # note that the above is syntatic sugar for
#   df['data'].grouby(['key1'])
#
# * You can groupby using a dictionary (``{'<row label>': '<group>', ...}``.
#   This can be done with column labels as well. You can include labels that
#   do not occur in the df. You can also groupby a Series, where the index
#   of the series will be the row/column labels.
# * You can groupby using a function. The function will be called once per
#   index and the output value will be the group name. E.g., if you passed the
#   function ``len``, pandas will calculate the length of the index (string)
#   and the group name would be the integer that is the length of the index.
# * To pass several functions, use ``agg()``. This results in a df where the
#   column names are the function names.
#
#   * To specify name use
#     ``.agg([('<col>', <fun name>), ('<col2>', <fun2 name>)])``
#   * To specify different functions to different columns, us a dictionary
#     ``.agg({'<col>': <function>})
#   * Note that common 'aggregation' functions have optimised groupby methods.
#     If you are using one of these, you must give the function name as as
#     string. Others should be the function name not as a string.
#
#   using the ``apply()`` function-
# * To perform a user defined function use ``.apply()``. Like R, pass arguments
#   to your function by passing them to ``apply()``. Certain methods are
#   actually doing this under the hood e.g., ``.describe()`` is doing
#   ``apply(lambda x: x.describe())``.
# * ``cut()`` outputs a ``Categorical`` object, splitting your data into
#   a desired number of bins. You can groupby this categorical object.
#
# **Indexes**
#
# When performing a 'aggregation' function (e.g, mean, median), which returns
# summary value(s) of the original data, the original index information is
# not passed on to the resulting df. This is because you cannot, as the
# resulting value(s) are summary value(s) from data.
#
# For this type of function ``as_index=True`` sets the group data as the index
# and ``as_index=False`` uses default integers, starting from 0, as the index.
# If the group data was a column of the original data, this column will
# remain in the output df. The ``group_keys`` parameter produces the same
# result in this case.
#
# When performing a non-aggregation function (e.g., take the lowest 5 values)
# it is possible to return the original index. ``as_index=True`` in this case
# sets the group keys as the index, and the original index is kept as index
# as well. ``as_index=False`` will still have 2 indicies, original and
# an index of the keys, but the group keys will just be integers:

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
def top(df, n=5, column='sepal_length'):
   return df.sort_values(by=column)[-n:]

iris.groupby('species', as_index=True).apply(top)

#%%

iris.groupby('species', as_index=False).apply(top)

#%%
# ``group_keys=True`` in this case sets the group keys as the index. Setting
# this to ``False`` results in only one index, the original one. Changing
# ``as_index()`` changes nothing.

iris.groupby('species', group_keys=True).apply(top) # default

#%%

iris.groupby('species', group_keys=False).apply(top)

#%%
# In summary, for dfs where it is possible to have more than 1 index (e.g., the
# original and the group keys) ``set_index`` lets you specify whether the
# index should be the group keys or just numbers. ``group_keys`` lets you
# specify whether there should be a group keys index (as well as the original).
#
# Transform
# =========
#
# The ``transfomr()`` function creates a new column. It can either produce
# an object of the same shape as the input group, or a scalar that can be
# broadcast to the shape.

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                  'value': np.arange(12.)})
df.groupby('key').transform(lambda x: x.mean())

#%%
# For built in 'aggregation' functions, you can pass a string alias (as with
# ``agg()`` above). Performing the below function gives the same results
# whether you use ``transform()`` or ``apply()``::
#
#   def normalize(x):
#       return (x - x.mean()) / x.std()
#
# It is however, faster to use the built-in aggregate functions with
# transform::
#
#   normalized = (df['value'] - g.transform('mean')) / g.transform('std')
#
# Categorical data
# ****************
#
# Factors in R efficiently stores categorical data. The data called dimension
# tables and the key references are called categorical or dictionary encoded
# representation. Use ``<encoding>.take(<data>)`` to restore the original
# values. Performance (e.g., with ``groupby``) is better with the data in
# this format.
#
# pandas as the ``category`` dtype. You can convert a column to category
# using ``.astype('category')``. The values of the resulting data is of type
# ``pandas.Categorical``, which has 'categories' (encoding) and 'codes' (data)
# attributes. The ``.from_codes()`` function can take a codes and category list
# to create a category object.
#
# Unless specified, it assumes no order of the catgeories. Use ``ordered=True``
# to specify order. The printed output will have ``<`` signs between the
# categories to show order.
#
# Reshaping
# *********
#
# * ``stack()`` 'pivots' from the columns to rows, to long.
# * ``unstack()`` 'pivots' from rows into columns, to wide.
#

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                    name='number'))
data

#%%

result = data.stack()
result

#%%
# The result is 1D with hierachichal indexing. By default the innermost
# level is 'unstacked' (made into columns). Unstacking can result in missing
# values if all the values in the level are not found in each of the
# subgroups. Note that stacking filters out missing values by default.-

result.unstack()

#%%

df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))
df

#%%
df.unstack()

#%%
# Note that above the column indexing is now hierachichal and the innermost
# hierachy of the row labels was 'unstacked'.
#
# ``pivot()``
#
# Syntax: ``pivot(<row index>, <col index>, <values>)``
#
# If you omit the last argument, all resulting columns will be used as
# the 'value', with hierachichal column indexing.
#
# Note that ``pivot()`` is equivalent to creating a hierchichal index with
# ``set_index()`` then ``unstack()``.
#
# ``melt()``
#
# ``pd.melt(<df>, <group col(s)>, <value col(s)>)``
#
# You 'group col(s)' is -
#

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
df

#%%

pd.melt(df, ['key'])

# %%
