# -*- coding: utf-8 -*-
"""
######
Python
######

Python is an interpreted language (c.f. compiled) and can be used
interactively.

References used: SciPy lecture notes, Python for Data Science.
"""

#%%
# ***************
# Magic functions
# ***************
#
# These functions are prefixed by ``%``. In certain IDE's the setting
# ``automagic`` is
# enabled by default and allows you to omit the ``%`` sign. Useful magic
# functions include ``timeit``, which times the execution of short snippets
# using the timeit module from the standard library and ``debug``, which allows
# you to enter post-mortem debugging.
#
# **********
# Data types
# **********
#
# * numeric
#
#    * Integer
#    * Float
#    * Complex
#    * Boolean
#
# Type conversion is called 'casting'.
#
# **********
# Containers
# **********
#
# * **Lists** ordered, can have different types, mutable
#
#   * ``[-1]`` negative indexing = count from the back
#   * ``[start:stop:step]`` slicing syntax, 'stop' not inclusive
#   * ``list1 = list(list2)`` creates a new object that is in a different
#     memory area
#   * multiplying a list with a scalar concatenates the list 'scaler' times
#   * ``+`` will concatenated lists via making new list and copying the objects
#     over. ``extend()`` adds several elements to the end of a list and is less
#     expensive.
#   * ``sort()`` sorts in place
#
# * **Set** unordered collection of unique elements. Like dictionary without
#   keys. Create with ``set() or ``{}``.
#
#   * support mathematical operations like union, intersection and difference-
# * **Strings** immutable, accessible via indexing just like lists
#
#   * string formatting:

print(
    'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string')
)

#%%
# * **Dictionary** unordered, maps keys to values
#
#   * checking for a value is much faster c.f. lists as stored as hash table
#   * valid keys are anything that is hashable (mutable object)
#
# Dictionary functions:
#
# ``get()`` allows you to get a value from a dictionary, if a key
# is present and if not present, gives you a default value instead::
#
#   value = some_dict.get(key, default_value)
#
# ``setdefault`` is used for setting the values in a dictionary using another
# collection, e.g., a list.

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0] # first letter
    by_letter.setdefault(letter, [])

by_letter

# %%
# * **Tuple** immutable list. You can convert any sequence or iterator into a
#   tuple.

t = 1, 2, 3, 'string'
t = (1, 2, 3, 'string')
t = tuple([1,2,3])

#%%
# You can assign to a tuple-like expression of variables:

t = (1,2,3)
a, b, c = t

#%%
# The ``*rest`` syntax to select only the start of a tuple. ``rest`` will be a
# list:

t = 1,2,3,4
a, b, *rest = t
rest

#%%
# You can also use this to return multiple values from a function.
#
# ******************
# Sequence functions
# ******************
#
# ``enumerate``
# Let's you keep track of the index of the current item when you loop through a
# list:

some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
mapping

#%%
# ``zip``
#
# 'Pairs' up elements of a number of sequences (like a zip), to create a list
# of tuples:

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)    # returns a zip object
list(zipped)

#%%
# It can take an aribitrary number of sequences and will return ``n`` tuples,
# where ``n`` is the length of the shortest sequence.

#%%
# ************************
# List, dict comprehension
# ************************
#
# Create new list by filtering and transforming the elements in a list. The
# basic form is::
#
#   [expr for val in collection if condition]
#

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]

#%%
# Dictionary comprehension has a similar syntax::
#
#   dict_comp = {key-expr : value-expr for value in collection if condition}
#

loc_mapping = {val : index for index, val in enumerate(strings)}
loc_mapping

# ********************
# Mutable vs immutable
# ********************
#
# **Immutable**: string, tuple, int, float, boolean
# Cannot be altered in place.
#
# **Mutable**: list, dictionary, set
# Can be altered in place.
#
# You can think of a variable as a name 'bound' to an object. One object
# can have several 'names'. You can check this with the ``id()`` function
# which returns the memory location of where the variable is stored.
# You can also check if two objects have the same ID by using the ``is``
# function. If two 'variables' are point to the same object, changing one
# variable, changes the other variable pointint to that object.
#
# Creating two strings with the same value will result in the two variables
# pointing to the same object. This is to economise memory usable as these
# objects are immutable.

string1 = "hello"
string2 = "hello"
print(id(string1))
print(id(string2))

#%%
# Strings cannot be changed in place. Altering one of these strings results
# in Python creating a new string object at a different location in memory.

string1 += "e"
print(id(string1))

#%%
# Integers will appear to act the same way but this is for a different reason.
# To economise memory usage, CPython pre-allocates the first 262 integers on
# start up. This means that the numbers -5 to 256 (inclusive) are automatically
# bound to certain addresses in memory. CPython stores references to all of
# these integer objects in an array. When we 'create' an integer object, we
# are just telling our variable to point to an address stored in that array.
# These numbers are choosen as they are the most commonly used numbers.
# For some reason this does not seem to work with sphinx?

num1 = 1
num2 = 1
print(num1 is num2)

num3 = 1e1000
num4 = 1e1000
print(num3 is num4)

#%%
# A list is an array of pointers, which point to each element in the list. The
# values in the list are not stored in continuous place in memory.

list1 = [1,2,3]
print(id(list1))
print(id(list1[0]), id(list1[1]), id(list1[2]))

#%%
# When you change a list, the location of the list (array of pointers)
# does not change but the id of the values changes.
list1[0] = -1
print(id(list1))
print(id(list1[0]), id(list1[1]), id(list1[2]))

#%%
# This influences when a variable is modified inside a function. There are two
# ways that arguments (given when calling a function) from a function are
# passed to the parameters (which exist inside functions) of the function
# (`py course <https://www.python-course.eu/python3_passing_arguments.php>`_).
#
# * **call/pass by value** - the argument expression (e.g. ``x=2``) is
#   evaluated. If the expression is a variable (e.g. ``x=var1``) its value will
#   assigned (copied) to the corresponding parameter. This ensures that the
#   'global' variable will not be changed.
# * **call/pass by reference** - the function gets a reference to the argument,
#   rather than a copy of its value. The function can then modify the variable.
#   This saves computation time and memory space as arguments do not need to be
#   copied but variables can be 'mistakenly' changed in a function call.
#
# Python uses a mechanism known as 'call by object' or 'call by object
# reference'. If you pass an immutable argument, the object reference is
# passed to the function parameters and they cannot be changed in a
# function call, as they cannot be changed at all. If a mutable object is passed
# they can be changed in place in the function. If you pass a mutable argument
# function.
#
# Below is example of an immutable object:

x = 4
print(id(x))
def ref_demo(x):

    print("x=",x," id=",id(x))
    x=42
    print("x=",x," id=",id(x))

ref_demo(x=x)

#%%
# Example of a mutable object:
def side_effects(cities):
     print(cities)
     cities += ["Birmingham", "Bradford"]
     print(cities)

locations = ["London", "Leeds", "Glasgow"]
side_effects(locations)
print("Global:", locations)

#%%
# *******************
# List implementation
# *******************
#
# Ref: `blog laurent <http://www.laurentluce.com/posts/python-list-implementation/>`_
#
# As suggested above a list is implemented in CPython with a list of pointers
# to the list elements. When initialising a list memory is allocated for the
# list of pointers. Usually the allocated slots is greater than the list size
# to prevent needing to reallocate memory every time the list is appended to.
#
# * ``append()`` adds a pointer to the end of the list. If we have run out of
#   allocated slots, 'realloc' needs to be called.
# * ``insert()`` is more complex and it involves moving every element after
#   the insertion point, down one. Then a new pointer is added at the correct
#   place.
# * ``pop()`` removes the last element. If the new size is less than half the
#   allocated size, then the list is shrunk.
#
# *********
# Functions
# *********
#
# * When a function encounters a ``return`` statement, it will stop. If it
#   reaches the end of a function without encountering a ``return`` it will
#   return ``None``.
# * Positional ('required') parameters first, then keyword parameters
#
#   * keyword parameters used to specify optional arguments (e.g., ``x=1.5``)
#   * positions parameters still have a keyword, which you can use when
#     calling a function
#
# * Variables created in a function are local to the function and destroyed
#   after the function is finished.
#
# You can return multiple variables:

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
#
# **********
# Write/Read
# **********
#
# Strings are read in or written to from files. This is done with the function
# ``open()`` and the following arguments:
#
# * ``r`` read only
# * ``w`` write only - will write over existing file
# * ``a`` append a file
# * ``r+`` read and write
# * ``b`` binary files
#
# ***************
# Standard libary
# ***************
#
# Useful packages in the standard library:
#
# * ``os`` - using OS dependent functionality
#
#    * ``os.getcwd()``
#    * ``os.listdir``
#    * ``os.mkdir``
#    * ``os.rename`` - rename a dir
#    * ``os.remove`` - delete a file
#    * path name manipulations
#
# * ``glob`` (``*``)
#
#    * glob.glob(``*.txt``) - pattern matching
#
# * ``sys`` - system specific information
#
#    * ``sys.platform``
#    * ``sys.version``
#    * ``sys.argv`` - command line arguments
#
# * ``pickle`` - store arbitrary objects to a file
#
# ******************
# Exception handling
# ******************
#
# Ref: `blog ics <http://tutors.ics.uci.edu/index.php/79-python-resources/104-try-except>`_
#
# Exceptions are raised by errors. There are many different types of
# errors. You can 'catch' an exception with:

try:
    # Code to try, with exception that you wish to catch
    # If an exception is raised, immediately moves to the next block
    print('hello')
except: # catches ALL exceptions
    # code to execute if an exception occurs
    pass

#%%
# You can specify the exact type of exception and then continue the control
# flow defining what to do if various types of exceptions are raised:

try:
    print('hello')
except TypeError:
    pass
except FileNotFoundError:
    pass

#%%
# The difference between ``except:`` and ``except Exception`` is that the
# former catches ALL exceptions whereas the latter only catches exceptions
# that inherit from the 'Exception' class. This means that ``KeyboardInterrupt``
# and ``SystemExit`` would not be caught (ref: `Quora
# <https://www.quora.com/Is-there-any-difference-between-except-and-except-Exception-in-Python>`_).
#
# There is actually more to this control flow:
try:
    print('hello')
except ZeroDivisionError:
    pass
else:
    # only executed if there are NO exceptions raised
    pass
finally:
    # this code is ALWAYS executed, regardless of if there was an exception
    pass

#%%
# ******************
# Naming conventions
# ******************
#
# Ref: `blog dbader <https://dbader.org/blog/meaning-of-underscores-in-python>`_
#
# * Single leading ``_`` means that the variable or method is for internal
#   use only.
#
#   * This affects how ``from my_module import *`` works. Python will not
#     import names with a leading ``_``.
#
# * Dunder (double underscore) e.g.: ``__name__`` is reserved for special use
#   in the language. Often referred to as *magic methods*. These are not
#   mangled (see below).
# * By convention ``_`` is used to indicate a variable that is temporary or
#   insignificant.
# * Trailing underscore ``name_`` - this is used when the most appropriate
#   name is already taken, thus a ``_`` is added to the end to avoid naming
#   conflict.
#
# ************
# repr vs str
# ************
#
# Ref: `blog dbader2 <https://dbader.org/blog/python-repr-vs-str>`_,
# `blog journaldev <https://www.journaldev.com/22460/python-str-repr-functions>`_
#
# The ``__str__()`` method returns the string representation of the object.
# It's goal is readability. It is called when ``str()`` is invoked on an object.
#
# The ``__repr__()`` method returns the object representation. It's goal is
# unambiguity. It is called when ``repr()`` is invoked on an object. This
# object representation can be evaluated with ``eval()`` to recreate the
# object itself.
#
# * If ``__str__()`` is missing, ``__repr__()`` is used as a fallback. There is
#   no fallback if ``__repr__()`` is missing.
# * ``__str__()`` must return a string object whereas ``__repr__()`` can
#   return any Python expression.
# * If ``repr()`` is called on an object and ``__repr__()`` is not return a
#   string, an error will be thrown.
#
# When you define a custom class (with no ``__repr__()`` or ``__str__()``
# methods), create an object of this class (``o``) and
# then try to print the object (``print(o)``), it will call upon the 'default'
# to string conversion. This will be a string containing the class name and ID
# of the object instance.
#
# Defining a the ``__repr__()`` and ``__str__()`` methods however, will allow
# you to better control the how objects are converted to strings in different
# situations.
#
# * ``print()`` will use the ``__str__()`` method
# * ``{}.format()`` will use the ``__str__()`` method
# * ``eval()`` (or just running the variable in IPython) will use
#   ``__repr__()``
# * containers (e.g. dict and list) will always use the result of
#   ``__repr__()`` to represent the objects they contain. Even if you call
#   ``str()`` on it. e.g. ``str([o])`` will return ``'[__repr__for car]'``
