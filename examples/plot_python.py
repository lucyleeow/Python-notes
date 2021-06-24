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
#
# *******
# Logging
# *******
#
# * ``logging`` part of standard library
#   * Note uses camelCase for historic reasons, when it was decided to add to
#     the standard library was already adopted and changing to meet PEP8 would
#     have broken backwards compatibility.
#
# The 4 standard levels, increasing in severity:
#
# 1. DEBUG
# 2. INFO
# 3. WARNING
# 4. ERROR
# 5. CRITICAL
#
# The default logger is called 'root'. By default only logs at DEBUG or higher
# level are logged.
#
# ``basicConfig`` can be used to set:
#
# * ``level`` - lowest level to log
# * ``filename`` - file, if you want to log to file instead of console
# * ``filemode`` - mode to open ``filename``, if 'w', new logs will overwritte
#   old
# * ``format`` - format of the log, e.g. '%(asctime)s - %(message)s'
#
# This function can only be called once. The logging functions (``debug`` to
# ``critical``) call ``basicConfig`` without arguments if it has not been
# called before. This means you cannot call ``basicConfig``.
#
# Capturing stack traces
# ======================
#
# Stack traces can be captured too::
#
#    try:
#       c = a / b
#   except Exception as e:
#       logging.error("Exception occurred", exc_info=True)
#
# another way to do this is to use the ``logging.exception`` function. It
# logs at error level and always gives the exception information.
#
#   try:
#       c = a / b
#   except Exception as e:
#       logging.exception("Exception occurred")
#
# Logging classes
# ===============
#
# The default logger is 'root', but you can and should define your own logger
# by creating an object of the ``Logger`` class. ``logging.getLogger(name)``
# instantiates an object of the ``Logger`` class. Calling it several times
# with the same name will return a reference to the same object. This saves
# us from passing the logger object around to different parts that need it.-