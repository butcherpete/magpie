
Vim JavaScript & Node
=====================

A crib of Vim tips and tricks. `Edit
me <https://github.com/butcherpete/documentation-theme-jekyll/blob/gh-pages/pages//_pages/vim/vim_javascript.html.md>`__

`Setting up Vim for JavaScript
development <https://davidosomething.com/blog/vim-for-javascript/>`__

http://vimawesome.com/plugin/node

Code Completion
---------------

https://github.com/nodejs/node/wiki/Vim-Plugins

You Complete Me
~~~~~~~~~~~~~~~

`valloric/youcompleteme <https://github.com/Valloric/YouCompleteMe#mac-os-x>`__

#. Install with Vundle
#. Compile YCM with semantic support for C-family languages.

   .. code:: highlight

      $ cd ~/.vim/bundle/youcompleteme
      $ ./install.py --clang-completer

#. Compile YCM with semantic support for JavaScript.

   .. code:: highlight

      $ cd ~/.vim/bundle/youcompleteme
      $ ./install.py --tern-completer

   cd ~/.vim/bundle/YouCompleteMe ./install.py –clang-complete

Tern for Vim
~~~~~~~~~~~~

TernJS parses JavaScript code and extracts symbols (e.g. function names,
variable names, and values).

`ternjs/tern_for_vim <https://github.com/ternjs/tern_for_vim>`__

In JavaScript files, tern_for_vim hooks into ‘omnicompletion’ to provide
for auto-completion support.

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``:TernDef``                      | Jump to the definition of the     |
|                                   | thing under the cursor.           |
+-----------------------------------+-----------------------------------+
| ``:TernDoc``                      | Look up the documentation of      |
|                                   | something.                        |
+-----------------------------------+-----------------------------------+
| ``:TernType``                     | Find the type of the thing under  |
|                                   | the cursor.                       |
+-----------------------------------+-----------------------------------+
| ``:TernRefs``                     | Show all references to the        |
|                                   | variable or property under the    |
|                                   | cursor.                           |
+-----------------------------------+-----------------------------------+
| ``:TernRename``                   | Rename the variable under the     |
|                                   | cursor.                           |
+-----------------------------------+-----------------------------------+

Tern Documentation
~~~~~~~~~~~~~~~~~~

`Tern Reference Manual <http://ternjs.net/doc/manual.html>`__

   Tern is a stand-alone code-analysis engine for JavaScript. It is
   intended to be used with a code editor plugin to enhance the editor’s
   support for intelligent JavaScript editing. Features provided are:

   -  Autocompletion on variables and properties
   -  Function argument hints
   -  Querying the type of an expression
   -  Finding the definition of something
   -  Automatic refactoring

Indentation
-----------

Highlighting
------------

Linting
-------

`vim-syntastic/syntastic <https://github.com/vim-syntastic/syntastic>`__

``:help syntastic-checkers``

