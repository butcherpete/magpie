.. include:: <isopub.txt>
 
Vim Buffers
===========

A crib of Vim tips and tricks. 


Navigating the Buffer List
--------------------------

`Vimcast: Working with
Buffers <http://vimcasts.org/episodes/working-with-buffers/>`__

These commands show and navigate through the buffer list:

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``:ls``                           | Show the buffer list              |
+-----------------------------------+-----------------------------------+
| ``:bn``                           | Open the next buffer in the       |
|                                   | current window (cycles from the   |
|                                   | end of the list to the            |
|                                   | beginning).                       |
+-----------------------------------+-----------------------------------+
| ``:bp``                           | Open the previous buffer in the   |
|                                   | current window (cycles from the   |
|                                   | start of the list to the end).    |
+-----------------------------------+-----------------------------------+
| ``:b2``                           | Open buffers in the current       |
|                                   | window by specifying the buffer   |
|                                   | number.                           |
+-----------------------------------+-----------------------------------+
| ``CTRL-^``                        | Switch to the alternate file.     |
+-----------------------------------+-----------------------------------+

Explaining the buffer list:

+-----------------------------------+-----------------------------------+
| Symbol                            | Meaning                           |
+===================================+===================================+
| ``a``                             | Identifes the active buffer.      |
+-----------------------------------+-----------------------------------+
| ``h``                             | Identifies a hidden buffer.       |
+-----------------------------------+-----------------------------------+
| ``%``                             | Identfies the buffer displayed in |
|                                   | the current window.               |
+-----------------------------------+-----------------------------------+
| ``#``                             | Identifies the alternate buffer,  |
|                                   | which can be accessed by pressing |
|                                   | ``CTRL-^``.                       |
+-----------------------------------+-----------------------------------+

Opening Multiple Files into Buffers
-----------------------------------

To open the contents of a directory into the buffer:

.. code-block:: rest

   :args /path_to_dir/*

To open multiple files into the buffer list:

.. code-block:: rest

   :args a.txt b.txt c.txt 

To open open files into the buffer list using globs:

+------------------+---------------------------------+
| Glob             | Matching Files                  |
+==================+=================================+
| ``:args *.*``    | ``index.html``                  |
|                  | ``app.js``                      |
+------------------+---------------------------------+
| ``:args *.txt``  | ``a.txt``                       |
|                  | ``b.txt``                       |
+------------------+---------------------------------+
| ``:args **.js``  | ``app.js``                      |
|                  | ``lib/framework.js``            |
|                  | ``app/controllers/mailer.js``   |
+------------------+---------------------------------+
| ``:args **/*.*`` | ``index.html`` </br> ``app.js`` |
|                  | ``lib/framework.js``            |
|                  | ``lib/theme.css``               |
|                  | ``app/controllers/mailer.js``   |
+------------------+---------------------------------+

From *Practical Vim*.

Closing Buffers
---------------

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``:bd``, ``:bdelete``             | Unloads the current buffer and    |
|                                   | deletes if from the buffer list.  |
|                                   | The buffer is not completely      |
|                                   | deleted. It is removed from the   |
|                                   | buffer list, option values,       |
|                                   | variables, and mappings are       |
|                                   | cleared.                          |
+-----------------------------------+-----------------------------------+
| ``:bw``, ``:bwipeout``            | Deletes the current buffer.       |
|                                   | Everything related to the buffer  |
|                                   | is lost.                          |
+-----------------------------------+-----------------------------------+
| ``:bw2``                          | Deletes buffers by specifying he  |
|                                   | buffer number, i.e. ``:bw2``      |
+-----------------------------------+-----------------------------------+
| ``:1,3bw``                        | Deletes a range of buffers.       |
+-----------------------------------+-----------------------------------+

`vim-bdubs <https://github.com/jbranchaud/vim-bdubs>`__

+----------+----------------------------------------------------+
| Command  | Action                                             |
+==========+====================================================+
| ``:BD``  | Deletes all but the current buffer                 |
+----------+----------------------------------------------------+
| ``:BD3`` | Deletes all but the 3 most recently used buffers   |
+----------+----------------------------------------------------+
| ``:BW``  | Wipes out all but the current buffer               |
+----------+----------------------------------------------------+
| ``:BW2`` | Wipes out all but the 2 most recently used buffers |
+----------+----------------------------------------------------+

-  Uses ``:bdelete`` to delete all of the buffers in the buffer-list
   except for the current buffer.
-  Uses ``:bwipeout`` to delete all of the buffers in the buffer-list
   except for the current buffer. Because of the way ``:bw`` works, each
   deleted buffer will be unloaded and entirely removed from the buffer
   list.

Buffers in Airline
------------------

Tab line in airline automatically displays all buffers if only one tab
open. Added the following to my ``.vimrc`` file:

.. code-block:: rest

   let g:airline#extensions#tabline#enabled = 1

Argdo Command
-------------

`Vimcast: Using :argdo to change multiple
files <http://vimcasts.org/episodes/using-argdo-to-change-multiple-files/>`__

Substitutions in Multiple Buffers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make substitutions to buffers in the arglist:

.. code-block:: rest

   :argdo %s/mydoc_sidebar/notes_sidebar/ge

The ``e`` flag suppresses errors that may occur if a buffer in the
arglist does not contain a match for the specified pattern.

Reverting Changes
~~~~~~~~~~~~~~~~~

To revert changes:

.. code-block:: rest

   :argdo edit!

Saving Changes
~~~~~~~~~~~~~~

To save changes to files in arglist:

.. code-block:: rest

   :argdo update

