"""
#######
Classes
#######
"""
# %%
# *******
# Classes
# *******
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
# * ``hasattr()`` - check if an attribute exists or not
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

# %%
# Type and class
# ==============
#
# Ref: `py course <https://www.python-course.eu/classes_and_type.php>`_,
# `realpython <https://realpython.com/python-metaclasses/>`_
#
# ``type()`` can be used in two different ways. Passing an object to type
# ``type(object)`` returns the class which the object is an instance of:

x = []
type(x)

# %%
# If you check the ``type()`` of a class object, you can see that the class
# ``type`` is returned:

type(type(x))

# %%
# This is because all class objects are instances of the class ``type``. This
# is because everything is an object in Python. Classes are objects as well
# and thus must have a type. The type of x is a list, the type of the class
# list is 'type'. The type of 'type' is also type! Type is a 'metaclass'
# and classes are instances of type.
#
# Additionally, ``type()`` can be used to create a type object (class object)
# when you give it 3 arguments:
# ``type(classname, superclasses, attributes_dict)``:
#
# * ``classname`` - name of the class as string
# * ``superclasses`` - list or tuple of the superclasses of your class
# * ``attributes_dict`` - dictonary that contains the definitions for the
#   class body and becomes the ``__dict__`` attribute.

A = type("A", (), {})
# is the same as
class A(object):
    pass

# %%
# Prior to Python 2.2 type and class were different. Types were built-in
# objects and classes were user-defined using a ``class`` statement. These
# could not be mixed, a user-defined class could not extend a built-in type.
# The old style class does not inherit from a built-in type.
#
# The instance of an old style class is 'instance' whereas ``__class__`` of the
# instance gives the class. Thus instances of old style classes are of a
# different type than their class. This is because old style classes are
# implemented with a single built-in type (instance). This type looks at the
# instances ``__dict__`` and only if it is not present looks up the class
# hierarchy. Old style classes have simpler method resolution order,
# are still instances of object. More about the
# implementaton in `nextthought
# <https://dev.nextthought.com/blog/2018/07/python-2-new-vs-old-classes.html>`_.
# For new style classes the ``type()`` and ``__class__`` of an instance is the
# same.

# %%
# Object and type
# ---------------
#
# Ref `SO <https://stackoverflow.com/questions/22921093/query-on-object-class-type-class-in-python>`_
#
# Everything in Python is an object, an instance of some class - including
# class **objects**. Everything
# is an instance of the class 'object'. Thus type class is an instance of
# object. However, every class is an instance of type. Thus the object class is
# an instance of the class type. This gives circular hierarchy.

print(isinstance(type,object))
print(isinstance(object,type))

# %%
# This kind of mutual inheritance is not normally possible but it is the way
# for these fundamental classes in Python.
#
# Built-in or user defined classes are instances of type but are subclasses
# of object.
# %%
# Mixin
# =====
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