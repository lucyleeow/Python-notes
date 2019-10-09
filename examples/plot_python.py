# -*- coding: utf-8 -*-
"""
Python
#######

Python is an interpreted language (c.f. compiled) and can be used 
interactively.
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
# **************
# * **Lists** ordered, can have different types, mutable
#   
#   * ``[-1]`` negative indexing = count from the back
#   * ``[start:stop:step]`` slicing syntax
#   * ``list1 = list(list2)`` creates a new object that is in a different 
#     memory area
# 
# * **Strings** immutable, accessible via indexing just like lists
#
#   * string formatting:

print(
    'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string')
)

#%%
# * **Dictionary** unordered, maps keys to values
# * **Tuple** immutable list. 

t = 1, 2, 3, 'string' 
t = (1, 2, 3, 'string') # both ways to create tuple

#%%  
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
# Functions
# ***********
# 
# When defining a function with a variable number of parameters you can use:
# ``*args`` (any number of positional arguments packed into a tuple) and
# ``**kwargs`` (any number of key word arguments packed into a dictionary).
# 
# Functions are objects meaning that they can:
# 
# * be assigned to a variable
# * an element in a list, or any data structure
# * passed as an argument to another function
# 
# Methods are functions attached to objects. 
#
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
# Packages
# ***********
#
# Package is a directory containing many modules. A special file named
# '__init__.py' tells python that the directory is a package from which  
# modules can be imported.
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
# <https://www.quora.com/Is-there-any-difference-between-except-and-except-Exception-in-Python>`_.
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
# Ref: `blog <https://dbader.org/blog/meaning-of-underscores-in-python>`_-
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
# * 'Data attribute' - data associated with class
# * 'Method' - function associated with class
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
# and use 'self'. It refers to the current instance of the class. 

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
# Ref: `SO <https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile/29456463#29456463>`_,
#
# ``eval()`` evaluates a single dynamically generated Python expression.
#
# ``exec()`` executes dynamically generated Python code only for its side
# effects.
#
# * ``eval()`` excepts only a single expression. Anything to the RHS of a 
#   variable assignment.
# * ``exec()`` excepts all Python code (e.g. includes statements like ``for``
#   ``if``, ``while``, ``class`` and ``def``). Note that
# ``if``-``elif``-``else`` chain, ``try``-``except``-``else``-``finally`` chain
# are considered a single statement.

eval('a=4') # you cannot eval a statement
eval('for i in range(3): print(i)') # nor a loop

#%%
# * ``eval()`` returns the value of the expression.
# * ``exec()`` ignores the output and always returns ``None``.

eval('1+2')
exec('1+2')

#%%
# The side effects are output though, e.g. ``print()``:

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
# ``compile()`` can also compile source code to ``ast`` (see below).  -
#%%
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
# AST
# ====
#
# Ref: `Blog <https://www.mattlayman.com/blog/2018/decipher-python-ast/>`_`,
# `<>`_
#
# Abstract syntax tree. At a high level the Python interpreter is following
# a set of steps to translate your code into machine instructions:
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
# about what you wrote. AST contain enough structured information within them
# to make them useful for learning about your code.
# 
# Each node in an AST contains some data (a token and its value) and pointers:
#
# .. image:: https://miro.medium.com/max/2035/1*NO_p9739sX6Tf-ESRkSKaw.jpeg
#
# For example here is the AST of a simple equation:
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

eval(compile(ast.Expression(code_ast.body[1]), '<string>', 'eval'))

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
# so that it is not run twice. A differnt solution in this
# `SO <https://stackoverflow.com/questions/33908794/get-value-of-last-expression-in-exec-call>`_
#
# `Green tree snakes <https://astexplorer.net/>`_ provides comprehensive
# (though difficult to understand) guide on the functions and methods of
# ast.
# 
# `Blog <https://tobiaskohn.ch/index.php/2018/07/30/transformations-in-python/>`_
# goes through ast in Python well.
