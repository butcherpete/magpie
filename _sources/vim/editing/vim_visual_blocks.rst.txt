.. include:: <isopub.txt>
 
Visual Mode
===========

Visual mode is a flexible and easy way to select a piece of text for an
operator. It is the only way to select a block of text. 

Entering and Exiting Visual Modes
---------------------------------

Visual mode has three submodes: character-wise mode, line-wise mode, and
block-wise mode.

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``v``                             | Enter Visual mode per character.  |
+-----------------------------------+-----------------------------------+
| ``V``                             | Enter Visual mode per line.       |
+-----------------------------------+-----------------------------------+
| ``CTRL-V``                        | Enter Visual mode per block.      |
+-----------------------------------+-----------------------------------+
| ``gv``                            | Enter Visual mode with the same   |
|                                   | area as the previous area and the |
|                                   | same mode.                        |
+-----------------------------------+-----------------------------------+
| ``<Esc>``                         | Exit Visual Block Mode with       |
|                                   | insertion.                        |
+-----------------------------------+-----------------------------------+
| ``CTRL-C``                        | Exit Visual Block Mode without    |
|                                   | insertion.                        |
+-----------------------------------+-----------------------------------+

Changing the Visual Area
------------------------

+---------+------------------------------------+
| Command | Action                             |
+=========+====================================+
| ``o``   | Toggle cursor to opposite corner.  |
+---------+------------------------------------+
| ``O``   | Toggle cursor to end of same line. |
+---------+------------------------------------+
| ``$``   | Highlight to end of longest line.  |
+---------+------------------------------------+

Operating on Visual Blocks
--------------------------

`vimcasts 22: Selecting columns with visual block
mode <http://vimcasts.org/episodes/selecting-columns-with-visual-block-mode/>`__

+---------+------------------------------------------------------+
| Command | Action                                               |
+=========+======================================================+
| ``c``   | Change selection (delete and switch to Insert mode). |
+---------+------------------------------------------------------+
| ``I``   | Insert in front of cursor.                           |
+---------+------------------------------------------------------+
| ``A``   | Append after cursor.                                 |
+---------+------------------------------------------------------+
| ``r``   | Replace every character in selection.                |
+---------+------------------------------------------------------+
| ``d``   | Delete selection.                                    |
+---------+------------------------------------------------------+

Selecting Columns in Visual Block Mode
--------------------------------------

To insert on multiple lines:

#. Move the cursor to the first letter of the first line.
#. Enter visual block mode (CTRL+v).
#. Press ``j`` to select to end of list.
#. Press ``I``.
#. Type the prefix. For example, ``*<space>``
#. Press the ``<Esc>`` key.

