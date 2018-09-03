.. include:: <isopub.txt>
 

Vim Windows
===========

A crib of Vim tips and tricks. 

Opening Split Windows
---------------------

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``ctrl-w s``                      | Split the current window          |
|                                   | horizontally, loading the same    |
|                                   | file in the new window            |
+-----------------------------------+-----------------------------------+
| ``ctrl-w v``                      | Split the current window          |
|                                   | vertically, loading the same file |
|                                   | in the new window                 |
+-----------------------------------+-----------------------------------+
| ``:sp[lit]`` *filename*           | Split the current window          |
|                                   | horizontally, loading filename in |
|                                   | the new window                    |
+-----------------------------------+-----------------------------------+
| :star: ``:vsp[lit]`` *filename*   | Split the current window          |
|                                   | vertically, loading filename in   |
|                                   | the new window                    |
+-----------------------------------+-----------------------------------+

Closing Split Windows
---------------------

+-------------+-------------------------------------------------------+
| Command     | Action                                                |
+=============+=======================================================+
| ``:q[uit]`` | Close the currently active window.                    |
+-------------+-------------------------------------------------------+
| ``:on[ly]`` | Close all windows except the currently active window. |
+-------------+-------------------------------------------------------+

Changing Focus Between Windows
------------------------------

+------------+--------------+---------------------------------+
| Shortcut   | Command      | Action                          |
+============+==============+=================================+
| -          | ``ctrl-w w`` | Cycle between the open windows. |
+------------+--------------+---------------------------------+
| ``ctrl-h`` | ``ctrl-w h`` | Focus the window to the left.   |
+------------+--------------+---------------------------------+
| ``ctrl-j`` | ``ctrl-w j`` | Focus the window to the down.   |
+------------+--------------+---------------------------------+
| ``ctrl-k`` | ``ctrl-w k`` | Focus the window to the up.     |
+------------+--------------+---------------------------------+
| ``ctrl-l`` | ``ctrl-w l`` | Focus the window to the right.  |
+------------+--------------+---------------------------------+

I included the following in my ``.vimrc`` file to enable the shortcuts:

.. code-block:: rest

   map <C-h> <C-w>h
   map <C-j> <C-w>j
   map <C-k> <C-w>k
   map <C-l> <C-w>l

Resizing Windows
----------------

You can resize windows by clicking on the boundary between windows, and
dragging it to your prefered size. The following key commands also help:

+--------------+----------------------------------------------+
| Command      | Action                                       |
+==============+==============================================+
| ``ctrl-w =`` | Makes the windows equal widths.              |
+--------------+----------------------------------------------+
| ``ctrl-w +`` | Increase height of current window by 1 line. |
+--------------+----------------------------------------------+
| ``ctrl-w -`` | Decrease height of current window by 1 line. |
+--------------+----------------------------------------------+
| ``ctrl-w _`` | Maximise height of current window.           |
+--------------+----------------------------------------------+
| ``ctrl-w |`` | Maximise width of current window.            |
+--------------+----------------------------------------------+

Moving Windows
--------------

+--------------+--------------------------------------------+
| Command      | Action                                     |
+==============+============================================+
| ``ctrl-w r`` | Rotate all windows.                        |
+--------------+--------------------------------------------+
| ``ctrl-w x`` | Exchange current window with its neighbor. |
+--------------+--------------------------------------------+
| ``ctrl-w H`` | Move current window to far left.           |
+--------------+--------------------------------------------+
| ``ctrl-w J`` | Move current window to bottom.             |
+--------------+--------------------------------------------+
| ``ctrl-w K`` | Move current window to top.                |
+--------------+--------------------------------------------+
| ``ctrl-w L`` | Move current window to far right.          |
+--------------+--------------------------------------------+

