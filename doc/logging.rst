#######
Logging
#######

ref: `real python <https://realpython.com/python-logging/>`_

The logging module is in the Python standard library and used by most
third-party Python libraries, enabling easy integration of your log messages
with that of those libraries.

5 standard levels, in order of increasing severity:

1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

The logging module has a default logger named 'root'. This is used when logging
functions are used directly e.g., ``logging.debug()``. It has a default output
format and logs levels ``WARNING`` or above. To configure the root logger you
can use ``basicConfig(**kwargs)``:

* ``level`` - what level to log
* ``filename``
* ``filemode`` - mode to open file, 'a' for append
* ``format`` - format of the log message

Note ``basicConfig()`` can only be called once - it can only configure the
root logger if the root logger has *not* been configured before. The logging
functions ``debug()`` ... ``critical()`` call ``basicConfig`` without arguments
automatically *if* it has not been called before. Thus after any of the
above functions has been called, you can no longer configure the root logger.

**********
Formatting
**********

There are some basic elements that are already a part of the ``LogRecord``
and can be easily added to output format:

* ``process`` - process id
* ``levelname``
* ``asctime`` - time of creation of the ``LogRecord``. Change format with e.g.:
  ``datefmt='%d-%b-%y %H:%M:%S'``

Entire list of attributes can be found `here
<https://docs.python.org/3/library/logging.html#logrecord-attributes>`_.

*********
Exception
*********

To get the full stack trace set ``exc_info=True`` (works at any level) and log
functions like this::

    try:
    c = a / b
    except Exception as e:
    logging.error("Exception occurred", exc_info=True)

Using ``logging.exception("Exception occurred")`` also produces the same
result as `` logging.error("Exception occurred", exc_info=True)``.

*******
Classes
*******

Commonly used classes in the logging module:

* ``Logger`` - you can create your own logger (like the root logger) by
  creating ab object of this class. Multiple calls to ``getLogger(<name>)``
  with the same name will return a reference to the same ``Logger`` object.
  This saves you from passing ``Logger`` objects to different scripts.
  These objects will be used to call the functions. e.g.:

.. code-block:: Python

  import logging

  logger = logging.getLogger('example_logger')
  logger.warning('This is a warning')

* ``LogRecord`` -  ``Loggers`` automatically create ``LogRecord`` objects,
  which have all the information related to the event being logged.
* ``Handler`` - send the ``LogRecord`` to the required output destination, like
  console, file or over HTTP. It is a base class for subclasses like
  ``StreamHandler``, ``FileHandler``, ``HTTPHandler`` etc.
* ``Formatter`` - specify format of the log message.

To configure custom loggers, use ``Handlers`` and ``Formatters`` (unlike
with root logger where you can use ``basicConfig``).

It is recommended that module level loggers are created using
``name=__name__`` (``__name__`` is a built-in variable that evaluates to the
name of the current module). This way the name of the logger informs us where the
logs are coming from.

********
Handlers
********

You can have more than one handler for a logger, allowing you to output
log messages e.g., to console and to a file. You can also set severity level
for handlers, such that different destinations record different logs.

.. code-block:: Python

  import logging

  # Create a custom logger
  logger = logging.getLogger(__name__)

  # Create handlers
  # StreamHandler outputs to console
  c_handler = logging.StreamHandler()
  # FileHandler outputs to files
  f_handler = logging.FileHandler('file.log')
  c_handler.setLevel(logging.WARNING)
  f_handler.setLevel(logging.ERROR)

  # Create formatters and add it to handlers
  c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
  f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  c_handler.setFormatter(c_format)
  f_handler.setFormatter(f_format)

  # Add handlers to the logger
  logger.addHandler(c_handler)
  logger.addHandler(f_handler)

  logger.warning('This is a warning')

When ``logger.warning()`` is run, it creates a ``LogRecord`` that holds all
the information of the event and passes to all the ``Handlers`` it has:
``c_handler`` and ``f_handler``.

You can also configure logging by creating a config file and loading it using
``fileConfig()`` or a dictionary and loading with ``dictConfig()``.
