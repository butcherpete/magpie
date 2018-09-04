#########
Node REPL
#########

- https://nodejs.org/api/repl.html
- https://hackernoon.com/know-node-repl-better-dbd15bca0af6

*************************
Commands and Special Keys
*************************
The following special commands are supported by all REPL instances:

- :code:`.break` - When in the process of inputting a multi-line expression, entering the :code:`.break` command (or pressing the :code:`<ctrl>-C` key combination) will abort further input or processing of that expression.
- :code:`.clear` - Resets the REPL context to an empty object and clears any multi-line expression currently being input.
- :code:`.exit` - Close the I/O stream, causing the REPL to exit.
- :code:`.help` - Show this list of special commands.
- :code:`.save` - Save the current REPL session to a file: :code:`> .save ./file/to/save.js`
- :code:`.load` - Load a file into the current REPL session. :code:`> .load ./file/to/load.js`
- :code:`.editor` - Enter editor mode (:code:`<ctrl>-D` to finish, :code:`<ctrl>-C` to cancel).

Break
===============
These commands can be used to terminate and come out of a multi line session. Sometimes while copy pasting code snippet into REPL, we get stuck. We can type :code:`.break` to terminate a multi-line session in such cases and get back to REPL prompt.



Clear
=====
https://stackoverflow.com/questions/18971034/the-clear-meta-command-in-the-node-js-repl

The :code:`.break` and :code:`.clear` commands behave differently depending on if you started the REPL from the node command, or used :code:`repl.start()`.

When using the node command, :code:`.clear` is just an alias for :code:`.break`. But if you start the REPL from :code:`repl.start()`, :code:`.clear` will then clear the local context as you are expecting, and :code:`.break` behaves as stated.

.. code-block:: javascript
  :caption: example.js

  const repl = require('repl');
  
  function initializeContext(context) {
    context.m = 'test';
  }
  
  const r = repl.start({ prompt: '> ' });
  initializeContext(r.context);
  
  r.on('reset', initializeContext);

When this code is executed, the global :code:`m` variable can be modified but then reset to its initial value using the :code:`.clear` command:

.. code-block:: javascript

  $ ./node example.js
  > m
  'test'
  > m = 1
  1
  > m
  1
  > .clear
  Clearing context...
  > m
  'test'
  >

Load
====

.. code-block:: javascript
  :linenos:

  > .load ./file/to/load.js


Editor
======

.. code-block:: javascript
  :linenos:

  > .editor
  // Entering editor mode (^D to finish, ^C to cancel)
  function welcome(name) {
    return `Hello ${name}!`;
  }
  
  welcome('Node.js User');
  
  // ^D
  'Hello Node.js User!'
  >

****************
Key Combinations
****************

The following key combinations in the REPL have these special effects:

- :code:`<ctrl>-C` - When pressed once, has the same effect as the .break command. When pressed twice on a blank line, has the same effect as the .exit command.
- :code:`<ctrl>-D` - Has the same effect as the .exit command.
- :code:`<tab>` - When pressed on a blank line, displays global and local (scope) variables. When pressed while entering other input, displays relevant autocompletion options.

*******************
Underscore Variable
*******************
The default evaluator will, by default, assign the result of the most recently evaluated expression to the special variable _ (underscore). Explicitly setting _ to a value will disable this behavior.

.. code-block:: javascript
  :linenos:

  > [ 'a', 'b', 'c' ]
  [ 'a', 'b', 'c' ]
  > _.length
  3
  > _ += 1
  Expression assignment to _ now disabled.
  4
  > 1 + 1
  2
  > _
  4

Similarly, _error will refer to the last seen error, if there was any. Explicitly setting _error to a value will disable this behavior.

.. code-block:: javascript
  :linenos:

  > throw new Error('foo');
  Error: foo
  > _error.message
  'foo'
