# -*- coding: utf-8 -*-
"""
Python
#######

Python is an interpreted language (c.f. compiled) and can be used
interactively.

References used: SciPy lecture notes, Python for Data Science.
"""

#%%
# Magic functions
# ******************
# These functions are prefixed by ``%``. In certain IDE's the setting
# ``automagic`` is
# enabled by default and allows you to omit the ``%`` sign. Useful magic
# functions include ``timeit``, which times the execution of short snippets
# using the timeit module from the standard library and ``debug``, which allows
# you to enter post-mortem debugging.
#
# Data types
# ************
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
# Containers
# **********
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
# This is often used in a ``for`` loop:

for a, b, c in t:
    print(a)
    print(b)
    print(c)

#%%
# The ``*rest`` syntax to select only the start of a tuple. ``rest`` will be a
# list:

t = 1,2,3,4
a, b, *rest = t
rest

#%%
# You can also use this to return multiple values from a function.
#
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
#
# Dictionary
# ==========
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

#%%
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

#
# Mutable vs immutable
# **********************
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
# (`ref <https://www.python-course.eu/python3_passing_arguments.php>`_).
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
# List implementation
# *******************
#
# Ref: `blog <http://www.laurentluce.com/posts/python-list-implementation/>`_
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
# Iterators and iterables
# ***********************
#
# Ref: `nvie <https://nvie.com/posts/iterators-vs-generators/>`_
#
# Containers (e.g., list, set, dict, tuple, str) are:
#
# * Data structures.
# * Support membership tests - ask whether it contains a certain element
# * Typically hold all values in memory
# * Not all containers are iterable
#
# Iterables (e.g., lists, generators, files, tuples, dicts, str)
#
# * Essentially means it can be looped over
# * Technically - requires the dunder method ``__iter__()`` and can return
#   an ``iterator``
#
# Iterator
#
# * Helper object that will produce the next value when you call `next()`
# * It knows how to compute the next value because it holds an internal state.
#   Every call to next() changes the state and produces a result.
#
# What is occuring when you are using a for loop is this:
#
# .. image:: images/iterable-vs-iterator.png
#
# Functions
# *********
#
# * When a function encounters a ``return`` statement, it will stop. If it
#   reaches the end of a function without encountering a ``return`` it will
#    return ``None``.
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
# Scripts and modules
# ******************
#
# A python script (``.py`` text file) can be executed interactively with
# ``%run <file name>`` in IPython or ``execfile`` in plain Python
# interpreter. It can also be run in a terimal with ``python <file name>``.
# Scripts can also take command line arguments. Use: ``import sys`` then
# ``sys.argv``.
#
# Modules are a way to organise Python code in a hierarchichal way. It is also
# better way to organise functions that you wish to use in several other
# scripts. A module is
# just a Python script. You can ``import`` a module, which gives access to all
# objects in that module (script). Modules are chached, such that if you
# modify the module script and import the module again in the same script, you
# will get the old one. One solution is to use ``reload(<module>)``.
#
# How importing works:
#
# Ref: `effbot <http://effbot.org/zone/import-confusion.htm>`_,
# `SO mouad <https://stackoverflow.com/questions/6351805/cyclic-module-dependencies-and-relative-imports-in-python>`_
# `SO mouad2 <https://stackoverflow.com/questions/12330891/python-cyclic-imports-fail-when-using-from-package-import-module-syntax>`_
#
# * ``import <x>`` imports the module and creates a reference to that module
#   in the current namespace (i.e., you can use ``x.fun()`` now).
# * ``from <x> import *`` imports the module and creates references in the
#   current namespace to all public objects defined in that module.
# * ``from <x> import <y>`` imports the module and creates references in
#   current namespace to y. y could be a variable in a module x OR a module in
#   package x. Under the hood it is ``IMPORT_NAME x`` (same as
#   ``import x``) then ``IMPORT_FROM y``. This is uses the function
#   ``import_from`` which will try to get the attribute ``y`` from the module
#   ``x``.
# * ``import x.y`` as above except that y can only be a module. The difference
#   is important because in this case, the contents of ``sys.modules`` is
#   enough to to get y, whereas if y is a variable (which is possible in the
#   case above) the interpreter must look into the contents of x (i.e. with
#   ``getattr()``.
#
# When Python imports a module, it checks the module registery ``sys.modules``
# to see if the
# module was already imported. If it was, Python uses the existing object
# from cache. The module registery is a table of modules that have in
# initialised and indexed by module name.
# If it was not registered, Python:
#
# 1. Creates a new empty module object
# 2. Insert that object in the ``sys.modules`` dictionary
# 3. Load the module code object (convert to ``.pyc`` compiled bytecode)
# 4. Execute the module code in the new modules namespace. All variables
#    assigned will be available via the module object.
#
# If you run a module as a script (e.g., ``python <file name> rather than
# importing it) it is loaded under the module name ``__main__``. There is
# another difference, is that no ``.pyc`` file will be created, like with
# importing.
#
# __main__
# ==========
#
# Ref: `CSchafer <https://www.youtube.com/watch?v=sugvnHA7ElY>`_
#
# Whenever Python runs a file, it sets a number of special variables.
# ``__name__`` is one of them. When it runs a ``.py`` file directly,
# ``__name__`` variable is set to '__main__'. When importing a module
# however, the ``__name__`` variable is set to the name of the file (without
# the extension). When you see the script ``if __name__ == '__main__'``,
# it is specifying that the code below the if statement should only be run
# if the script is being run directly (and NOT if it is being imported).
#
# sys.path
# =========
#
# Python looks for modules to import in a number of directories dictated by
# the list of directories in the ``sys.path`` variable. This list consists of
# installation dependent default paths as well as directories specified by the
# environment variable ``PYTHONPATH``.
#
# Circular dependencies
# =====================
#
# Ref: `stackabuse <https://stackabuse.com/python-circular-imports/>`_,
#
# Can cause problems with code reusability, difficulty maintaining code and
# can cause infinite recursion and memory leaks.
#
# For example::
#
#   # module1
#   import module2
#
#   def function1():
#     module2.function2()
#
#   def function3():
#     print('Goodbye, World!')
#
#   # module2
#   import module1
#
#   def function2():
#     print('Hello, World!')
#     module1.function3()
#
# In the example above here are the steps:
#
# 1. We import module 1. The first thing that module 1 does is to import
#    module 2.
# 2. module 2, is loaded and executed. But function 2 requires the use of
#    module 1, function3!
#
# The problems are generally due to design. To fix:
#
# * merge both modules into a single module
# * defer the import of the a module to when it is needed
#
# Another example::
#
#   # main.py
#   from pkg import foo
#
#   # pkg/foo.py
#   from pkg import bar
#   # pkg/bar.py
#   from pkg import foo
#
# This will cause the error::
#
#   Traceback (most recent call last):
#       File "/path/to/main.py", line 1, in <module>
#           from pkg import foo
#       File "/path/to/pkg/foo.py", line 1, in <module>
#           from pkg import bar
#       File "/path/to/pkg/bar.py", line 1, in <module>
#           from pkg import foo
#   ImportError: cannot import name foo
#
# What is happening is this:
#
# 1. In ``main.py`` we start with ``from pkg import foo`` so ``pkg.foo``
#    is added to ``sys.modules``.
# 2. In ``foo.py`` we execute ``from pkg import bar``. ``pkg.bar`` is added
#    to ``sys.modules``. Then we starting importing bar.
# 3. To import ``bar.py`` we must run ``from pkg import foo``. We check if
#    there is a ``pkg.foo`` in ``sys.modules``. There is as we did this in 1.
#    Thus, we skip this and get straight to ``getattr(pkg, 'foo')`` - but
#    we are still in the middle of importing ``pkg.foo`` so there is no
#    attribute called ``foo`` so we get the error above.
#
# Change ``bar.py`` to ``import pkg.foo`` actually fixes this error because
# this will not perform the ``getattr()`` function. It uses
# ``sys.modules[foo]`` instead. From above, this is because you can only
# use this syntax to import module from package, you cannot import variable
# from module this way. Thus ``getattr()`` is not used, just
# ``sys.module[foo]``.
#
# Aside, ``import bar`` also does not perform ``getattr()``. Thus you can
# ``import bar`` from ``foo`` and ``import foo`` from ``bar`` because ``import``
# in this instance does not require the *other* module to be already imported
# before *it* can be imported.
#
# Packages
# ========
#
# Package is a directory containing many modules. A special file named
# '__init__.py' tells python that the directory is a package from which
# modules can be imported. From python 3.2 onwards, the '__init__.py' file is
# actually required anymore.
#
# The purpose of a package is to group modules (``.py`` files) together. The
# main benefit is that you can use relative imports to import from other
# modules from the same package (e.g., ``from . import mod``). The other
# benefit is not needing to add the module path to ``sys.path`` if you
# are importing a module from a different directory (ref: `SO-Bren
# <https://stackoverflow.com/questions/32152373/python-why-can-i-import-modules-without-init-py-at-all>`_).
#
# Note that you 'import' modules not pacakges! When you import a package, all
# you are doing is importing the ``__init__.py`` file. If your ``__init__.py``
# file is empty, you will need to import modules like this::
#
#   import PackageName.ModuleFileName
#
#   PackageName.ModuleFileName.FunctionName()
#
# However, if, in your ``__init__.py`` file, you import modules like this::
#
#   from .ModuleFileName import FunctionName
#
# Note the ``.`` before the module name is required as of Python 3 since it
# is more strict. With the above in the ``__init__.py`` file we can use the
# following in your code::
#
#   import PackageName
#
#   PackageName.FunctionName()
#
# See `<bramlett
# https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html>`_
# for more details.
#
# Write/Read
# *************
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
# Standard libary
# ****************
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
# Exception handling
# ********************
#
# Ref: `blog <http://tutors.ics.uci.edu/index.php/79-python-resources/104-try-except>`_
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
# Naming conventions
# ******************
#
# Ref: `blog <https://dbader.org/blog/meaning-of-underscores-in-python>`_
#
# * Single leading ``_`` means that the variable or method is for internal
#   use only.
#
#   * This affects how ``from my_module import *`` works. Python will not
#     import names with a leanding ``_``.
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
# Classes
# ********
#
# * A class is a blueprint for creating instances. Instance variables are
#   created using a class blueprint and contains data specific for that
#   instance.
#
#   * An 'object' is an unique instance of a class.
#
# * 'Data attribute' - data associated with class. This can be either specific
#   to the class (class variable) or specific to an instance (instance
#   variable). E.g., the class vehicles may have a data attribute
#   'can move = True', which is the same for all instances of this classes and
#   each instance may also have it's own data attributes like 'speed'.
# * 'Method' - function associated with class. E.g., the method ``len()`` will
#   work for strings and lists.
#
# These data and method attributes can be accessed via dot notation. -
#
# Generally, both can be referred to as an 'attribute'.
#
# The `__init__` method can be thought of as 'initialise'. It is a reserved
# method in Python classes and is known as a 'constructor' in object oriented
# world. This method is called when an instance is created from the class
# (in fact it is called as soon as memory for the object is allocated)
# and allows the class to 'initialise' the attributes. These are inherited
# to the methods inside the class. This means that other functions defined in
# the class have access to these initalised attributes.
#
# All functions defined in a class must have the 'self' parameter first. This
# parameter can actually be called anything, but you should follow convention
# and use 'self'. It refers to the current instance of the class. If you do not
# include self, variables are created locally. Self, stores it to the
# instance/class.

class Employee:

    def __init__(self, first, last):
        self.fname = first
        self.sname = last

    def method1(self, param1):
        print(param1, self.fname)

#%%
# To create an instance. You must provide all the arguments of the first
# '__init__' method.
emp1 = Employee('alice','smith')

#%%
# access the attributes:
print(emp1.fname)
print(emp1.sname)

#%%
# use the method:
emp1.method1('hello')

#%%
# Useful functions to investigate the attributes of a class:
#
# * ``getattr()`` - access the attribute of the object
# * ``hasattr() - check if an attribute exists or not
# * ``setattr()`` - set an attribute. If it does not exist at all, it would be
#   created.
# * ``delattr()`` - delete an attribute.
#
# ``dir()`` will also list all the attributes of of an object.
#
# Inheritance
# ===========
#
# Ref: `realpython <https://realpython.com/python-super/>`_
#
# Transfer of the characteristics of a class to other classes that are derived
# from it. You can override the methods of the base class or can keep the
# methods. They are created at runtime, and can be modified further after
# creation. Classes that inheret from a base class are called derived classes,
# subclasses or subtypes. A subclass is said to derive, inherit or extend
# a base class.
#
# The advantage of inheritance is to save you from re-writing the similar code.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

#%%
# The above code is repititive. And it does not reflect that square is a
# special case of rectangle. Instead you can write:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

#%%
# Because the ``__init__()`` methods are so similar, the ``__init__()`` of
# ``Square``` can just call the ``__init__()`` of ``Rectangle``.
#
# The ``super()`` function gives you access to methods in a 'superclass' from
# the subclass that inherits from it. ``super()`` alone returns a temporary
# object of the superclass that then allows you to call that superclass's
# methods. This allows you to build classes that extend the functionality of
# previously built classes. Calling the previously built methods saves your
# from re-writing those methods.

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

#%%
# The ``Cube`` class extended the functionality of ``Square`` by using
# ``area()`` to calculate the face area in ``Cube``. Above, ``super()`` returns
# a delegate object to a parent class (in this case ``Square``), so you
# can all the method ``.area()`` directly on it. Further ``Cube`` does not have
# an ``__init__()`` because ``Square`` already has an ``__init__()`` that
# would work fine for ``Cube``.
#
# ``super()`` takes 2 parameters, subclass and an object that is an instance
# of that subclass.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

#%%
# In Python 3, ``super(Square, self)`` is the same as ``super()``. Here the
# ``Square`` object is ``self``.

class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

#%%
# In the above case, ``Square`` is the subclass. This means that super will
# search for the method ``area()`` one level above ``Square``, which is
# ``Rectangle``.
#
# If you also provide an instance of the class in the second parameter,
# ``super()`` will return a bound object - a method that is bound to an object
# giving the method the objects context, such as any attributes of that
# instance.
# If the second parameter is not included, the method returned is just a
# function unassociated with an objects context.
#
# In more complicated situations you may be using multiple inheritance,
# where you inherit from >1 superclass.

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

#%%
# The ``RightPyramid`` inherits from both ``Triange`` and ``Square``. Both of
# these super classes define an ``area()``. Method resolution order (MSO) tells
# Python how to search for inherited methods. Every class has a ``__mro__``
# that shows the order. This is the main advantage of ``super``.

RightPyramid.__mro__

#%%
# The methods that will be searched first will be ``RightPyramid`` then
# ``Triange`` and so on. You can change the order when defining ``RightPyramid``
# to change this MRO.

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

RightPyramid.__mro__

#%%
# Minxin
# ======
#
# A mixin is a class that provides methods to other classes but are not
# considered a base class. The mixin allows you to implement a method to other
# unrelated classes. It does this without becoming a super class.
#
# For example, let's say you want to be able to convert certain objects to
# a dictionary representation of the object. This would be implemented
# similarly for many different classes.
#
# The difference between a mixin and normal inheritance is that the mixin is
# rarely used as a standalone object. It is designed to be 'mixed in' with
# other classes. It is just a specific application of
# multiple inheritance and can be thought of as a special case of
# inheritance.
#
# Name mangling
# =============
#
# Ref: `SO <https://stackoverflow.com/questions/44114560/how-to-access-double-underscore-variables-in-methods-added-to-a-class>`_
#
# This happens when the attributes in a class are compiled. An attribute name
# like ``__foo`` gets turned into ``_ClassName__foo``. This is to prevent
# accidental internal attribute access in subclasses (which inherit from a
# base class).

class class1:
    def __init__(self):
        self.__attr = 1 # private

class class2(class1):
    def __init__(self):
        self.__attr = 'string' # name is a coincidence

#%%
# In ``class2``, there is an attempt to 'overwrite' ``__attr``. Without name
# mangling, the accidental reuse of the same name in ``class2`` would result
# in the attribute being overwritten, which may break ``class1``. But because
# of name mangling, this does not happen and ``class1`` has an attribute
# called ``_class1__attr`` and ``class2`` has an attribute called
# ``_class2__attr``.
#
# The main reason for name mangling is to prevent code not defined in your
# class from accessing your attributes.
#
# repr vs str
# ************
#
# Ref: `blog <https://dbader.org/blog/python-repr-vs-str>`_,
# `blog2 <https://www.journaldev.com/22460/python-str-repr-functions>`_
#
# The ``__str__()`` method returns the string representation of the object.
# It's goal is readability. It is called when ``str()`` is invoked on an object.
#
# The ``__repr__()`` method returns the object representation. It's goal is
# unambiguity. It is called when ``repr()`` is invoked on an object. This
# object representation can be evaluated with ``eval()`` to recreate the
# object itself.
#
# * If ``__str()`` is missing, ``__repr__()`` is used as a fallback. There is
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
#
# eval vs exec
# *************
#
# Ref: `SO <https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile/29456463#29456463>`_
#
# ``eval()`` evaluates a single dynamically generated Python expression.
#
# ``exec()`` executes dynamically generated Python code only for its side
# effects.
#
# * ``eval()`` excepts only a single expression. Anything to the RHS of a
#   variable assignment.
# * ``exec()`` excepts all Python code (e.g. includes statements like ``for``
#   ``if``, ``while``, ``class`` and ``def``). Note that:
#   ``if``-``elif``-``else`` chain, ``try``-``except``-``else``-``finally``
#   chain are considered a single statement.
#
# * ``eval()`` returns the value of the expression.
# * ``exec()`` ignores the output and always returns ``None``.
#
# Data directed to standard output e.g. ``print()``, is output.

exec('for i in range(3): print(i)')

#%%
# ``exec()`` and ``eval()`` accepts the code in the form of ``str``,
# ``unicode`` or ``bytes`` object containing source code, or as compiled
# ``bytecode``.
#
# Both ``exec()`` and ``eval()`` accept 2 positional arguments, ``globals``
# and ``locals`` (global and local variable scopes). These default to the
# ``globals()`` and ``locals()`` within the scope that called ``exec()`` or
# ``eval()`` but you can also provide a dictionary for ``globals()`` and any
# mapping object (map hash table values (keys) to objects (or data value),
# dictionary being the only standard mapping type in Python) for ``locals()``.

a=2
eval('print(a)')

#%%
# Compile
# =======
#
# Ref: `journaldev <https://www.journaldev.com/22772/python-compile-function>`_
#
# ``compile()`` is a lower level function that does not evaluate or execute
# your code but returns a code object or AST module object.
#
# It can be used to speed up repeated invocations of the same code with
# ``exec()`` or ``eval()`` by compiling to a code object beforehand. It is
# also used in metaprogramming (where computer programs have the ability to
# treat other programs as their data) -
#
# It takes 3 non-optional arguments:
#
# * ``source`` - the source code as sting, byte string or AST module object.
# * ``filename`` - filename from which the code was read, as string. It is not
#   used to in compiling but to improve code readability. If not
#   read from file, pass some value (``'<string>'`` is often used).
# * ``mode`` - either ``exec``, ``eval`` or ``string``, see below.
#
#
# ``compile()`` in ``eval()`` mode compiles a *single* expression into bytecode
# that returns the value of the expression.
#
# ``compile()`` in ``exec()`` mode compiles any number of statements into
# bytecode, that implicitely always returns ``None``.

eval(compile('42', '<string>', 'exec'))  # code returns None
eval(compile('42', '<string>', 'eval'))  # code returns 42
exec(compile('42', '<string>', 'eval')) # returns 42 but ignored by exec

#%%
# There is a 3rd mode, 'single`. It accepts source code containing a single
# statement (or multiple statements separated by `;`). If the last statement
# is an expression, the resulting compile bytecode also prints the `__repr__`
# of the value to standard output. Mostly used for interactive Python shells.
#
# ``compile()`` can also compile source code to ``ast`` (see below).
# Technically ``eval()`` accepts a single expression only when a string is
# passed.
# If more than a single expression passed in string form, an exception is
# raised.
#
# If a bytecode object is passed, ``eval()`` can accept more than just a single
# expression. Notice below that you must first use ``exec()`` to compile as
# it is a string. The output is ``None`` because the code object returned
# from ``compile()`` returns ``None``.

eval(compile('a=2', '<string>', 'exec'))

#%%
# Trees
# =====
#
# Ref: `ruslanspivak <https://ruslanspivak.com/lsbasi-part7/>`_,
# `basecs <https://medium.com/basecs/grammatically-rooting-oneself-with-parse-trees-ec9daeda7dad>`_
# `basecs2 <https://medium.com/basecs/leveling-up-ones-parsing-game-with-asts-d7a6fc2400ff>`_-
#
# * data structure composed of 1 or more nodes, connected by edges
# * has 1 root, the top node
# * all nodes have a parent except the root node
# * a node with no children is called a leaf node
# * a node with 1 or more children and is not the root node, is called an
#   interior node
# * an interior node can be a 'complete subtree'
# * children - set of nodes with incoming edges from the same node are the
#   children of that node
# * parent - a node is the parent of all nodes it connects to with outgoing
#   edges
# * level - number of edges on the path from the root node
# * height - larges level of any node in the tree
#
# Parse tree
# ----------
#
# Also known as, concrete syntax tree, a parse is a tree that represents the
# syntatic structure of a language structure according to the grammar
# definition. It can be used to represent a language sentence, mathematical
# expression or code.
#
# To build a parse tree the first step is to break the expression into a list
# of tokens. Tokens or terminals are symbols that cannot be broken down any
# further. They help us understand how parts of an expression relate to one
# another and the syntactic relationships between individual elements. Examples
# in Python code include ``+``, ``-``, ``if``, ``else``. They also include
# factor values like string or number. These always end up being leaves in the
# tree. Non-terminals are expressions and terms which can potentially be broken
# down further.
#
# The job of the *parser* is to take some input and build a parse tree. This
# parse tree can be built by following a set of rules. For example, in a maths
# expression, whenever we see a parenthesis we know that we are starting a new
# expression and should create a new expression. Importantly, the grammar must
# not be ambiguous. In other words, one 'expression' should only lead to one
# parse tree.
#
# .. _image:: https://ruslanspivak.com/lsbasi-part7/lsbasi_part7_parsetree_01.png
#
# Take a look at the difference between a parse tree and an abstract syntax
# tree (AST):
#
# .. _image:: https://ruslanspivak.com/lsbasi-part7/lsbasi_part7_ast_01.png
#
# ASTs uses operators/operations as root and interior nodes while operands
# are children. ASTs do not represent every detail, e.g., no parentheses.
# Interior nodes are not used to represent grammar. Instead grammar, e.g.,
# operator precendence, is shown by it's level on the tree. Perform operations
# starting from the lowest node. AST shows us the 'important bits' or the
# abstracted syntax of the code 'sentence'.
#
# Technically - you can see that some interior nodes only have one child. These
# are called single-successor nodes. It tells us that the token is a factor
# or a term, but we are more interested in what the factor or term is. In the
# above case picture, compressing the single-successor nodes is all we have
# to do to get from the parse tree to the AST. In other cases we may need to
# do. For example, parentheses may be expressed like this:
#
# .. image:: images/ast_paren.jpeg
#   :width: 700
#
# This structure is mirrored. The parentheses do not do much once we have our
# tree structure. The tree can be compressed by removing the top mirror, the
# parentheses subtree.
#
# The differences include:
#
# * AST will not contain syntactic details like parentheses and commas
# * operators such as ``+`` will be internal nodes and not leaves
#
# The parser may or may not generate a parse tree, it may go straight to AST,
# depending on the compiler. Building AST is actually very difficult which is
# why some parsers decide to build a parse tree first.-
#
# AST
# ----
#
# Ref: `Blog <https://www.mattlayman.com/blog/2018/decipher-python-ast/>`_
#
# Your parser is performing these tasks:
#
# 1. Parse code into list of pieces (tokens). Different things are different
#    types of tokens e.g. the numeric ``42`` is different from ``if``.
# 2. Raw list of tokens transformed to build an AST. This is a collection of
#    nodes joined together by edges based on the grammar of the Python
#    language.
# 3. From the AST, the interpreter can project a lower level of instructions
#    called bytecode. These instructions are things like ``BINARY_ADD`` and
#    are meant to be very generic so a computer can run them.
# 4. The interpreter can run your code with the bytecode, which is used to call
#    functions in your OS.
#
# Bytecode is very low level and it is difficult to gain much understanding
# about what you wrote. AST contains enough structured information within them
# to make them useful for learning about your code.
#
# Each node in an AST contains some data (a token and its value) and pointers:
#
# .. image:: https://miro.medium.com/max/2035/1*NO_p9739sX6Tf-ESRkSKaw.jpeg
#
# For example here is the AST of a simple equation:
#
# .. image:: https://miro.medium.com/max/1920/1*T0Zo8ZLDDm0m0fSmmkj7wA.jpeg
#
# Following the first child node/next sibling node points gives this:
#
# .. image:: https://miro.medium.com/max/1901/1*0n73V3Ld0e-nTmZKGw3OpQ.jpeg
#
# You can think of the AST as the 'final project' of the front-end of the
# compiler (technically 'intermediate code representation').
#
# Used for modifying source code and dynamic code creation, as it is often
# easier to deal with tree of nodes rather than lines of text.
#
# For more see `blog <https://medium.com/basecs/leveling-up-ones-parsing-game-with-asts-d7a6fc2400ff>`_
# and `AST explorer <https://astexplorer.net/>`_ to interactively explore
# AST of any code you input.
#
# In Python, AST treats the entire code source you give it as a 'module'. The
# body of the module consists of all the statements inside the module.

import ast

# to parse code
code_ast = ast.parse('a=2\na\nfor i in range(2):\n    print(i)', mode = 'exec')
# explore
ast.dump(code_ast)
# body is a list of statements
code_ast.body
# get the last one like so:
code_ast.body[-1]

#%%
# Each 'node' in the body can be of class ``Expr`` (expression) technically
# expression-statement (statement consisting of only one Expression) or class
# statement ``stmt``:

for i in range(3):
    print("Is statement")
    print(isinstance(code_ast.body[i], ast.stmt))
    print("Is expression")
    print(isinstance(code_ast.body[i], ast.Expr))

#%%
# The value of a node can be obtained as well:

code_ast.body[0].value

#%%
# It seems that you can create an expression using the value of an expression
# but not the expression itself:

a=2
ast.Expression(code_ast.body[1].value)
eval(compile(ast.Expression(code_ast.body[1].value), '<string>', 'eval'))
# this will not work:
# eval(compile(ast.Expression(code_ast.body[1]), '<string>', 'eval'))

#%%
# You can also create a new assignment using the value of an expression:

ast.Module(body=[
    ast.Assign(targets=[ast.Name(id='name_of_var', ctx=ast.Store())],
    value=code_ast.body[1].value)
])

#%%
# Of interest, note that variable we are assigning to has ``ctx=ast.Store()``
# whereas when looking at the ``ast.dump()`` of an expression which is just
# one variable, ``ctx=ast.Load()``.
#
# References:
#
# For more useful guides to using ``ast`` see `blog
# <http://stuartmyles.blogspot.com/2016/09/an-ast-hello-world-getting-started-with.html>`_
#
# JakeVP uses this `SO <https://stackoverflow.com/questions/39379331/python-exec-a-code-block-and-eval-the-last-line>`_
# logic to exec and eval the last line. Note that the last body is ``popped()``
# so that it is not run twice. A different solution in this
# `SO <https://stackoverflow.com/questions/33908794/get-value-of-last-expression-in-exec-call>`_
#
# `Green tree snakes <https://astexplorer.net/>`_ provides comprehensive
# (though difficult to understand) guide on the functions and methods of
# ast.
#
# `Blog <https://tobiaskohn.ch/index.php/2018/07/30/transformations-in-python/>`_
# goes through ast in Python well.
