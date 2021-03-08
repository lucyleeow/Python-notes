PEP8
####

W605
====

Ref: `pycodestyle <https://github.com/PyCQA/pycodestyle/issues/766>`_,
`SO <https://stackoverflow.com/questions/19030952/pep8-warning-on-regex-string-in-python-eclipse>`_

For regular expressions, add ``r`` (raw string) at the start. 'Invalid escape
sequence' means something like ``\w``, which does not have a special meaning
outside of a regex. ``\t`` for example does, as it means tab. Python previously
has expanded this to the literal backslash and the following character but
this will become a syntax error in the future. You either need to add ``r``
(``r'\w'``) or escape the backslash ``'\\w'``.

Error warning is: ``W605 invalid escape sequence '\w'``
