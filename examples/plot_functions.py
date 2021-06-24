
# -*- coding: utf-8 -*-
"""
#########
Functions
#########

* When a function encounters a ``return`` statement, it will stop. If it
  reaches the end of a function without encountering a ``return`` it will
  return ``None``.
* Positional ('required') parameters first, then keyword parameters

  * keyword parameters used to specify optional arguments (e.g., ``x=1.5``)
  * positions parameters still have a keyword, which you can use when
    calling a function

* Variables created in a function are local to the function and destroyed
  after the function is finished.

You can return multiple variables:
"""

def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()

#%%
# Technically the function is returning one object, a tuple, which is being
# unpacked into the result variables.
#
# Functions are objects meaning that they can:
#
# * be assigned to a variable
# * an element in a list, or any data structure
# * passed as an argument to another function
#
# When defining a function with a variable number of parameters you can use:
# ``*args`` (any number of positional arguments packed into a tuple) and
# ``**kwargs`` (any number of key word arguments packed into a dictionary).
#
# **Anonymous/lambda functions**
#
# Writing a function consisting of a single statement. It is used in cases
# where it is easier to write an anonymous function, rather than write out a
# full function. For example in data transformation (e.g., ``apply`` function
# in R)
#
# **Curring**
#
# Deriving functions from existing ones and setting values for a subset of the
# arguments.

def add_numbers(x, y):
    return x + y

from functools import partial

add_five = partial(add_numbers, 5)

#%%
# Parameters/arguments
# ====================
#
# Ref: `RealPython <https://realpython.com/lessons/positional-only-arguments/>`_
#
# Position only parameters (available from Python 3.8) indicated with ``/``.

def my_fun(x, /):
    return x

# %%
# All parameters before the ``/`` must be positional only (cannot use keyword).
# Useful when parameters have natural order but are hard to give good
# descriptive names to.
#
# Keyword only parameters (available from Python 3.0) indicated by ``*``. Any
# parameter after ``*`` must be specified via keyword.

def headline(text, /, border="~", *, width=50):
    pass

# %%
# ``text`` is positional only, ``border`` can be specified with or without
# keyword and ``width`` must be specified with keyword. Additionally, ``text``
# is not optional but the other two are.
