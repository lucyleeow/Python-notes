# -*- coding: utf-8 -*-
"""
##########
Containers
##########

* **Lists** ordered, can have different types, mutable

  * ``[-1]`` negative indexing = count from the back
  * ``[start:stop:step]`` slicing syntax, 'stop' not inclusive
  * ``list1 = list(list2)`` creates a new object that is in a different
    memory area
  * multiplying a list with a scalar concatenates the list 'scaler' times
  * ``+`` will concatenated lists via making new list and copying the objects
    over. ``extend()`` adds several elements to the end of a list and is less
    expensive.
  * ``sort()`` sorts in place

* **Set** unordered collection of unique elements. Like dictionary without
  keys. Create with ``set() or ``{}``.

  * support mathematical operations like union, intersection and difference-
* **Strings** immutable, accessible via indexing just like lists

  * string formatting:
"""

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

# %%
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
