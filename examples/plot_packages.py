"""
########
Packages
########
"""
# %%
# *******************
# Scripts and modules
# *******************
#
# A python script (``.py`` text file) can be executed interactively with
# ``%run <file name>`` in IPython or ``execfile`` in plain Python
# interpreter. It can also be run in a terimal with ``python <file name>``.
# Scripts can also take command line arguments. Use: ``import sys`` then
# ``sys.argv``.
#
# Each python script file can contain one or more python functions or classes.
# A module is just a Python script, the name of that module is the
# name of the script. It is a way to organise Python code in a
# hierarchichal way. It is also better way to organise functions that you wish
# to use in several other scripts.
#
# You can ``import`` a module, which gives access to all objects in that
# module (script). This allows it to be used in a script or interactive
# instance of the interpreter. Definitions from a module can be imported into
# other modules or the main module.
#
# * **Definitions**: variables and functions you have assigned in python.
# * **Script**: using a text editor to prepare input for the interpreter.
# * **Module**: a python script.
#
# Modules can be defined in 3 ways:
#
# * written in Python
# * written in C and loaded dynamically at runtime (e.g.: regular expression
#   module `re`)
# * built-in module intrinsically included in interpreter
#
# All accessed the same way, with `import`.
#
# Modules are cached, such that if you modify the module script and import the
# module again in the same script, you will get the old one. One solution is
# to use ``reload(<module>)``.
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
# What importing does:
#
# 1. Search for the package/module. There is an ordered list of paths where
#    python will look for these.
#
#   * The interpreter searches for a built-in module with that name. This is
#     installation dependent and can be found in `sys.builtin_module_names`
#   * If not found, it will look for a file named <name>.py for a folder
#     called <name> - in an ordered list of paths. This list of paths can be
#     found with `import sys; sys.path` and is initialised using the
#     following:
#
#       * directory from which the script was run, or cwd if interpreter
#         run interactively
#       * `PYTHONPATH` (list of directory names with the same syntax as the
#         shell PATH)
#       * Installation-dependent default (controlled by `site.py` see: `SO
#         <https://stackoverflow.com/questions/25715039/python-interplay-between-lib-site-packages-site-py-and-lib-site-py>`_)
#
#   * Note that the directory containing the script being run is put after
#     built-in, order is as follows:
#     (built-in > current working directory > standard library paths > ?)
#   * After initialisation, Python programs can modify `sys.path`
#
# 2. Bind and load the package.
#
#   * Binding puts all the functions and classes in that package in your
#     namespace (so python knows that they exist) and also put a link to the
#     code for each function and class.
#   * Loading the package means that it runs the code in the script.
#
# **Package** - run all of the code in the package’s `__init__.py` file if it
# exists.
#
# **Module** - runs all of the code in the module file and the `__init__.py`
# file of the package it belongs to, if it exists.
#
# The `<module>.__file__` attribute will tell you where the module file was found.
# Once a module is imported, you can explore the contents with `dir()`.
# Only objects declared in the imported package’s `__init__.py` are accessible
# to the importer.
# `import package` does not place it’s modules in the local namespace, i.e.
# following with `package.module` will return you attribute not found error.
#
# Pycache
# =======
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
# Importing a package also puts a ‘pycache’ file in the package you imported.
# There will basically be a compiled version of your package in this file -
# this means that if your __init__ file says to load a certain module (.py)
# file, a compiled version of that file will be in the pycache file. It will
# be a .pyc file. You have permission to delete the cache after you have
# imported your package - the functions from that package are still
# available because they have already been imported and the scripts
# already loaded!
#
# When importing in a new python session, python will check to see if
# the latest update of the source code and the .pyc file are in sync. If
# the source code has been edited, the code will be compiled again.
#
# Each module has its own private symbol table which is used as the global
# symbol table by all functions defined in the module. Thus, the author of a
# module can use global variables in the module without worrying about
# accidental clashes with a user’s global variables.
#
# Top down and bottom up
# ======================
#
# If you import the top package (and the `__init__` file does not say to
# import the sub package), any subpackages will not be imported.
# E.g., in the init file you have `import mod1`, then you can do
#  `import package` then use `package.mod1.fun()`.
# Also any modules (.py files) will not be imported (if it does not specify
# it in the `__init__` file).
#
# If you import a function from a subpackage, the top package and all
# sub package will all be imported.
#
# __main__
# ========
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
# ========
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
# ********
# Packages
# ********
#
# References: `Chris Yeh <https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html>`_,
# `ASPP github <https://github.com/aspp-apac/2019-data-tidying-and-visualisation>`_,
# `realpython <https://realpython.com/pypi-publish-python-package/>`_,
# `common problems <https://jwodder.github.io/kbits/posts/pypkg-mistakes/#top-level-tests-directory-in-wheel>`_
#
# Package is a directory containing many modules (collection of scripts). A
# special file named '__init__.py' tells python that the directory is a package
# from which modules can be imported. From python 3.2 onwards, the
# '__init__.py' file is actually required anymore.
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
# (Note the ``.`` before the module name is required as of Python 3 since it
# is more strict) With the above import in the ``__init__.py`` file, we can use
# the following in your code::
#
#   import PackageName
#
#   PackageName.FunctionName()
#
# See `<bramlett
# https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html>`_
# for more details.
#
# Anatomy of package
# ==================
#
# This is what a package folder looks like:
#
# * A `__init__.py` file tells python that this folder is a package (before
#   python 3.3). When a file is imported this is the file that gets executed.
#   Often here you will specify modules (.py files) to load or subpackages to
#   load.
#
#   * This file contains package initialisation code
#   * Variables defined here become available in package namespace
#     (e.g., `packagename.var`)
#   * as a module is only loaded once per interpreted session, executable
#     statements are only run the first time a module is imported
#   * Special variable `__version__` used by convention
#     (`<package>.__version__` will return version)
#
# * `.py` files contain the functions or classes etc
# * `__main__.py` - acts as entry point to package. When running package as
#   `python -m <package>`, it runs this file.
#
#   * The `-m` flag allows you to specify a module name (instead of a file
#     name, e.g., `hello` instead of `hello.py`)
#
# * A `setup.py` file - you don’t need this if you are just using the package locally
# * Can use package to automatically get version from git tag:
#   `setuptools_scm <https://pypi.org/project/setuptools-scm/>`_
#
# Main
# ----
#
# Ref: `SO main <https://stackoverflow.com/questions/419163/what-does-if-name-main-do>`_
#
# Often see::
#
#   if __name__ == "__main__":
#       main()
#
# When python interpreter reads a source file it:
#
# * sets a few special variables e.g., `__name__`. E.g.,
#   `python foo.py` will assign `__name__` to string “__main__`.
#   If another module is the main, and your module is imported by it,
#   `__name__` will be the name of your module, thus it executes all of the
#   code in the file.
#
# *********
# Packaging
# *********
#
# disutils vs setuptools
# ======================
#
# * disutils is part of the python standard library
#
#   * limited feature set
#   * infrequently updated
#
# * setuptools is 3rd party, built on top of disutils
#   * many opinionated features
#   * can make wheels
#
# setuptools preferred over disutils but disutils used in a number of popular
# legacy programs.
#
# Dependency management
# =====================
#
# Ref: `realpython <https://realpython.com/pipenv-guide/>`_
#
# Specifying versions:
#
# `requirements.txt` file allows you to pin package version.
# However, the pinned package itself has dependencies - and the package may
# not specify exact versions for some of its dependencies.
# This means the install is not deterministic - given the same requirements
# file, the same env is not always produced.
# You can use `pip freeze` to specify exact version of all packages and their
# sub-dependencies this comes with problem of you needing to manually update
# versions (e.g., due to security updates in a package)
#
# Dependencies resolution:
#
# E.g., requirements are:
# a
# b
# a has dependency c>=1.0 and b also has dependency c<=2.0
#
# The way pip would handle this is:
#
# 1. install a and look for c that satisfies c>=1.0
# 2. install b - if the version of c installed above does not satisfy b’s
#    requirements, the installation will fail
#
# The solution is to add c and the range i.e. c>=1.0,<=2.0 to the requirements
# file. But this means you need to deal with sub-dependencies.
#
# setup.py
# ========
#
# Ref: `py docs <https://docs.python.org/2/distutils/introduction.html#distutils-simple-example>`_,
# `setuptools doc <https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html>`_ (lists options),
# `SO setup <https://stackoverflow.com/questions/58533084/what-keyword-arguments-does-setuptools-setup-accept>`_(describes options),
# `guide <https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires>`_
#
# Required when you are using `setuptools` as your build/distribution system.
# `setup.py` tells setuptools about your package as well as files to include.
#
# Required parameters for pypi:
#
# * `name` - as long as you want, can contain `_` and `-`
# * `version`
# * `packages` (list of packages and subpackages)
#
#   * tells disutils to process all pure Python modules found in each package
#     listed
#   * default filename correspondence is that package ‘abc’ is found within
#     folder ‘abc’, which is in the (distribution) root dir
#
# Optional:
#
# * `author` and `author_email`
# * `description` - one sentence
# * `long_description` - commonly loaded from README.md
# * `long_description_content_type` - text markup used for long description,
#   e.g., Markdown
# * `url`
# * `classifiers` - gives the index and pip metadata, e.g., licence, which
#   versions of Python the package is compatible with
# * `install_requires` - list any dependencies
# * `entry_points` - create scripts that call a function within your package
# * `scripts` - files containing Python source intended to be started from the
#   command line
#
# Example::
#
#   from setuptools import setup
#
#   setup(
#       name='pyexample',
#       version='0.1.0',
#       description='A example Python package',
#       url='https://github.com/shuds13/pyexample',
#       author='Stephen Hudson',
#       author_email='shudson@anl.gov',
#       license='BSD 2-clause',
#       packages=['pyexample'],
#       install_requires=['mpi4py>=2.0', 'numpy', ],
#       classifiers=[
#           'Development Status :: 1 - Planning',
#           'Intended Audience :: Science/Research',
#           'License :: OSI Approved :: BSD License',
#           'Operating System :: POSIX :: Linux',
#           'Programming Language :: Python :: 2',
#         ],
#     )
#
# setup.py vs setup.cfg
# =====================
#
# Ref: `SO cfg <https://stackoverflow.com/questions/39484863/whats-the-difference-between-setup-py-and-setup-cfg-in-python-projects>`_,
# `disutils docs <https://docs.python.org/3/distutils/configfile.html>`_,
# `setuptools docs <https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html>`_
#
# `setup.py` can contain code but some consider it bad style - thus the use
# of `setup.cfg` file, which is purely declarative (describe desired results,
# no commands). Advantage is python only needs to parse config file. You would
# only include dummy setup file::
#
#   from setuptools import setup
#
#   if __name__ == "__main__":
#       setup()
#
# `setuptools’ only allows use of `setup.cfg` from version 30.3.0 onwards.
#
# * `setup.cfg` middle ground between `setup.py` (opaque to users) and command
#   line to the setup script (outside control of package writer control and
#   completely up to user)
# * processed after contents of `setup.py` but before command-line
# * user can override `setup.py` settings by editing `setup.cfg`
# * non-standard defaults can be provided for options not easily set in
#   `setup.py`
# * user can override anything in `setup.cfg` with command line options
# * users can edit `setup.cfg` file - esp if user specific info req
# * you can provide default values, these are over-rideable on command line
#   (when performing `python setup.py`
#
# Example `setup.cfg file <https://gist.github.com/althonos/6914b896789d3f2078d1e6237642c35c>`_
#
# Source distribution & wheel
# ===========================
#
# Ref: `realpython <https://realpython.com/python-wheels/>`_
# `realpython2 <https://realpython.com/pypi-publish-python-package/#building-your-package>`_
#
# Source distribution
# -------------------
#
# Contains source code (incl. any extension e.g., C) and any supporting files.
# With source distribution, extensions are compiled on user’s side and not
# developers. Metadata in dir `<package_name>.egg.info` helps with building
# and installing package.
# Created with `python setup.py sdist`
#
# What happens when you install from source distribution:
#
# 1. Download compressed tar file (‘tar.gz’) - this is a source distribution
#    (see below)
# 2. Build wheel (‘whl’) file using tarball, via call to setup.py
# 3. Label wheel
# 4. Install package using wheel
#
# Note that pip will prefer wheel (if available and compatible with your
# system), over source distribution.
#
# Wheels
# ------
#
# Type of built distribution, contains source code and any extensions ready to
# use.
#
# built = ready-to-install format, avoid build stage. Only need to be moved to
# correct location to be installed (Python files do not need to be
# pre-compiled).
#
# * Faster installation
# * Typically smaller in size cf source dist (can be downloaded faster)
# * Installing from wheel avoids intermediate step of building packages using
#   the source distribution
# * No need for compiler to install packages that contain compiled extension
#   modules
# * Provide consistency - cuts many variables involved in installation out
# * Name tells you what Python versions and platforms it is compatible with
# * Essentially a `.zip` archive
#
# .egg files
# ==========
#
# Bundles additional info along with a python project that allows the projects
# dependencies to be checked at runtime. Also allows projects to provide
# #plugins for other projects.
#
#
# conda packaging
# ===============
#
# Ref: `condadoc1 <https://conda.io/projects/conda/en/latest/user-guide/concepts/packages.html>`_,
# `conda forge <https://conda-forge.org/docs/maintainer/adding_pkgs.html#test>`_
#
# Conda package is a compressed tarball file (`.tar.bz2`) or `.conda` file.
# It contains the module to be installed and info about how to install it,
# specifically:
#
# * system-level libraries
# * python or other modules
# * executable programs
# * metadata under `info/` dir - dependencies, list of where files go when it
#   is installed
# * collection of files that are installed directly into an `install` prefix
#
# * Only files are included, no directories
# * `.conda` file format introduced in conda 4.7 as more compact and faster
#   alternative to tarball
# * ‘Noarch’ packages - not architecture specific, only have to be built once
#
#   * can be generic (e.g., datasets, docs, source code) or (pure) Python
#   * pure python has no compiled extensions, OS-specific build-scripts, python
#     version specific requirements (just Python and shell scripts)
#   * Declare in `meta.yml` file to reduce shared CI resources
#
# * `conda-build` used to build the conda package
#
# Channels
# --------
#
# * contain packages
# * conform to standard structure and contain index of avail packages
# * conda can install from channels
# * default is ‘.condarc’
# * installing locally built conda package: SO
#
# Recipe
# ------
#
# Building conda package requires recipe. Conda-build recipe is a flat dir that
# contains:
#
# * `meta.yml` - contains metadata. Only package name and package version are
#   required
# * `build.sh` - installs files for the package, for Linux and MacOS
# * `bld.bat` - installs files for the package for Windows
# * `run_test.[py,pl,sh,bat]` - optional test file, test script that runs
#   automatically if it is part of the recipe
# * other files can include patches, icon files, readme files (these cannot be
#   generated by the build scripts)
#
# `conda skeleton` generates the first 3 files for you.
#
# conda-build
# -----------
#
# Ref: `condadoc <https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html>`_
#
# 1. Reads metadata, `meta.yml` - template filled in using conda-build config,
#    which states what packages and versions to build
# 2. Downloads source into cache
# 3. Extracts source into source dir
# 4. Applies any patches
# 5. Re-evaluates metadata, if source is req to fill any metadata values
# 6. Creates build env and installs the build (and run?) dependencies there
# 7. Runs build script - any installs go into the build env, cwd is source dir
# 8. Post processing steps e.g., shebang and rpath
# 9. Creates conda package containing all the files along with req conda
#    package metadata
# 10. Tests the new conda package if the recipe includes tests - creates new
#     env and builds the package
#
# Build variants
# --------------
#
# Ref: `conda docs <https://docs.conda.io/projects/conda-build/en/latest/resources/variants.html>`_
#
# May need to build package for multiple combinations of dependencies or
# platforms. E.g., Python 2 and 3.
# Some binary packages need to be built with several variants to support users’
# environment.
# A build that needs to be done for variants can be defined in
# `conda_build_config.yaml` (this should live in your recipe dir). The vars
# defined here are available in the `meta.yaml` file as jinja variables::
#
#   python:
#       - 2.7
#       - 3.5
#
# In the `meta.yaml`, a part that refers to `python` will be expanded out to 2
# build definitions::
#
#   package:
#       name: compiled-code
#       version: 1.0
#
#   requirements:
#       build:
#           - python {{ python }}
#       run:
#           - python
#
# means that the package is built for both versions of Python.
#
#
# ************
# Installation
# ************
#
# You can use a local file without ‘installing’, if you are in the same folder
# as the package. For all other situations (non local and local but not in the
# same folder), you need to install the package first.
#
# Installation requires a setup.py file. This is similar to the DESCRIPTION
# file in R. It gives details like the licence, name of package, version, and
# importantly package dependencies.
#
# If you download a package and use pip install, installation would copy the
# files to where all the python packages are stored. Note that this location
# would be in your python path. If you `pip install` in editable format
# (with `-e`), the source code will not be copied to where the other python
# packages are stored, the path to your source code will be added to the
# python PATH.
#
# The installation part can also be done with
# `python <setup.py> install/develop` (this does not require pip to be
# installed). Give this function a path to a setup.py file and it will install
# the package. However, it will not (ref: `SO
# <https://docs.google.com/document/d/1A-KwoQ7FN20q2ktLaPQvLkqEbrqqiqpU90nsnyfGEZw/edit#>`_):
#
# * check the required dependencies
# * keep track of metadata so you can easily uninstall or update
# * automatically download and extract the files
#
# install vs develop
# ==================
#
# `python <setup.py> install/develop`
#
# * install - copies code to `site-packages`, this means that if you change
#   the code you will need to install again
#
#   * equivalent to `pip install`
#
# * develop - creates link to source code, a special `.egg-link` file in
# `site-packages`
#
#   * equivalent to `pip install -e`
#
# This is where `pip` and `conda` come in. They will run
# `python setup.py install` under the hood, but will also:
#
# `pip install`
#
# * Can install local file
# * Can install from github, even specify a commit or branch
# * Check all the dependency requirements and install anything you do not have
# * You an install with -e, which means editable install. This is for if
#   you want to develop the package.
#
# `python -m pip`
#
# Ref: `blog snarky <https://snarky.ca/why-you-should-use-python-m-pip/>`_
#
# Executes `pip` with the python interpreter specified e.g., you could do
# `python3 -m pip` or `/usr/bin/python3.7 -m pip`
# Just using `pip` means that if you have >1 python interpreter, you are
# not sure which interpreter you are installing for.
# Note: Usually to run python script you use `python <script.py>`. Using
# `-m` enables you to run a module as a script (looks up module as if you
# were importing it and runs it like a script) - syntax is
# `python -m <module_name>` - note that you do not give a file extension.
# Technically - it ‘search sys.path for the named module and execute its
# contents as the __main__ module’ see: `doc
# <https://docs.python.org/3/using/cmdline.html#cmdoption-m>`_.
# If your module is one .py file, it will execute it, if it is a dir, it will
# look for `__main___.py` and run that.
#
# `conda install`
#
# * Cannot install from local file
# * Will check all the dependencies and update any that are not the latest
# version, as well as install ones you do not have
#
# You can get problems if you install the same package with pip and conda.
# `conda install <packagename>` will look in the default channel (this is just
# a server online) for the package. You can also specify a specific channel to
# look in (instead of the default channel, which is called default).
# `conda` aims to do more than pip by handling library dependencies outside
# of Python packages.
# Conda creates a virtual environment (ref: `SO
# <https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda>`_)
#
# Installation from github
# ========================
#
# Installation from Github can be done via a number of download protocols, see
# `here <https://pip.pypa.io/en/stable/reference/pip_install/#git>`_.
# Options include ``pip install <git+git://git.example.com/MyProject>``
# (start with `git+` then use the https clone url but replace the https at
# the start with `git`), ```pip install <https://git.example.com/MyProject>``.
#
# Instead of using git you can also use a 'zipball', with
# ``pip install <https://git.example.com/MyProject/zipball/master>``. This is
# the clone https url, without ``.git`` at the end and with ``zipball/master``
# added to the end.
# See `SO hugo <https://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github>`_-.
#
# Conda vs pip
# ============
#
# .. table::
#    :widths: 50, 50
#
#   +-------------------------------------------------+---------------------------------------------------------+
#   |                      Conda                      |                           Pip                           |
#   +-------------------------------------------------+---------------------------------------------------------+
#   | Installs conda packages from Anaconda repo      | Installs from Python Package Index (PyPI).              |
#   | and Anaconda Cloud.                             |                                                         |
#   +-------------------------------------------------+---------------------------------------------------------+
#   | Packages are binaries - never need compiler.    | Wheel (binary format) or source - can require compiler. |
#   +-------------------------------------------------+---------------------------------------------------------+
#   | Not limited to Python (can include C++, R etc). | Only Python.                                            |
#   +-------------------------------------------------+---------------------------------------------------------+
#   | Can create isolated environments.               | Depends on other tools like venv and                    |
#   |                                                 | virtualenv to create environments.                      |                |
#   +-------------------------------------------------+---------------------------------------------------------+
#   | Over 1,500 packages available.                  | Over 150,000 packages available.                        |
#   +-------------------------------------------------+---------------------------------------------------------+
#
# pip Deals with dependencies in recursive, serial
# loop - does not check if dependencies of ALL packages have been met.
# Packages installed earlier may have incompatible dependency versions
# relative to packages installed later.
#
# conda environments
# ------------------
#
# When creating a new environment, it will not include any packages - it will
# NOT inherit from your base environment (ref).
# `conda environments` will list all available environments and put a ``*``
# next to the active one.
# It will point to base even when no environment is active.
#
# Activating a conda environment tells your shell to use a specific python
# interpreter. When you deactivate all conda environments, your shell generally
# reverts back to the python interpreter determined by $PATH. Use
# `which conda` and `which pip` to determine which interpreter and where
# packages are stored.
