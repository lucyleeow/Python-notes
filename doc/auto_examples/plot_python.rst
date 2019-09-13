.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_auto_examples_plot_python.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_examples_plot_python.py:


Python
#######

Python is an interpreted language (c.f. compiled) and can be used 
interactively.

Magic functions
******************
These functions are prefixed by ``%``. In certain IDE's the setting 
``automagic`` is
enabled by default and allows you to omit the ``%`` sign. Useful magic 
functions include ``timeit``, which times the execution of short snippets
using the timeit module from the standard library and ``debug``, which allows
you to enter post-mortem debugging. 

Data types
************

* numeric

   * Integer
   * Float
   * Complex
   * Boolean 

Type conversion is called 'casting'.

Containers
**************
* **Lists** ordered, can have different types, mutable

  * ``[-1]`` negative indexing = count from the back
  * ``[start:stop:step]`` slicing syntax
  * ``list1 = list(list2)`` creates a new object that is in a different 
    memory area

* **Strings** immutable, accessible via indexing just like lists

  * string formatting:


.. code-block:: default


    print(
        'An integer: %i; a float: %f; another string: %s' % (1, 0.1, 'string')
    )





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    An integer: 1; a float: 0.100000; another string: string



* **Dictionary** unordered, maps keys to values
* **Tuple** immutable list. 


.. code-block:: default


    t = 1, 2, 3, 'string' 
    t = (1, 2, 3, 'string') # both ways to create tuple







Mutable vs immutable
**********************

**Immutable**: string, tuple, int, float, boolean
Cannot be altered in place.

**Mutable**: list, dictionary, set
Can be altered in place.

You can think of a variable as a name 'bound' to an object. One object
can have several 'names'. You can check this with the ``id()`` function
which returns the memory location of where the variable is stored.
You can also check if two objects have the same ID by using the ``is`` 
function. If two 'variables' are point to the same object, changing one 
variable, changes the other variable pointint to that object.

Creating two strings with the same value will result in the two variables
pointing to the same object. This is to economise memory usable as these
objects are immutable.


.. code-block:: default


    string1 = "hello"
    string2 = "hello"
    print(id(string1))
    print(id(string2))





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    139842330542576
    139842330542576



Strings cannot be changed in place. Altering one of these strings results
in Python creating a new string object at a different location in memory.


.. code-block:: default


    string1 += "e"
    print(id(string1))





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    139842330645232



Integers will appear to act the same way but this is for a different reason.
To economise memory usage, CPython pre-allocates the first 262 integers on
start up. This means that the numbers -5 to 256 (inclusive) are automatically
bound to certain addresses in memory. CPython stores references to all of 
these integer objects in an array. When we 'create' an integer object, we 
are just telling our variable to point to an address stored in that array.
These numbers are choosen as they are the most commonly used numbers. 
For some reason this does not seem to work with sphinx?


.. code-block:: default


    num1 = 1
    num2 = 1
    print(num1 is num2)

    num3 = 1e1000
    num4 = 1e1000
    print(num3 is num4)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    True
    True



A list is an array of pointers, which point to each element in the list. The
values in the list are not stored in continuous place in memory.


.. code-block:: default


    list1 = [1,2,3]
    print(id(list1))
    print(id(list1[0]), id(list1[1]), id(list1[2]))





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    139842330570656
    94790694064928 94790694064960 94790694064992



When you change a list, the location of the list (array of pointers)
does not change but the id of the values changes.


.. code-block:: default

    list1[0] = -1
    print(id(list1))
    print(id(list1[0]), id(list1[1]), id(list1[2]))





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    139842330570656
    94790694064864 94790694064960 94790694064992



This influences when a variable is modified inside a function. There are two
ways that arguments (given when calling a function) from a function are 
passed to the parameters (which exist inside functions) of the function
(`ref <https://www.python-course.eu/python3_passing_arguments.php>`_). 

* **call/pass by value** - the argument expression (e.g. ``x=2``) is 
  evaluated. If the expression is a variable (e.g. ``x=var1``) its value will 
  assigned (copied) to the corresponding parameter. This ensures that the 
  'global' variable will not be changed.
* **call/pass by reference** - the function gets a reference to the argument,
  rather than a copy of its value. The function can then modify the variable.
  This saves computation time and memory space as arguments do not need to be
  copied but variables can be 'mistakenly' changed in a function call.

Python uses a mechanism known as 'call by object' or 'call by object
reference'. If you pass an immutable argument, the object reference is 
passed to the function parameters and they cannot be changed in a 
function call, as they cannot be changed at all. If a mutable object is passed
they can be changed in place in the function. If you pass a mutable argument 
function.

Below is example of an immutable object:


.. code-block:: default

 
    x = 4
    print(id(x))
    def ref_demo(x):
    
        print("x=",x," id=",id(x))
        x=42
        print("x=",x," id=",id(x))

    ref_demo(x=x)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    94790694065024
    x= 4  id= 94790694065024
    x= 42  id= 94790694066240



Example of a mutable object:


.. code-block:: default

    def side_effects(cities):
         print(cities)
         cities += ["Birmingham", "Bradford"]
         print(cities)

    locations = ["London", "Leeds", "Glasgow"]
    side_effects(locations)
    print("Global:", locations)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ['London', 'Leeds', 'Glasgow']
    ['London', 'Leeds', 'Glasgow', 'Birmingham', 'Bradford']
    Global: ['London', 'Leeds', 'Glasgow', 'Birmingham', 'Bradford']



Functions
***********

When defining a function with a variable number of parameters you can use:
``*args`` (any number of positional arguments packed into a tuple) and
``**kwargs`` (any number of key word arguments packed into a dictionary).

Functions are objects meaning that they can:

* be assigned to a variable
* an element in a list, or any data structure
* passed as an argument to another function

Methods are functions attached to objects. 

Scripts and modules
******************

A python script (``.py`` text file) can be executed interactively with 
``%run <file name>`` in IPython or ``execfile`` in plain Python 
interpreter. It can also be run in a terimal with ``python <file name>``. 
Scripts can also take command line arguments. Use: ``import sys`` then 
``sys.argv``. 

Modules are a way to organise Python code in a hierarchichal way. It is also 
better way to organise functions that you wish to use in several other
scripts. A module is
just a Python script. You can ``import`` a module, which gives access to all
objects in that module (script). Modules are chached, such that if you
modify the module script and import the module again in the same script, you
will get the old one. One solution is to use ``reload(<module>)``. 

__main__
==========

Ref: `CSchafer <https://www.youtube.com/watch?v=sugvnHA7ElY>`_

Whenever Python runs a file, it sets a number of special variables. 
``__name__`` is one of them. When it runs a ``.py`` file directly,
``__name__`` variable is set to '__main__'. When importing a module
however, the ``__name__`` variable is set to the name of the file (without
the extension). When you see the script ``if __name__ == '__main__'``,
it is specifying that the code below the if statement should only be run
if the script is being run directly (and NOT if it is being imported).

sys.path
=========

Python looks for modules to import in a number of directories dictated by
the list of directories in the ``sys.path`` variable. This list consists of
installation dependent default paths as well as directories specified by the
environment variable ``PYTHONPATH``. 

Packages
***********

Package is a directory containing many modules. A special file named
'__init__.py' tells python that the directory is a package from which  
modules can be imported.

Write/Read
*************

Strings are read in or written to from files. This is done with the function
``open()`` and the following arguments:

* ``r`` read only
* ``w`` write only - will write over existing file
* ``a`` append a file
* ``r+`` read and write
* ``b`` binary files

Standard libary
******************

Useful packages in the standard library:

* ``os`` - using OS dependent functionality

   * ``os.getcwd()``
   * ``os.listdir``
   * ``os.mkdir``
   * ``os.rename`` - rename a dir
   * ``os.remove`` - delete a file
   * path name manipulations

* ``glob`` (``*``) 

   * glob.glob(``*.txt``) - pattern matching

* ``sys`` - system specific information

   * ``sys.platform``
   * ``sys.version``
   * ``sys.argv`` - command line arguments

* ``pickle`` - store arbitrary objects to a file

Exception handling
********************

Exceptions are raised by errors. There are many different types of
errors. You can catch an exception like so with ``try`` <command> and use
``except`` to specify some actions if a certain type of error appears.

Classes
********

* A class is a blueprint for creating instances. Instance variables are 
  created using a class blueprint and contains data specific for that 
  instance.
* 'Attribute' - data associated with class
* 'Method' - function associated with class

The `__init__` method can be thought of as 'initialise'. It is a reserved
method in Python classes and is known as a 'constructor' in object oriented
world. This method is called when an instance is created from the class
(in fact it is called as soon as memory for the object is allocated)
and allows the class to 'initialise' the attributes. These are inherited
to the methods inside the class. This means that other functions defined in
the class have access to these initalised attributes. 

All functions defined in a class must have the 'self' parameter first. This
parameter can actually be called anything, but you should follow convention 
and use 'self'. It refers to the current instance of the class. 


.. code-block:: default


    class Employee:
    
        def __init__(self, first, last):
            self.fname = first
            self.sname = last
    
        def method1(self, param1):
            print(param1, self.fname)







To create an instance. You must provide all the arguments of the first
'__init__' method.


.. code-block:: default

    emp1 = Employee('alice','smith')







access the attributes:


.. code-block:: default

    print(emp1.fname)
    print(emp1.sname)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    alice
    smith



use the method:


.. code-block:: default

    emp1.method1('hello')




.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    hello alice




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.005 seconds)


.. _sphx_glr_download_auto_examples_plot_python.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: plot_python.py <plot_python.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: plot_python.ipynb <plot_python.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
