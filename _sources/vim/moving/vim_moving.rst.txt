.. include:: <isopub.txt>
 
Vim Getting Around
==================


Up-Down Motions
---------------

+-----------------------------------+-----------------------------------+
| Key                               | Action                            |
+===================================+===================================+
| *#* ``gk``                        | Count display lines upward.       |
|                                   | Differs from ``k`` when lines     |
|                                   | wrap, and when used with an       |
|                                   | operator.                         |
+-----------------------------------+-----------------------------------+
| *#* ``gj``                        | Count display lines upward.       |
|                                   | Differs from ``j`` when lines     |
|                                   | wrap, and when used with an       |
|                                   | operator.                         |
+-----------------------------------+-----------------------------------+
| *#* ``G``                         | Count display lines upward.       |
+-----------------------------------+-----------------------------------+
| ``G``                             | Go to bottom of file.             |
+-----------------------------------+-----------------------------------+
| ``gg``                            | Go to top of file.                |
+-----------------------------------+-----------------------------------+

Line Motions
------------

+--------+-------------------------------------+
| Key    | Action                              |
+========+=====================================+
| ``$``  | End of line                         |
+--------+-------------------------------------+
| ``$p`` | Paste to end of line                |
+--------+-------------------------------------+
| ``0``  | Start of line                       |
+--------+-------------------------------------+
| ``A``  | End of line & Input mode            |
+--------+-------------------------------------+
| ``C``  | Delete to the end line & Input mode |
+--------+-------------------------------------+

Word Motions
------------

+---------------+--------------------------+
| Key           | Action                   |
+===============+==========================+
| ``b`` / ``B`` | Backward one word/WORD   |
+---------------+--------------------------+
| ``w`` / ``W`` | Forward one word/WORD    |
+---------------+--------------------------+
| ``e``         | End of current/next word |
+---------------+--------------------------+
| ``E``         | End of current/next WORD |
+---------------+--------------------------+
| ``ge``        | End of previous word     |
+---------------+--------------------------+
| ``gE``        | End of previous WORD     |
+---------------+--------------------------+

WORDs are bigger than words.

-  A WORD consists of a sequence of non-blank characters is separated by
   white space. Both *we’re* and *e.g.* are WORDs.
-  A word consists of a sequence of letters, digits, and underscores.

Character Searches
------------------

+-------------+-------------------------------------------------------+
| Key         | Action                                                |
+=============+=======================================================+
| ``f{char}`` | Forward to the next {char}.                           |
+-------------+-------------------------------------------------------+
| ``F{char}`` | Backward to the previous {char}.                      |
+-------------+-------------------------------------------------------+
| ``t{char}`` | Forward to the character before next {char}.          |
+-------------+-------------------------------------------------------+
| ``T{char}`` | Backward to the characgter before the next {char}.    |
+-------------+-------------------------------------------------------+
| ``;``       | Repeat the last character-search command (forward).   |
+-------------+-------------------------------------------------------+
| ``,``       | Reverse the last character-search command (backward). |
+-------------+-------------------------------------------------------+

