#######
Grepper
#######

- grep
- git-grep
- Ripgrep

****
Grep
****

.. code-block:: bash

  grep [options] pattern [files]

For each match in the specified file, return a filename, line number, and line contents:

.. code-block:: bash

  $ grep -RIn Waldo goldrush.txt

  goldrush.txt:6:Waldo is studying his clipboard.
  goldrush.txt:10:The penny farthing is 10 paces ahead of Waldo.

Search all files in the specified directory:

.. code-block:: bash

  $ grep -R string dir/ 

Useful Options
==============

-v    Print lines that do not match
-l    Print filenames not the lines
-L    Print filename that do not contain lines
-c    Print count of matching lines
-n    Print matching line number
-i    Case insenstive
-w    Match complete word only
-x    Match complete lines only
-r    Recursive
-A N  Print next N lines
-B N  Print previous N lines
-C N  Print previous and next N lines 
-E    Use extended regular expressions (egrep)
-F    Use list of fixed strings (fgrep)
--color always   Highlight for readability


********
Git Grep
********
https://git-scm.com/docs/git-grep

.. code-block:: bash

  git grep [options] pattern [files]

Looks for time_t in all tracked .c and .h files in the working directory and its subdirectories.

.. code-block:: bash

  $ git grep 'time_t' -- '*.[ch]'

Looks for a line that has #define and either MAX_PATH or PATH_MAX.

.. code-block:: bash

  $ git grep -e '#define' --and \( -e MAX_PATH -e PATH_MAX \)

Looks for a line that has NODE or Unexpected in files that have lines that match both.

.. code-block:: bash

  $ git grep --all-match -e NODE -e Unexpected

Looks for solution, excluding files in Documentation.

.. code-block:: bash

  $ git grep solution -- :^Documentation

For each match in the specified file, return a filename, line number, and line contents:

.. code-block:: bash

  $ git grep -RIn Waldo goldrush.txt

  goldrush.txt:6:Waldo is studying his clipboard.
  goldrush.txt:10:The penny farthing is 10 paces ahead of Waldo.

