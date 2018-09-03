.. include:: <isopub.txt>
 

Vim Miscellany
==============


Useful Commands
---------------

`Stackoverflow: Simple Vim commands you wish you’d known
earlier <https://stackoverflow.com/questions/1276403/simple-vim-commands-you-wish-youd-known-earlier>`__

Markdown Preview
----------------

I installed grip using homebrew. Grip provides the Github flavored
markdown formatting.

.. code-block:: rest

   $ grip filename.md

Fenced Code Blocks
------------------

``Esc`` + *n* + ``i`` + ``~`` + ``Esc``

For example ``5i~Esc``.

.. code-block:: rest

   Code Sample

Reading Microsoft Word Files
----------------------------

To view the content of ``.docx`` in Vim by adding the following to your
``.vimrc``.

.. code-block:: rest

   "use docx2txt.pl to allow VIm to view the text content of a .docx file directly.

   autocmd BufReadPre *.docx set ro
   autocmd BufReadPost *.docx %!docx2txt.pl 

The settings enables you to view ``.docx`` text specified as
command-line argument to vim, but not of those read using
``:r file.docx``.

Pandoc
------

`Vimcast 64:Using external filter commands to reformat
HTML <http://vimcasts.org/episodes/using-external-filter-commands-to-reformat-html/>`__

Use the bang Ex command to filter the contents of the current buffer
through a pandoc pipeline:

.. code-block:: rest

   :%!pandoc --from=html --to=markdown | pandoc --from=markdown --to=html

URLs
----

+---------+-------------------------+
| Command | Action                  |
+=========+=========================+
| ``gx``  | Opens URL under cursor. |
+---------+-------------------------+

Emojis
------

http://www.webpagefx.com/tools/emoji-cheat-sheet/

