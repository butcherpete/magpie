.. include:: <isopub.txt>
 
############
VIMRC File
############


Getting Information and Help To get information:

.. code-block:: rest

   :version

To open vimrc within Vim:

.. code-block:: rest

   :e $MYVIMRC

To source the vimrc within Vim:

.. code-block:: rest

   :so $MYVIMRC

   " If the .vimrc is activ
   :so %

Brew
----

Installed with Homebrew.

-  Version: 8.0.52
-  Location: ``/usr/local/bin/vim`` ### Vimrc To edit:

.. code-block:: rest

   $ vim ~/.vimrc

To reload (source) changes to the ``.vimrc`` from within the .vimrc
file:

.. code-block:: rest

   :so %

The character ``%`` stands for the current file name (see
``:h current-file``).

Otherwise:

.. code-block:: rest

   :so $MYVIMRC

Vundle
------

To install in Vim, launch vim and run:

.. code-block:: rest

   :PluginInstall

To install from command line:

.. code-block:: rest

   $ vim +PluginInstall +qall

To read docs:

.. code-block:: rest

   :h vundle

