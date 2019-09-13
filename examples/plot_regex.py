# -*- coding: utf-8 -*-
"""
Regular expressions
###################

Regular expressions with the ``re`` module. Good resource for testing your
regex is `regex101 <https://regex101.com/>`_ and `pythex 
<https://pythex.org/>`_.
"""

#%%
# The backslash
# =============
# 
# The backslash is used as an escape or to invoke a special form on 2 different
# levels - at Python and ``re``. The Python interpreter performs substitutions
# first (e.g. ``\n`` becomes a newline) before ``re`` sees your string.
# To get an actual ``\`` you need ``\\``. To see how Python is exanding your
# strings simply ``print()`` the string (ref: `SO
# <https://stackoverflow.com/questions/24085680/why-do-backslashes-appear-twice>`_):

s = 'a\\b\tc\q'
print(s)

#%%
# Notice how the first ``\`` escapes the special character ``\``. ``\t`` is
# interpreted as a 'tab'. The final ``\`` is not followed be a special
# character so appears as just ``\`` but doing this is not recommended. Indeed
# the representation of a string (created by ``__repr()__``):

s='slash\s'
s

#%%
# Thus if you need a literal ``\`` in your regex, you need to ``\\`` because
# the regular expression is ``\\`` (to escape the special meaning in ``re``)
# but inside a regular Python string literal 
