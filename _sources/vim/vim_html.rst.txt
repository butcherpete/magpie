.. include:: <isopub.txt>
 

Vim HTML
========

A crib of Vim tips and tricks. `Edit
me <https://github.com/butcherpete/documentation-theme-jekyll/blob/gh-pages/pages//_pages/vim/vim_html.html.md>`__

HTML Cleanup
------------

Live Preview of HTML
~~~~~~~~~~~~~~~~~~~~

Run the following in the root folder:

.. code-block:: rest

   $ python -m SimpleHTTPServer 8080

Editing HTML
~~~~~~~~~~~~

To delete blank lines:

.. code-block:: rest

   :g/^$/d

To strip trailing whitespace:

.. code-block:: rest

   :%s/\s\+$//e

To remove leading whitespace from range of lines:

.. code-block:: rest

   :19,25s/^\s\+//

Tidy
~~~~

Pipe the buffer through Tidy to get clean HTML:

.. code-block:: rest

   :%!tidy -qicbn -asxhtml

+--------------------------+---------------------------------------------+
| Command                  | Action                                      |
+==========================+=============================================+
| ``-indent``, ``-i``      | Indent element content                      |
+--------------------------+---------------------------------------------+
| ``-clean``, ``-c``       | Replace FONT, NOBR, and CENTER tags by CSS. |
+--------------------------+---------------------------------------------+
| ``-bare``, ``-b``        | Strip out smart quotes and em dashes, etc.  |
+--------------------------+---------------------------------------------+
| ``-quiet``, ``-q``       | Suppress nonessential output..              |
+--------------------------+---------------------------------------------+
| ``-asxml``, ``-asxhtml`` | Convert HTML to well formed XML.            |
+--------------------------+---------------------------------------------+

Use ``tidy -h`` to view more options.

Pandoc
~~~~~~

http://vimcasts.org/episodes/using-external-filter-commands-to-reformat-html/

Use the bang Ex command to filter the contents of the current buffer
through a pandoc pipeline:

.. code-block:: rest

   :%!pandoc --from=html --to=markdown | pandoc --from=markdown --to=html

Emmet
-----

+--------------+--------+-----------------------------+
| Command      | Mode   | Function                    |
+==============+========+=============================+
| ``<c-y>,``   |        | Expands abbreviations.      |
+--------------+--------+-----------------------------+
| ``<c-y>;``   |        | Expands words.              |
+--------------+--------+-----------------------------+
| ``<c-y>u``   |        | Expands tags.               |
+--------------+--------+-----------------------------+
| ``v_<c-y>,`` |        | Wraps with abbreviations.   |
+--------------+--------+-----------------------------+
| ``<c-y>d``   |        | Balance tags inward.        |
+--------------+--------+-----------------------------+
| ``<c-y>D``   | Insert | Balance tags outward.       |
+--------------+--------+-----------------------------+
| ``<c-y>n``   | Insert | Go to Next edit point.      |
+--------------+--------+-----------------------------+
| ``<c-y>N``   | Insert | Go to Previous edit point.  |
+--------------+--------+-----------------------------+
| ``<c-y>i``   |        | Update image sizes.         |
+--------------+--------+-----------------------------+
| ``<c-y>m``   |        | Merge lines.                |
+--------------+--------+-----------------------------+
| ``<c-y>k``   | Insert | Remove/return tags.         |
+--------------+--------+-----------------------------+
| ``<c-y>j``   | Insert | Split/join tags.            |
+--------------+--------+-----------------------------+
| ``<c-y>/``   | Insert | Add/remove comment tags.    |
+--------------+--------+-----------------------------+
| ``<c-y>a``   |        | Make anchor from URLs.      |
+--------------+--------+-----------------------------+
| ``<c-y>A``   |        | Make quoted text from URLs. |
+--------------+--------+-----------------------------+
| ``<c-y>c``   |        | Make code pretty.           |
+--------------+--------+-----------------------------+

Tutorial for Emmet.vim
~~~~~~~~~~~~~~~~~~~~~~

`Tutorial for
Emmet.vim <https://raw.githubusercontent.com/mattn/emmet-vim/master/TUTORIAL>`__

Expand an Abbreviation
^^^^^^^^^^^^^^^^^^^^^^

Type the abbreviation as ``div>p#foo$*3>a`` and type ``<c-y>,``.

.. code-block:: rest

   <div>
     <p id="foo1">
         <a href=""></a>
     </p>
     <p id="foo2">
         <a href=""></a>
     </p>
     <p id="foo3">
         <a href=""></a>
     </p>
   </div>

Wrap with an Abbreviation
^^^^^^^^^^^^^^^^^^^^^^^^^

Write as below.

.. code-block:: rest

   test1
   test2
   test3

Then do visual select (line wise) and type ``<c-y>,``.

Once you get to the Tag: prompt, type ``ul>li*``.

.. code-block:: rest

   <ul>
       <li>test1</li>
       <li>test2</li>
       <li>test3</li>
   </ul>

If you type a tag, such as ``blockquote``, then you’ll see the
following:

.. code-block:: rest

   <blockquote>
       test1
       test2
       test3
   </blockquote>

Balance Tags Inward
~~~~~~~~~~~~~~~~~~~

Type ``<c-y>d`` in Insert mode.

Balance Tags Outward
~~~~~~~~~~~~~~~~~~~~

Type ``<c-y>D`` in Insert mode.

Go to Next Edit Points
~~~~~~~~~~~~~~~~~~~~~~

Type ``<c-y>n`` in Insert mode.

Go to Previous Edit Points
~~~~~~~~~~~~~~~~~~~~~~~~~~

Type ``<c-y>N`` in Insert mode.

Update ``<img>`` Sizes
~~~~~~~~~~~~~~~~~~~~~~

Move cursor to the tag.

.. code-block:: rest

   <img src="foo.png" />

Type ``<c-y>i`` on the tag.

.. code-block:: rest

   <img src="foo.png" width="32" height="48" />

Merge Lines
~~~~~~~~~~~

Select the lines, which include ``<li>``.

.. code-block:: rest

   <ul>
     <li class="list1"></li>
     <li class="list2"></li>
     <li class="list3"></li>
   </ul>

Type ``<c-y>m``.

.. code-block:: rest

   <ul>
     <li class="list1"></li><li class="list2"></li><li class="list3"></li>
   </ul>

Remove Tags
~~~~~~~~~~~

Move cursor in block

.. code-block:: rest

   <div class="foo">
       <a>cursor is here</a>
   </div>

Type ``<c-y>k`` in Insert mode.

.. code-block:: rest

   <div class="foo">

   </div>

And type ``<c-y>k`` in there again.

Split/Join Tags
~~~~~~~~~~~~~~~

Move the cursor inside the block.

.. code-block:: rest

   <div class="foo">
       cursor is here
   </div>

Type ``<c-y>j`` in Insert mode.

.. code-block:: rest

   <div class="foo"/>

And then type ``<c-y>j`` in there again.

.. code-block:: rest

   <div class="foo">
   </div>

Toggle Comments
~~~~~~~~~~~~~~~

Move cursor inside the block.

.. code-block:: rest

   <div>
       hello world
   </div>

Type ``<c-y>/`` in Insert mode.

.. code-block:: rest

   <!-- <div>
       hello world
   </div> -->

Type ``<c-y>/`` in there again.

.. code-block:: rest

   <div>
       hello world
   </div>

Make Anchors from URLs
~~~~~~~~~~~~~~~~~~~~~~

Move cursor to the URL.

.. code-block:: rest

   http://www.google.com/

Type ``<c-y>a``

.. code-block:: rest

   <a href="http://www.google.com/">Google</a>

Make Quoted Text from URLs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Move cursor to the URL

.. code-block:: rest

   http://github.com/

Type ``<c-y>A``.

.. code-block:: rest

   <blockquote class="quote">
     <a href="http://github.com/">Secure source code hosting and collaborative development - GitHub</a><br />
     <p>How does it work? Get up and running in seconds by forking a project, pushing an existing repository...</p>
     <cite>http://github.com/</cite>
   </blockquote>

Enable emmet.vim for the language you using
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can customize the behavior of the languages you are using.

.. code-block:: rest

   let g:user_emmet_settings = {
     'php' : {
       'extends' : 'html',
       'filters' : 'c',
     },
     'xml' : {
       'extends' : 'html',
     },
     'haml' : {
       'extends' : 'html',
     },
   }

HTML Page
~~~~~~~~~

``html5:_``

Matchit
-------

To do, install machit

The ``%`` command jumps between matching parentheses. Matchit expands
this behavior to include jumps between paired ``< >``, HTML tags, or
regex expressions.

Vim-Ragtag
----------

https://github.com/tpope/vim-ragtag

   A set of mappings for HTML, XML, PHP, ASP, eRuby, JSP, and more
   (formerly allml)

..

   This plugin started out as a set of personal mappings, but there was
   enough enjoyment among those I shared it with for me to clean it up
   and release it.

