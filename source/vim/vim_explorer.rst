.. include:: <isopub.txt>
 
File Explorer
=============

A crib of Vim tips and tricks. `Edit
me <https://github.com/butcherpete/documentation-theme-jekyll/blob/gh-pages/pages//_pages/vim/vim_explorer.html.md>`__

Exploring the Filesystem
------------------------

+----------+---------------+-------------------------------------------------+
| Lazy     | Command       | Open File Explorer                              |
+==========+===============+=================================================+
| ``:e.``  | ``:edit .``   | At current working directory.                   |
+----------+---------------+-------------------------------------------------+
|          | ``:cd``       | Change the working directory.                   |
+----------+---------------+-------------------------------------------------+
| ``:sp.`` | ``:split .``  | In split at current working directory.          |
+----------+---------------+-------------------------------------------------+
| ``:vs.`` | ``:vsplit .`` | In vertical split at current working directory. |
+----------+---------------+-------------------------------------------------+
| ``:E``   | ``:Explore``  | At directory of current line.                   |
+----------+---------------+-------------------------------------------------+
| ``:Se``  | ``:Sexplore`` | In split at directory of current line.          |
+----------+---------------+-------------------------------------------------+
| ``:Vex`` | ``:Vexplore`` | In vertical split at directory of current line. |
+----------+---------------+-------------------------------------------------+

Manipulating the Filesystem
---------------------------

+---------+---------------------------------------------+
| Command | Action                                      |
+=========+=============================================+
| ``%``   | Create a new file.                          |
+---------+---------------------------------------------+
| ``d``   | Create a new directory.                     |
+---------+---------------------------------------------+
| ``R``   | Rename the file/directory under the cursor. |
+---------+---------------------------------------------+
| ``D``   | Delete the file/directory under the cursor. |
+---------+---------------------------------------------+

Vinegar
-------

vinegar.vim: combine with netrw to create a delicious salad dressing.
`vim-vinegar <https://github.com/tpope/vim-vinegar>`__

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``-``                             | Press ``-`` in any buffer to hop  |
|                                   | up to the directory listing and   |
|                                   | seek to the file you just came    |
|                                   | from. Keep bouncing to go up, up, |
|                                   | up. Having rapid directory access |
|                                   | available changes everything.     |
+-----------------------------------+-----------------------------------+
| ``cg`` or ``cl``                  | Press ``cg`` or ``cl`` to ``:cd`` |
|                                   | or ``:lcd`` to the currently      |
|                                   | edited directory.                 |
+-----------------------------------+-----------------------------------+
| ``~``                             | Press ``~`` to go home.           |
+-----------------------------------+-----------------------------------+
| ``I``                             | Press ``I`` to toggle display the |
|                                   | help at the top of the File       |
|                                   | Explorer. All that annoying crap  |
|                                   | at the top is turned off, leaving |
|                                   | you with nothing but a list of    |
|                                   | files. This is surprisingly       |
|                                   | disorienting, but ultimately very |
|                                   | liberating.                       |
+-----------------------------------+-----------------------------------+
| ``.``                             | Press ``.`` on a file to          |
|                                   | pre-populate it at the end of a : |
|                                   | command line. This is great, for  |
|                                   | example, to quickly initiate a    |
|                                   | ``:grep`` of the file or          |
|                                   | directory under the cursor.       |
|                                   | There’s also ``!``, which starts  |
|                                   | the line off with a bang. Type    |
|                                   | ``!chmod +x`` and get             |
|                                   | ``:!chmod +x path/to/file``.      |
+-----------------------------------+-----------------------------------+
| ``gh``                            | Press ``gh`` to toggle dot file   |
|                                   | hiding. Enabled if add            |
|                                   | ``g:netrw_list_hide`` =           |
|                                   | ``'\(^\|\s\s\)\zs\.\S\+'`` to     |
|                                   | your vimrc. vinegar will          |
|                                   | initialize with dot files hidden. |
+-----------------------------------+-----------------------------------+

Other changes:

-  The oddly C-biased default sort order is replaced with a sensible
   application of ‘suffixes’.
-  File hiding: files are not listed that match with one of the patterns
   in ‘wildignore’.

