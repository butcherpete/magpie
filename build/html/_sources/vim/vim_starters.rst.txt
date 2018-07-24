Vim Starters
============

A crib of Vim tips and tricks. `Edit
me <https://github.com/butcherpete/documentation-theme-jekyll/blob/gh-pages/pages//_pages/vim/vim_starters.html.md>`__

Getting Information and Help To get information:

.. code:: highlight

   :version

.vimrc
------

To open vimrc within Vim:

.. code:: highlight

   :e $MYVIMRC

To source the vimrc within Vim:

.. code:: highlight

   :so $MYVIMRC

   " If the .vimrc is activ
   :so %

Brew
----

Installed with Homebrew.

-  Version: 8.0.52
-  Location: ``/usr/local/bin/vim`` ### Vimrc To edit:

.. code:: highlight

   $ vim ~/.vimrc

To reload (source) changes to the ``.vimrc`` from within the .vimrc
file:

.. code:: highlight

   :so %

The character ``%`` stands for the current file name (see
``:h current-file``).

Otherwise:

.. code:: highlight

   :so $MYVIMRC

Vundle
------

To install in Vim, launch vim and run:

.. code:: highlight

   :PluginInstall

To install from command line:

.. code:: highlight

   $ vim +PluginInstall +qall

To read docs:

.. code:: highlight

   :h vundle

