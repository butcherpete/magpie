.. include:: <isopub.txt>
 
###########
Yanking
###########

A crib of Vim tips and tricks. 

.. contents::
  :local:
  :depth: 1

System Clipboard / Quoteplus Register
-------------------------------------

   CLIPBOARD is expected to be used for cut, copy and paste operations.
   … Vim uses CLIPBOARD when reading and writing the “+ register. (see
   \`:h quoteplus)

To yank text from a Vim buffer into the system clipboard, use these
commands:

+-----------------------------------+-----------------------------------+
| Command                           | Affect                            |
+===================================+===================================+
| ``{VISUAL}"+y``                   | Copy the selected text into the   |
|                                   | system clipboard.                 |
+-----------------------------------+-----------------------------------+
| ``"+y{motion}``                   | Copy the text specified by        |
|                                   | ``{motion}`` into the system      |
|                                   | clipboard.                        |
+-----------------------------------+-----------------------------------+
| ``:[range]yank +``                | Copy the text specified by        |
|                                   | ``[range]`` into the system       |
|                                   | clipboard.                        |
+-----------------------------------+-----------------------------------+

To copy text into the Mac OS register:

.. code-block:: rest

   "*y

To paste text from the system clipboard into a Vim buffer, use these
commands:

+------------+--------------------------------------------------------------+
| Command    | Affect                                                       |
+============+==============================================================+
| ``"+p``    | Pastes the system clipboard after the cursor in Normal mode. |
+------------+--------------------------------------------------------------+
| ``:put +`` | Puts contents of system clipboard on a new line.             |
+------------+--------------------------------------------------------------+
| ``<C-r>+`` | Pastes from Insert or Commandline mode.                      |
+------------+--------------------------------------------------------------+

Pasting
-------

To paste the contents of a register:

+---------+------------------------------------+
| Command | Affect                             |
+=========+====================================+
| ``p``   | Paste contents after the cursor.   |
+---------+------------------------------------+
| ``P``   | Paster contents before the cursor. |
+---------+------------------------------------+

Alfred’s Clipboard History
--------------------------

https://www.alfredapp.com/help/features/clipboard/

