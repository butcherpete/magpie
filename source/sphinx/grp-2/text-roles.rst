.. _RFCs: http://foldoc.doc.ic.ac.uk/foldoc/foldoc.cgi?query=rfc&action=Search&sourceid=Mozilla-search

##################################################
Creating reStructuredText Interpreted Text Roles
##################################################

From http://docutils.sourceforge.net/docs/howto/rst-roles.html

Interpreted text roles are an extension mechanism for inline markup in reStructuredText.  This document aims to make the creation of new roles as easy and understandable as possible.

************************
Define the Role Function
************************
The :code:`role` function creates and returns inline elements (nodes) and does any additional processing required.  Its signature is as follows:

.. code-block:: python

    def role_fn(name, rawtext, text, lineno, inliner,
                options={}, content=[]):
        code...

    # Set function attributes for customization:
    role_fn.options = ...
    role_fn.content = ...

The role function parameters are as follows:

:code:`name`
  The local name of the interpreted role, the role name actually used in the document.

:code:`rawtext`
  A string containing the enitre interpreted text input, including the role and markup.  Return it as a :code:`problematic` node linked to a system message if a problem is encountered.

:code:`text`
  The interpreted text content.

:code:`lineno`
  The line number where the interpreted text begins.

:code:`inliner`
  The :code:`docutils.parsers.rst.states.Inliner` object that called :code:`role_fn`.  It contains the several attributes useful for error reporting and document tree access.

:code:`options`
  A dictionary of directive options for customization (from the `role directive <http://docutils.sourceforge.net/docs/ref/rst/directives.html#role>`_), to be interpreted by the role function.  Used for additional attributes for the generated elements and other functionality.

:code:`content`
  A list of strings, the directive content for customization (from the `role directive <http://docutils.sourceforge.net/docs/ref/rst/directives.html#role>`_).  To be interpreted by the role function.

.. Function attributes are described below (see `Specify Role Function Options and Content`_).  

Role functions return a tuple of two values:

* A list of nodes which will be inserted into the document tree at the point where the interpreted role was encountered (can be an empty list).

* A list of system messages, which will be inserted into the document tree immediately after the end of the current block (can also be empty).

*****************************************
Specify Role Function Options and Content
*****************************************
Function attributes are for customization, and are interpreted by the
`role directive <http://docutils.sourceforge.net/docs/ref/rst/directives.html#role>`_.  

If unspecified, :code:`role` function attributes are assumed to have the value :code:`None`.  Two function attributes are recognized:

:code:`options`
  The option specification.  All role functions implicitly support the "class" option, unless disabled with an explicit :code:`{'class': None}`.

  An option specification must be defined detailing the options available to the :code:`role` directive.  An option spec is a mapping of option name to conversion function; conversion functions are applied to each option value to check validity and convert them to the expected type.  

  Python's built-in conversion functions are often usable for this, such as :code:`int`, :code:`float`, and :code:`bool` (included in Python from version 2.2.1).  Other useful conversion functions are included in the :code:`docutils.parsers.rst.directives` package. For further details, see `Creating reStructuredText Directives <http://docutils.sourceforge.net/docs/howto/rst-directives.html#specify-directive-arguments-options-and-content>`_.

:code:`content`
  A boolean; true if :code:`role` directive content is allowed. Role functions must handle the case where content is required but not supplied (an empty content list will be supplied).

.. important:: As of this writing, no roles accept directive content.

Note that unlike directives, the :code:`arguments` function attribute is not supported for role customization.  Directive arguments are handled by the :code:`role` directive itself.

*****************
Register the Role
*****************

If the role is a general-use addition to the Docutils core, it must be registered with the parser and language mappings added:

1. Register the new role using the canonical name::

       from docutils.parsers.rst import roles
       roles.register_canonical_role(name, role_function)

   This code is normally placed immediately after the definition of the role funtion.

2. Add an entry to the :code:`roles` dictionary in :code:`docutils/parsers/rst/languages/en.py` for the role, mapping the English name to the canonical name (both lowercase).  Usually the English name and the canonical name are the same.  Abbreviations and other aliases may also be added here.

3. Update all the other language modules as well.  For languages in which you are proficient, please add translations.  For other languages, add the English role name plus "(translation required)".

If the role is application-specific, use the :code:`register_local_role` function::

    from docutils.parsers.rst import roles
    roles.register_local_role(name, role_function)


********
Examples
********

For the most direct and accurate information, "Use the Source, Luke!".

All standard roles are documented in `reStructuredText Interpreted Text Roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_, and the source code implementing them is located in the :code:`docutils/parsers/rst/roles.py` module.  Several representative roles are described below.

Generic Roles
=============
Many roles simply wrap a given element around the text.  There's a special helper function, :code:`register_generic_role`, which generates a role function from the canonical role name and node class::

    register_generic_role('emphasis', nodes.emphasis)

For the implementation of :code:`register_generic_role`, see the :code:`docutils.parsers.rst.roles` module.

RFC Reference Role
==================
This role allows easy references to RFCs_ (Request For Comments documents) by automatically providing the base URL, :code:`http://www.faqs.org/rfcs/`, and appending the RFC document itself (rfcXXXX.html, where XXXX is the RFC number).  For example:

.. code-block:: rst

    See :RFC:`2822` for information about email headers.

Here is the implementation of the role:

.. code-block:: python 
  :linenos:

    def rfc_reference_role(role, rawtext, text, lineno, inliner,
                           options={}, content=[]):

        # The interpreted text itself should contain the RFC number.  
        # The try clause verifies by converting it to an integer.  
        try:
            rfcnum = int(text)
            if rfcnum <= 0:
                raise ValueError

        # If the conversion fails, the except clause is executed: a system
        # message is generated, the entire interpreted text construct (in
        # rawtext) is wrapped in a problematic node (linked to the
        # system message), and the two are returned.
        except ValueError:
            msg = inliner.reporter.error(
                'RFC number must be a number greater than or equal to 1; '
                '"%s" is invalid.' % text, line=lineno)
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [prb], [msg]
        # Base URL mainly used by inliner.rfc_reference, so this is correct:
        ref = inliner.document.settings.rfc_base_url + inliner.rfc_url % rfcnum

        # The ``options`` function parameter, a dictionary, may contain a
        # "class" customization attribute; it is interpreted and replaced
        # with a "classes" attribute by the ``set_classes()`` function.  The
        # resulting "classes" attribute is passed through to the "reference"
        # element node constructor.
        set_classes(options)

        # RFC reference is constructed from a stock URI, set as refuri attribute
        # of a reference element
        node = nodes.reference(rawtext, 'RFC ' + utils.unescape(text), refuri=ref, **options)
        return [node], []

    register_canonical_role('rfc-reference', rfc_reference_role)


See :RFC:`2822` for information about email headers.

********
See Also
********

.. seealso::

  - `Creating reStructuredText Interpreted Text Roles <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`_
  - `reStructuredText Interpreted Text Roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_
  - `Interpreted Text <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#interpreted-text>`_ 

