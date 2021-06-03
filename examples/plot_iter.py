"""
#######################
Iterators and iterables
#######################
"""
# %%
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
# .. image:: ../_static/iterable-vs-iterator.png
#
# *********
# Generator
# *********
#
# Ref: `Real Python Gen <https://realpython.com/introduction-to-python-generators/>`_
#
# Returns a lazy iterator (lazy = evaluation delayed until its value is
# needed), which you can loop over. Due to lazy evaluation, it does not
# store contents in memory, generates when needed.
#
# Commonly used to work with large data streams. Example::

#   def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         yield row
#
# Using `return` in the above function would only give you the first line of
# the csv file. Generators look and act like function, the `yield` indicates
# sending a value back to the caller but unlike `return` you do not
# exit the function after this. The **state** of the function is remembered.
#
# You can even make an infinite sequence. This works because of lazy eval.

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
# %%
# You can use your generator in a for loop or run `next` on it. (We don't
# want to run the for loop)::
#
#   for i in infinite_sequence():
#       print(i, end=" ")
#

gen = infinite_sequence()
next(gen)

# %%
# A generator is an iterator. When `next` is called on it, the code within the
# function is executed until the `yield` and function execution is suspended
# (c.f. in function after `return` function execution stopped completely).
# State of function save, including any variable bindings local to generator,
# instruction pointer, internal stack and any exception handling. This way all
# evaluation picks back up, starting from after the `yield`.
#
# Generators can iterate through ONCE only and can be exhausted (unless yours
# is infinite). Once all values evaluated, iteration will stop - the for loop
# will exit, or if you are using `next` on your generator, you will get a
# `StopIteration` exception. This is a natural exception that is raised to
# signal the end of an iterator.
#
# You can even use multiple `yield`s in on generator. Each iteration will stop
# at one of the `yield`s.
#
# yield from
# ==========
#
# Ref: `blog simeonvisse <http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html>`_
#
# Added in python 3.3. Enables you to refactor a generator by splitting into
# multiple generators.
#
# The generator below yields the numbers 0 to 19.

def generator():
    for i in range(10):
        yield i
    for j in range(10, 20):
        yield j

# %%
# Let's say we want to break this up into 2 generators, so that we can reuse
# them elsewhere. We could do this:

def generator2():
    for i in range(10):
        yield i

def generator3():
    for j in range(10, 20):
        yield j

def generator():
    for i in generator2():
        yield i
    for j in generator3():
        yield j

# %%
# The syntax for iterating over `generator2` and `generator3` seems
# unnecessary (and a bit redundant). Using `yield from` we can rewrite as:

def generator():
    yield from generator2()
    yield from generator3()

# %%
# We could have also used `chain` from `itertools`:

from itertools import chain

def generator():
    for v in chain(generator2(), generator3()):
        yield v

# %%
# It's arguable that `yield from` is cleaner and does not require importing a
# function.
#
# Generator expressions
# =====================
#
# Also called 'generator comprehension'. Another way to create a generator.
# Act like list comprehension, allowing
# you to quickly create a generator. Syntax:

nums_squared_gc = (num**2 for num in range(5))
nums_squared_gc

# %%
# Uses parentheses and creates a geneator expression. `yield` is assumed at
# the end of each inner iteration. Compare with list
# comprehensions:

nums_squared_lc = [num**2 for num in range(5)]
nums_squared_lc

# %%
# With the list, you build and hold the entire object in memory but with
# generator, there is no memory penalty. However, list comprehensions can
# be faster to evaluate than correspondig generator expression.-