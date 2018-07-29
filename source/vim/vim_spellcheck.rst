.. include:: <isopub.txt>
 
Vim Spellchecking
=================


http://vimcasts.org/episodes/spell-checking/

Enabling
--------

To turn on spell check.

.. code-block:: rest

   :set spell

The spell check recognizes four types of misspelled words:

+-----------------+-----------------------------------------+
| Highlight Group | Description                             |
+=================+=========================================+
| ``SpellBad``    | Unrecognized words.                     |
+-----------------+-----------------------------------------+
| ``SpellCap``    | Uncapitalized words.                    |
+-----------------+-----------------------------------------+
| ``SpellRare``   | Rare words.                             |
+-----------------+-----------------------------------------+
| ``SpellLocal``  | Incorrect spelling for selected region. |
+-----------------+-----------------------------------------+

Configuration
-------------

To set spelling language to American English.

.. code-block:: rest

   :set spelllang=en_us

.vimrc configurations:
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rest

   :set spelllang=en_us
   :set spellfile=$HOME/Dropbox/vim/spell/en.utf-8.add

By default, vim saves added words (``zg``) to
``.vim/spell/en.utf-8.add``. I moved the spellfile to my Dropbox to
enable me to use it across computers.

Local Spellfiles
~~~~~~~~~~~~~~~~

Multiple spellfiles can be defined.

.. code-block:: rest

   :setl spelllang=en_us
   :setl spellfile=/.vim/spell/en.utf-8.add
   :setl spellfile+=~/Drobox/vim/spell/jargon.utf-8.add
   :setl spellfile+=~/Drobox/vim/spell/intel.utf-8.add

If multiple spellfiles are defined, you can press ``1zg`` to add words
to the default spellfile and ``2zg`` to add words to the jargon
spellfile.

   What is the difference between ``:set`` and ``:setlocal``?

   -  ``:set`` sets properties globally.
   -  ``:setl`` sets properties locally to the current buffer or window.

Searching for Misspelled Words
------------------------------

+---------+-----------------------------------+
| Command | Action                            |
+=========+===================================+
| ``]s``  | Go to next misspelled word.       |
+---------+-----------------------------------+
| ``[s``  | Go to previous misspelled word.   |
+---------+-----------------------------------+
| ``]S``  | Go to next ``SpellBad`` word.     |
+---------+-----------------------------------+
| ``[S``  | Go to previous ``SpellBad`` word. |
+---------+-----------------------------------+

Correcting Words
----------------

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| ``z=``                            | View suggested spelling. To       |
|                                   | select a suggestion, enter the    |
|                                   | line number and press the Return  |
|                                   | key.                              |
+-----------------------------------+-----------------------------------+
| ``1z=``                           | Take the first suggestion without |
|                                   | viewing the list. To reverse the  |
|                                   | correction, press the ``u`` key.  |
+-----------------------------------+-----------------------------------+

Updating Spellfiles and Word Lists
----------------------------------

+-----------------------------------+-----------------------------------+
| Command                           | Action                            |
+===================================+===================================+
| zg                                | Adds the word under the cursor to |
|                                   | the ‘spellfile’. If the command   |
|                                   | is preceded by a number, you can  |
|                                   | specify an alternative spellfile  |
|                                   | entry. Default entry is           |
|                                   | ``~/.vim/spell/en.utf-8.add``.    |
+-----------------------------------+-----------------------------------+
| 2zg                               | Adds the word under the cursor to |
|                                   | the                               |
|                                   | ``~/Dropbox/vim/spell/jargon.utf- |
|                                   | 8.add``                           |
|                                   | spellfile.                        |
+-----------------------------------+-----------------------------------+
| 3zg                               | Adds the word under the cursor to |
|                                   | the                               |
|                                   | ``~/Dropbox/vim/spell/intel.utf-8 |
|                                   | .add``                            |
|                                   | spellfile.                        |
+-----------------------------------+-----------------------------------+
| zG                                | Adds the word to the internal     |
|                                   | word list.                        |
+-----------------------------------+-----------------------------------+
| zw                                | Marks the word as a bad word. If  |
|                                   | the word already appears in       |
|                                   | ‘spellfile’ it is turned into a   |
|                                   | comment line.                     |
+-----------------------------------+-----------------------------------+
| zW                                | Marks the word as a bad word in   |
|                                   | the internal word list.           |
+-----------------------------------+-----------------------------------+
| zuw                               | Removes the bad word from the     |
|                                   | ‘spellfile’.                      |
+-----------------------------------+-----------------------------------+
| zug                               | Removes the good word from the    |
|                                   | ‘spellfile’.                      |
+-----------------------------------+-----------------------------------+
| zuW                               | Removes the bad word from the     |
|                                   | ‘internal word list’.             |
+-----------------------------------+-----------------------------------+
| zuG                               | Removes the good word from the    |
|                                   | ‘internal word list’.             |
+-----------------------------------+-----------------------------------+

To view the spell file:

.. code-block:: rest

   `~/.vim/spell/en.utf-8.add`

