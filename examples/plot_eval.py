"""
####################
Evaulation and Trees
####################
"""
# %%
# ************
# eval vs exec
# ************
#
# Ref: `SO <https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile/29456463#29456463>`_
#
# ``eval()`` evaluates a single dynamically generated Python expression.
#
# ``exec()`` executes dynamically generated Python code only for its side
# effects.
#
# * ``eval()`` excepts only a single expression. Anything to the RHS of a
#   variable assignment.
# * ``exec()`` excepts all Python code (e.g. includes statements like ``for``
#   ``if``, ``while``, ``class`` and ``def``). Note that:
#   ``if``-``elif``-``else`` chain, ``try``-``except``-``else``-``finally``
#   chain are considered a single statement.
#
# * ``eval()`` returns the value of the expression.
# * ``exec()`` ignores the output and always returns ``None``.
#
# Data directed to standard output e.g. ``print()``, is output.

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
# ``compile()`` can also compile source code to ``ast`` (see below).
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
# *****
# Trees
# *****
#
# Ref: `ruslanspivak <https://ruslanspivak.com/lsbasi-part7/>`_,
# `basecs <https://medium.com/basecs/grammatically-rooting-oneself-with-parse-trees-ec9daeda7dad>`_,
# `basecs2 <https://medium.com/basecs/leveling-up-ones-parsing-game-with-asts-d7a6fc2400ff>`_
#
# * data structure composed of 1 or more nodes, connected by edges
# * has 1 root, the top node
# * all nodes have a parent except the root node
# * a node with no children is called a leaf node
# * a node with 1 or more children and is not the root node, is called an
#   interior node
# * an interior node can be a 'complete subtree'
# * children - set of nodes with incoming edges from the same node are the
#   children of that node
# * parent - a node is the parent of all nodes it connects to with outgoing
#   edges
# * level - number of edges on the path from the root node
# * height - larges level of any node in the tree
#
# Parse tree
# ==========
#
# Also known as, concrete syntax tree, a parse is a tree that represents the
# syntatic structure of a language structure according to the grammar
# definition. It can be used to represent a language sentence, mathematical
# expression or code.
#
# To build a parse tree the first step is to break the expression into a list
# of tokens. Tokens or terminals are symbols that cannot be broken down any
# further. They help us understand how parts of an expression relate to one
# another and the syntactic relationships between individual elements. Examples
# in Python code include ``+``, ``-``, ``if``, ``else``. They also include
# factor values like string or number. These always end up being leaves in the
# tree. Non-terminals are expressions and terms which can potentially be broken
# down further.
#
# The job of the *parser* is to take some input and build a parse tree. This
# parse tree can be built by following a set of rules. For example, in a maths
# expression, whenever we see a parenthesis we know that we are starting a new
# expression and should create a new expression. Importantly, the grammar must
# not be ambiguous. In other words, one 'expression' should only lead to one
# parse tree.
#
# .. image:: ../_static/parsetree_01.png
#
# Take a look at the difference between a parse tree and an abstract syntax
# tree (AST):
#
# .. image:: ../_static/ast_01.png
#
# ASTs uses operators/operations as root and interior nodes while operands
# are children. ASTs do not represent every detail, e.g., no parentheses.
# Interior nodes are not used to represent grammar. Instead grammar, e.g.,
# operator precendence, is shown by it's level on the tree. Perform operations
# starting from the lowest node. AST shows us the 'important bits' or the
# abstracted syntax of the code 'sentence'.
#
# Technically - you can see that some interior nodes only have one child. These
# are called single-successor nodes. It tells us that the token is a factor
# or a term, but we are more interested in what the factor or term is. In the
# above case picture, compressing the single-successor nodes is all we have
# to do to get from the parse tree to the AST. In other cases we may need to
# do. For example, parentheses may be expressed like this:
#
# .. image:: ../_static/ast_paren.jpeg
#   :width: 700
#
# This structure is mirrored. The parentheses do not do much once we have our
# tree structure. The tree can be compressed by removing the top mirror, the
# parentheses subtree.
#
# The differences include:
#
# * AST will not contain syntactic details like parentheses and commas
# * operators such as ``+`` will be internal nodes and not leaves
#
# The parser may or may not generate a parse tree, it may go straight to AST,
# depending on the compiler. Building AST is actually very difficult which is
# why some parsers decide to build a parse tree first.
#
# AST
# ===
#
# Ref: `blog mattlayman <https://www.mattlayman.com/blog/2018/decipher-python-ast/>`_
#
# Your parser is performing these tasks:
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
# about what you wrote. AST contains enough structured information within them
# to make them useful for learning about your code.
#
# Each node in an AST contains some data (a token and its value) and pointers:
#
# .. image:: ../_static/ast_tree1.jpeg
#
# For example here is the AST of a simple equation:
#
# .. image:: ../_static/ast_tree2.jpeg
#
# Following the first child node/next sibling node points gives this:
#
# .. image:: ../_static/ast_tree3.jpeg
#
# You can think of the AST as the 'final project' of the front-end of the
# compiler (technically 'intermediate code representation').
#
# Used for modifying source code and dynamic code creation, as it is often
# easier to deal with tree of nodes rather than lines of text.
#
# For more see `blog basecs <https://medium.com/basecs/leveling-up-ones-parsing-game-with-asts-d7a6fc2400ff>`_
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
# this will not work:
# eval(compile(ast.Expression(code_ast.body[1]), '<string>', 'eval'))

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
# so that it is not run twice. A different solution in this
# `SO <https://stackoverflow.com/questions/33908794/get-value-of-last-expression-in-exec-call>`_
#
# `Green tree snakes <https://astexplorer.net/>`_ provides comprehensive
# (though difficult to understand) guide on the functions and methods of
# ast.
#
# `Blog tobiaskohn <https://tobiaskohn.ch/index.php/2018/07/30/transformations-in-python/>`_
# goes through ast in Python well.
