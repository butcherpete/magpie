#######
Greps
#######

.. contents::
  :local:
  :depth: 1

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

********
Rip Grep
********
https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

ripgrep is a command line tool that searches your files for patterns that you give it. ripgrep behaves as if reading each file line by line. If a line matches the pattern provided to ripgrep, then that line will be printed. If a line does not match the pattern, then the line is not printed.

.. code-block:: bash

  rg [options] pattern [files]

.. code-block:: bash

  $ rg -H --no-heading --vimgrep Waldo goldrush.txt 


*************
Quickfix List
*************

Load the files into the quickfix list and search using :code:`:grep` command. 

.. code-block:: bash

  $ nvim *.txt

  :grep -RIn Waldo .

  :!grep -n -RIn Waldo . /dev/null 2>&1| tee /var/folders/2n/9qt5qxhj2ql9l_1qzfb4c2kc0000gn/T/nvimcK
  wocL/4
  ./goldrush.txt:6:Waldo is studying his clipboard.
  ./goldrush.txt:10:The penny farthing is 10 paces ahead of Waldo.
  ./department-store.txt:1:Waldo is beside the boot counter.
  ./department-store.txt:7:EvilWaldo (in black/yellow) is beside the glove counter.
  
  (1 of 4): Waldo is studying his clipboard.
  Press ENTER or type command to continue

You can navigate the quickfix list using :code:`:cnext`, :code:`:cprev`, :code:`:cfirst`, :code:`:clast`.

*******
Grepper
*******

Tab Through Tools
=================

Use multiple tools.

1. Open file.

  .. code-block:: bash

    $ nvim *.txt

2. Open file.

  .. code-block:: bash

    :Grepper

3. Tab through the opitons: 

  .. code-block:: bash

    :Grepper

    grep -RIn $* .>
    ack --noheading --column>
    ag --vimgrep>
    git grep -nI>
    rg -H --no-heading --vimgrep>


3. Specify the query and press :code:`<CR>`: 

  .. code-block:: bash

    grep -RIn $* .> Waldo

Search for Current Word
=======================

.. code-block:: bash

  :Grepper -cword

  grep -RIn $* .> '\bWaldo\b'
  Found 3 matches.

