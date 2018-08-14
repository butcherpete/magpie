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

For each match, return a filename, line number, and line contents.

.. code-block:: bash

  $ grep -RIn Waldo goldrush.txt

  goldrush.txt:6:Waldo is studying his clipboard.
  goldrush.txt:10:The penny farthing is 10 paces ahead of Waldo.

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
-- color always   Highlight for readability

