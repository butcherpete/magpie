.. include:: <isopub.txt>
 
Vim Surround
============

The surround-vim plugin is a tool for dealing with pairs of
surroundings. Examples of surroundings include parentheses, quotes, and
HTML tags. They are closely related to what Vim refers to as
\|text-objects|. Provided are mappings to allow for removing, changing,
and adding surroundings. 

Introduction
------------

`surround-vim <https://github.com/tpope/vim-surround>`__

Mappings
--------

*surround-mappings*

-  Delete surroundings: ``ds``
-  Change surroundings: ``cs`` or ``cS``
-  Add surroundings: ``ys`` , ``yS`` or ``ySS``
-  Visual mode: ``vS`` or ``vgS``

Change Surroundings
~~~~~~~~~~~~~~~~~~~

Change surroundings is ``cs``. It takes two arguments a *target* and a
*replacement*.

+---------------------+------------+----------------+
| Before              | Action     | After          |
+=====================+============+================+
| ``"Hello *world!"`` | ``cs"'``   | ‘Hello world!’ |
+---------------------+------------+----------------+
| ``"Hello *world!"`` | ``cs"<q>`` | “Hello world!” |
+---------------------+------------+----------------+
| ``(123+4*56)/2``    | ``cs)]``   | [123+456]/2    |
+---------------------+------------+----------------+
| ``(123+4*56)/2``    | ``cs)[``   | [ 123+456 ]/2  |
+---------------------+------------+----------------+
| ``<div>Yo!*</div>`` | ``cst<p>`` | <p>Yo!</p>     |
+---------------------+------------+----------------+

``cS`` changes surroundings, placing the surrounded text on its own
line(s) like ``yS``. Details about the second argument can be found
below in *surround-replacements*.

Description:

+------------+-----------------------------------------+
| Key        | Action                                  |
+============+=========================================+
| ``cs"'``   | Replaces surrounding ``"`` with ``'``   |
+------------+-----------------------------------------+
| ``cs'<q>`` | Replaces surrounding ``'`` with ``<q>`` |
+------------+-----------------------------------------+
| ``cst"``   | Replaces surrounding tag with ``"``     |
+------------+-----------------------------------------+

Delete Surroundings
~~~~~~~~~~~~~~~~~~~

Delete surroundings is ``ds``. The next character given determines the
targetted delete. The exact nature of the target is explained in
*surround-targets* but essentially it is the last character of a
*text-object*.

This mapping deletes the difference between the “i”nner object and “a”n
object. This is easiest to understand with some examples:

+----------------------+---------+--------------+
| Before               | Action  | After        |
+======================+=========+==============+
| ``"Hello *world!"``  | ``ds"`` | Hello world! |
+----------------------+---------+--------------+
| ``(123+4*56)/2``     | ``ds)`` | 123+456/2    |
+----------------------+---------+--------------+
| ``<div>Yo!*\</div>`` | ``dst`` | Yo!          |
+----------------------+---------+--------------+

Add Surroundings
~~~~~~~~~~~~~~~~

Add surroundings: ``ys`` , ``yS`` or ``ySS``.

Words
^^^^^

``ys`` takes a valid Vim motion or text object as the first object, and
wraps it using the second argument as with ``cs``. (It’s a stretch, but
a good mnemonic for ``ys`` is “you surround”.)

+-------------------+-----------+----------------+
| Before            | Action    | After          |
+===================+===========+================+
| ``Hello w*orld!`` | ``ysiw)`` | Hello (world)! |
+-------------------+-----------+----------------+

Lines
^^^^^

As a special case, *yss* operates on the current line, ignoring leading
whitespace.

+-------------------+----------+----------------+
| Before            | Action   | After          |
+===================+==========+================+
| ``Hello w*orld!`` | ``yssB`` | {Hello world!} |
+-------------------+----------+----------------+

Indentation
^^^^^^^^^^^

There is also ``yS`` and ``ySS`` which indent the surrounded text and
place it on a line of its own.

+---------+--------+
| Key     | Action |
+=========+========+
| ``yS``  |        |
+---------+--------+
| ``ySS`` |        |
+---------+--------+

Visual Mode Surroundings
------------------------

   In visual mode, a simple “S” with an argument wraps the selection.
   This is referred to as the *vS* mapping, although ordinarily there
   will be additional keystrokes between the v and S. In linewise visual
   mode, the surroundings are placed on separate lines and indented. In
   blockwise visual mode, each line is surrounded.

..

   A “gS” in visual mode, known as *vgS* , behaves similarly. In
   linewise visual mode, the automatic indenting is suppressed. In
   blockwise visual mode, this enables surrounding past the end of the
   line with ‘virtualedit’ set (there seems to be no way in Vim Script
   to differentiate between a jagged end of line selection and a virtual
   block selected past the end of the line, so two maps were needed).

+------------------------------------+---------------------------+
| Key                                | Action                    |
+====================================+===========================+
| Visual select + ``S<p class="x">`` | Surround text in element. |
+------------------------------------+---------------------------+

Targets
-------

*surround-targets*

The Vim Surround ``ds`` and ``cs`` commands both take a target as their
first argument. The possible targets are based closely on the
*text-objects* provided by Vim.

All targets are currently just one character.

+--------------+--------------------------------+
| Target       | Lexeme                         |
+==============+================================+
| ``(``, ``b`` | Parentheses                    |
+--------------+--------------------------------+
| ``)``, ``b`` | Parentheses, no whitespace     |
+--------------+--------------------------------+
| ``{``, ``B`` | Curly braces                   |
+--------------+--------------------------------+
| ``}``, ``B`` | Curly braces, no whitespace    |
+--------------+--------------------------------+
| ``[``, ``r`` | Brackets                       |
+--------------+--------------------------------+
| ``]``, ``r`` | Brackets, no whitespace        |
+--------------+--------------------------------+
| ``<``, ``a`` | Angled brackets                |
+--------------+--------------------------------+
| ``>``, ``a`` | Angled brackets, no whitespace |
+--------------+--------------------------------+
| ``t``        | HTML or XML tags               |
+--------------+--------------------------------+
| ``'``        | Single quotes                  |
+--------------+--------------------------------+
| ``"``        | Double quotes                  |
+--------------+--------------------------------+
| ``\```       | Back ticks                     |
+--------------+--------------------------------+
| :code:`-`    | Sphinx code markup             |
+--------------+--------------------------------+
| :code:`=`    | Sphinx link                    |
+--------------+--------------------------------+
| :code:`\``   | Back ticks                     |
+--------------+--------------------------------+
| ``w``        | Words                          |
+--------------+--------------------------------+
| ``W``        | WORDS                          |
+--------------+--------------------------------+
| ``s``        | Sentences                      |
+--------------+--------------------------------+

Punctuation Marks
~~~~~~~~~~~~~~~~~

Eight punctuation marks, ``(``, ``)``, ``{``, ``}``, ``[``, ``]``,
``<``, and ``>``, represent themselves and their counterparts. If the
closing mark is used, contained whitespace is also trimmed.

The targets ``b``, ``B``, ``r``, and ``a`` are aliases for ``)``, ``}``,
``]``, and ``>``. The first two (``b`` and ``B``) are standard Vim
mappings; the second two (``r`` and ``a``) are unique to vim-surround.

Quotation Marks
~~~~~~~~~~~~~~~

Three quote marks, ``'``, ``"``, :literal:`\``, represent themselves, in
pairs. They are only searched for on the current line.

Tag Alias
~~~~~~~~~

A ``t`` is a pair of HTML or XML tags. See *tag-blocks* for details.

Remember that you can specify a numerical argument if you want to get to
a tag other than the innermost one.

The letters ``w``, ``W``, and ``s`` correspond to a *word*, a *WORD*,
and a *sentence*, respectively. These are special in that they have
nothing to delete, and used with ``ds`` they are a no-op. With ``cs``,
one could consider them a slight shortcut for ``ysi`` (``cswb`` ==
``ysiwb``, more or less).

A ``p`` represents a *paragraph*. This behaves similarly to ``w``,
``W``, and ``s`` above; however, newlines are sometimes added and/or
removed.

Customization
-------------
To determine the ASCII code run the following in the vim command line. 

.. code-block:: none 

  :echo char2nr("-").  

Use a global variable for globally available replacements.

.. code-block:: none
  :caption: vimrc

  let g:surround_45 = ":code:`\r`" # -
  let g:surround_61 = "` <\r>`_"  # =

