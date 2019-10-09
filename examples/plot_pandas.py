# -*- coding: utf-8 -*-
"""
Pandas
#######

fff
"""

#%%
# dtype - object - means Python object - meaning could be anything and thus
# difficult to work with.
# Pandas is working on string object.

#%%
# loc vs iloc
# ************
#
# * **loc** - used for subsetting by reference  - e.g. to column names,
#   index (rowname)
# * **iloc** - used for subsetting by position
#
# Boolean
# ``loc`` will take a Pandas series and 'merge' using index. Thus if you
# performed a comparison on a column then changed the order (e.g. sort
# descending), it would subset according to the original index.
#
# ``iloc`` on the other hand will NOT take a pandas series, but only a list
# of booleans (if you were performing a comparison on a column of the df,
# you would neet to use ``tolist()``). The idea behind this is to inform the
# user that this set of booleans is completely separate from the df.

#%%
# Same values in one column but different in another 
# `SO <https://stackoverflow.com/questions/54043313/select-rows-from-a-pandas-dataframe-with-same-values-in-one-column-but-different>`_
#

