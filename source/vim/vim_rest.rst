.. include:: <isopub.txt>
 
Vim Restructured Text
=====================

A crib of Vim tips and tricks. `Edit
me <https://github.com/butcherpete/documentation-theme-jekyll/blob/gh-pages/pages//_pages/vim/vim_rest.html.md>`__

Marking Up Headers
------------------

A naïve approach (no plugins or scripting) would be ``Esc``\ + ``Y`` +
``p`` + ``V`` + ``r`` + ``=``

#. ``Y`` + ``p`` duplicates the current line and puts the cursor on the
   lower line.
#. ``V`` selects the second line in Visual Line mode.
#. ``r`` + ``=`` replaces all characters on the line with the ``=``
   character.

You can ``:noremap`` that keystroke sequence to your taste.

For example

.. code-block:: rest

   " Add Heading: Control-H
   nnoremap <C-h> YpVr

Leaving off the last character so you can type in whichever you want for
the title.

