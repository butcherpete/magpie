.. include:: /includes/<isopub.txt>
 

Vim Text Objects
================

A crib of Vim tips and tricks. `Edit
me <https://github.com/butcherpete/documentation-theme-jekyll/blob/gh-pages/pages//_pages/vim/vim_text_objects.html.md>`__

HTML Tags
---------

To select the contents of a tag (``t``):

.. code-block:: rest

   vit

To select the content of the outer tag:

.. code-block:: rest

   v_it

To select tags:

+---------+------------------------------------+
| Action  | Selection                          |
+=========+====================================+
| ``cit`` | Delete tag contents & insert mode. |
+---------+------------------------------------+
| ``dit`` | Delete tag contents.               |
+---------+------------------------------------+
| ``vit`` | Select tag contents & visual mode. |
+---------+------------------------------------+
| ``yit`` | Yank tag contents.                 |
+---------+------------------------------------+

Text Objects Selection
----------------------

+-----------------------------------+-----------------------------------+
| Text Object                       | Selection                         |
+===================================+===================================+
| ``a)`` / ``i)``                   | All / inside paretheses.          |
+-----------------------------------+-----------------------------------+
| ``a}`` / ``i}``                   | All / inside braces.              |
+-----------------------------------+-----------------------------------+
| ``a]`` / ``i]``                   | All / inside brackets.            |
+-----------------------------------+-----------------------------------+
| ``a>`` / ``i>``                   | All / inside angle brackets.      |
+-----------------------------------+-----------------------------------+
| ``a'`` / ``i'``                   | All / inside single quote.        |
+-----------------------------------+-----------------------------------+
| ``a"`` / ``i"``                   | All / inside double quote.        |
+-----------------------------------+-----------------------------------+
| :literal:`a\`` / :literal:`i\``   | All / inside backticks.           |
+-----------------------------------+-----------------------------------+
| ``at`` / ``it``                   | All / inside tags.                |
+-----------------------------------+-----------------------------------+
| ``a_`` / ``i_``                   | All / inside underscores.         |
|                                   | (vim-textobj-underscore)          |
+-----------------------------------+-----------------------------------+

Custom Text Objects
-------------------

`vim-textobj-user <https://github.com/kana/vim-textobj-user>`__

vim-textobj-user is a library plugin for Vim to define your own text
objects without handling many edge cases and complex stuffs.

A list of predefined text objects implemented using
``vim-textobj-user``.

`Text Object Plugins <https://github.com/kana/vim-textobj-user/wiki>`__

Plugins Installed:

-  `vim-textobj-underscore <https://github.com/lucapette/vim-textobj-underscore>`__:
   Works in Visual mode; In Default mode, works if cursor is over and
   underscore or blank space.

