Regular expressions
###################

Regular expressions with the ``re`` module. Good resource for testing your
regex is `regex101 <https://regex101.com/>`_ and `pythex
<https://pythex.org/>`_. Great introductory guide at `Python docs
<https://docs.python.org/3/howto/regex.html>`_.

The backslash
*************

The backslash is used as an escape or to invoke a special form on 2 different
levels - at Python and ``re``. The Python interpreter performs substitutions
first (e.g. ``\n`` becomes a newline) before ``re`` sees your string. RE's
handled as regular strings because Python REs are not part of the core
Python language.

To get an actual ``\`` you need ``\\``. To see how Python is exanding your
strings simply ``print()`` the string (ref: `SO
<https://stackoverflow.com/questions/24085680/why-do-backslashes-appear-twice>`_)::

    s = 'a\\b\tc\q'
    print(s)

Notice how the first ``\`` escapes the special character ``\``. ``\t`` is
interpreted as a 'tab'. The final ``\`` is not followed be a special
character so appears as just ``\`` but doing this is not recommended. Indeed
the representation of a string (created by ``__repr()__``) adds uses ``\\``
to represent a single ``\``::

    s='slash\s'
    s

Thus if you need a literal ``\`` in your regex, you need to ``\\`` because
the regular expression is ``\\`` (to escape the special meaning in ``re``)
but inside a regular Python string literal each ``\`` must be expressed as
``\\`` as we learned above. The solution is to use Pythons raw string
notation for regular expression patterns - prefix with ``r``. Backslashes are
not handled in any special way by Python (i.e. they are note treated
differently). ``r'\n'`` is a 2 character string
``\`` followed by ``n``.

Compiling
*********

After using ``re.compile`` to compile a regular expression, all the functions
available are available as methods of the resulting object. It is recommended
to compile a regular expression (instead of using ``re`` functions) when
you are going to perform a lot of matches using the same pattern. Python
internally compiles regexes when you use them and since Python 2, the
compiled versions of the most recent patterns are cached. Thus compiling
a regular expression technically lets you control when the compilation
takes place in computation process (at the start or during a function call),
using compiled expressions avoids cache lookup and since the size of the
cache is limited, gives more control over what needs to be re-compiled in
certain circumstances (ref: `SO
<https://stackoverflow.com/questions/47268595/when-to-use-re-compile>`_).

Special character meanings
**************************

Literal special characters can be matched by using ``\`` to escape or
using ``[]`` to enclose (except for ``]`` - this needs to be escaped
within a ``[]`` or put the ``]`` as the first character within the ``[]``).

**Groups**

The ASCII equivalent given at the end.

* ``[]`` - specifies set of characters to match

  * list inidividually or use ``-`` to specify range e.g. ``a-c``
  * ``^`` at the start specifies complementing set (everything BUT the
    following characters). ``^`` in any other position does not have special
    meaning.

* ``\d`` - digits ``[0-9]``
* ``\D`` - non-digit ``[^0-9]``
* ``\s`` - any whitespace character ``[ \t\n\r\f\v]``
* ``\S`` - any non-whitespace character ``[^ \t\n\r\f\v]``
* ``\w`` - any alphanumeric character in Unicode database, including ``_``,
  ASCII equivalent: ``[a-zA-Z0-9_]``
* ``\W`` - any non-alphanumeric character, ASCII equivalent: ``[^a-zA-Z0-9_]``

**Repeating**

Refers to the previous character or set (``[]``).

* ``*`` 0 or more times
* ``+`` 1 or more times
* ``?`` 0 or 1 time
* ``{m}`` m times
* ``{m,n}`` m to n repetitions
* ``{,n}`` 0 to n repetitions
* ``{m,}`` m to inifite repetitions

Greediness:

``*`` and ``+`` are greedy. This means it will match as many as possible.
If latter portions do not match, it will back up 1 character, sequentually,
and try with fewer matches. It will back up until it has 0 or 1 matches.
If the end of the RE is still not able to be matched then no match is
returned.

You can use ``?`` following the above characters to make them 'non-greedy'.
This means that it will try to match as little as possible of the RE before
it continues matches the rest of the RE.

**Other**

* ``.`` any character except newline, with ``DOTALL``,`S`` flag includes
  newline.
* ``^`` (Caret) Matches the start of the string, and in ``MULTILINE`` mode
  also matches immediately after each newline.
* ``$`` Matches the end of the string **or** just before the newline at the
  end of the string, and in ``MULTILINE`` mode also matches before a newline.

  * Searching for ``foo.$`` in 'foo1\nfoo2\n' matches ‘foo2’ normally (before
    newline at end of string), but ‘foo1’ in ``MULTILINE``` mode (gives first
    match it finds).
  * Searching for a single ``$`` in 'foo\n' will find two
    (empty) matches: one just before the newline, and one at the end of the
    string.

* ``|`` 'OR'. For ``A|B``, where A and B can be arbitrary REs, matches either
  A or B. An arbitrary number of REs can be separated by the '|' in this way.
  As the target string is scanned, REs separated by '|' are tried from left
  to right. When one pattern completely matches, that branch is accepted.
  This means that once A matches, B will not be tested further, even if it
  would produce a longer overall match - i.e. NOT greedy.
* ``b`` word boundary. Zero-width (does not consume any characters) assertion
  that matches only at the beginning or end of a word (indicated by white
  space). ``\bclass\b`` will only match the word 'class' when it is a
  word by itself, but not when it part of a longer word.

  * note that this is the worst collision between ``re`` and Python's string
    literals. In Python ``\b`` means backspace

* ``\B`` NOT at word boundary. Zero width assertion.
* ``(?(...)yes-pattern|no-pattern)`` try to match with ``yes-pattern``
  if the group RE exists, and with no-pattern if it. ``no-pattern``` is
  optional and can be omitted.

Compilation flags
*****************

Modify how your RE works. Available under a long name or a short one-letter
form.

* ``ASCII`` ``A`` - match only ASCII characters (affects ``\w \W \b \B``)
* ``DOTALL`` ``S`` - make ``.`` match any character, including newline
* ``IGNORECASE`` ``I`` - case-insensitive matches
* ``LOCALE`` ``L`` - makes ``\w \W \b \B`` dependent on locale
* ``MULTILINE`` ``M`` - affecting ``^`` and ``$``, matching at after/before
  newline
* ``VERBOSE`` ``X`` (for ‘extended’) - enable verbose REs, which can be
  organized more cleanly and understandably. Whitespace is ignored unless
  escaped allowing indenting.

Grouping
********

Allow for matching groups within a 'matched string'. Groups are numbered
starting with 0 - group 0 is always present and is the whole RE.

You can refer to a group within a RE using backreferences. ``\1`` will refer
to group 1, which must be found at the position of ``\1``. This RE will
detecte doubled words in a string: ``r'\b(\w+)\s+\1\b'``.

* ``(...)`` Matches the RE inside the parentheses, and indicates the start
  and end of a group. The contents of a group can be:

  * retrieved after a match has been performed
  * be matched later in the string with the ``\number`` (described below).

* ``(?...)`` meaning depends on the character following the ``?``. Do not
  usually create a new group (except for ``(?P<groupname>...)``).
* ``(?<flag>)`` a single character indicating a flag, which is set for the
  entire RE (alternative to pass a flag argument to a ``re`` function):

  * ``a`` ASCII only matching
  * ``i`` ignore case
  * ``L`` locale dependent
  * ``m`` multiline
  * ``s`` ``.`` matches all (including newline)
  * ``u`` unicode matching
  * ``x`` verbose

* ``(?:)`` non-capturing group. Matches RE inside but the substring matched
  cannot be retrieved.
* ``(?P<name>...)`` group can be accessed using 'name'. It can then be
  referenced:

  * in the RE with ``(?P=<name>)`` or ``\1``
  * in the match object ``m.group('name')``
  * in ``re.sub()``

Look ahead assertions
*********************

* ``(?=...)`` look ahead assertion. Matches if '...' (RE) matches next
  (but does not consume any of the string). ``Isaac (?=Asimov)`` will match
  'Isaac ' only if it’s followed by 'Asimov'.
* ``(?!...)`` negative look ahead assertion. Matches only if '...' does not
  match. Does not consume string. For example, ``Isaac (?!Asimov)`` will
  match 'Isaac ' only if it’s not followed by 'Asimov'.

Look behind assertion
*********************

* ``(?<=...)`` matches if the current position in the string is preceded by
  a match for ``...`` that ends at the current position. The pattern must be of
  a fixed length, meaning ``*`` is not allowed.

  * ``(?<=abc)def`` look for 'def' that is preceded by 'abc'. Thus the string
    'abcdef' will match
  * if a RE starts with a positive look behind assertion, it will not match
    at the start of a string, thus you need to use ``search`` and not
    ``match```

* ``(?<!...)`` matches if the current position in the string is not preceded
  by a match for ``...``. The contained pattern must only match strings of
  some fixed length. Patterns which start with negative lookbehind assertions
  may match at the beginning of the string being searched.

Functions
*********

All of these functions are available as a method of an compile object
or as ``re.<fun>``.

* ``match`` matches at start of string
* ``search`` searches entire string for match

Both return ``None`` if not succesful and a match object if succesful.

* ``findall`` looks for all matches, finds all substrings. Returns list
  of matching strings.
