.. include:: <isopub.txt>
 
#########################
Term Definition Role 
#########################

**********
Goals
**********
Identify and implement a role-based glossary term solution that using CSS-based hover boxes to display glossary term definitions. The solution with include custom roles, css, and possibility custom JS.
 
We want the extension to add a glossary-definition role to Sphinx. 

Three options:

Abbreviation
============
A role based on the existing :code:`abbreviation` role. The author must specify text or a variable in the role defintion. The hover box is defined in CSS and not as a HTML tool-tip.

The role is marked up like this:

.. code-block:: rest

  :glossy:`term (|term-variable|)`

And generates the following HTML:

.. code-block:: html 

  <a class= "glossy reference">



Term
============
A role based on the existing :code:`term` role. The role creates a reference to the glossary definition that is handled with as a CSS hover box. Would require JavaScript.

.. code-block:: rest

  :glossy:`term`

And generates the following HTML:

.. code-block:: html 

  <a class="reference internal" href="../../other/glossary.html#term-internal-link" id="yui_3_17_2_1_1534018420860_591"><span class="xref std std-term">term</span></a>

Ref
============
A role based on the existing :code:`ref` role. The role accepts a number and creates a reference to a distinct answer page that is handled with as a CSS hover box. May require JavaScript.

.. code-block:: rest

  :glossy:`term (3456)`

And generates the following HTML:

.. code-block:: html 

  <a class="glossy reference internal" data-answer="3456" href="/path/3456.html">term</a>


Worth research:

- http://docutils.sourceforge.net/docutils/parsers/rst/roles.py
- The term role may be built in the Sphinx glossary defintion.

To Do Items 
============

.. todo:: Understand how a role specifies a new CSS class. 
.. todo:: Understand how a directive specifies a new CSS class. How do I enable the user to specify the class of a directive?
.. todo:: Understand how a role is built. Many improvements can be made changing how Sphinx builds a directive/role in HTML and assigns CSS. For roles, the HTML is specified by the :code:`rawtext` parameter.
.. todo:: Understand how/when substitutions occur. May effect custom role builds.
.. todo:: Extend custom role to specify a unique CSS class.
.. todo:: Extend custom role to use JavaScript (if possible).

************************
Abbreviation-Based Role
************************
http://www.sphinx-doc.org/en/master/_modules/sphinx/addnodes.html#abbreviation

:abbr:`LIFO (last-in, first-out)`

:hover:`LIFO (last-in, first-out)`


.. code-block:: python

  class abbreviation(nodes.Inline, nodes.TextElement):
    """Node for abbreviations with explanations."""


Where is this from?

:file:`sphinx/roles.py`

.. code-block:: python
  :caption: sphinx/roles.py 
  :linenos:

  _abbr_re = re.compile(r'\((.*)\)$', re.S)
  
  
  def abbr_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
      # type: (unicode, unicode, unicode, int, Inliner, Dict, List[unicode]) -> Tuple[List[nodes.Node], List[nodes.Node]]  # NOQA
      text = utils.unescape(text)
      m = _abbr_re.search(text)  # type: ignore
      if m is None:
          return [addnodes.abbreviation(text, text, **options)], []
      abbr = text[:m.start()].strip()
      expl = m.group(1)
      options = options.copy()
      options['explanation'] = expl
      return [addnodes.abbreviation(abbr, abbr, **options)], []


First Attempt

WARNING: extension 'hover' has no setup() function; is it really a Sphinx extension module?

.. code-block:: python
  :caption: hover.py
  :linenos:

  from docutils import nodes
  import re
  
  
  hover_re = re.compile(r'\((.*)\)$', re.S)
  
  
  def hover_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
      # type: (unicode, unicode, unicode, int, Inliner, Dict, List[unicode]) -> Tuple[List[nodes.Node], List[nodes.Node]]  # NOQA
      text = utils.unescape(text)
      m = _hover_re.search(text)  # type: ignore
      if m is None:
          return [addnodes.hover-box(text, text, **options)], []
      abbr = text[:m.start()].strip()
      expl = m.group(1)
      options = options.copy()
      options['explanation'] = expl
      return [addnodes.hover-box(abbr, abbr, **options)], []


Second Attempt

.. code-block:: python
  :caption: Second Attempt 
  :linenos:

  register_generic_role('hover', nodes.abbr)

Third Attempt

.. code-block:: python
  :caption: Third Attempt
  :linenos:

  def rfc_reference_role(role, rawtext, text, lineno, inliner,
                       options={}, content=[]):
    try:
        rfcnum = int(text)
        if rfcnum <= 0:
            raise ValueError
    except ValueError:
        msg = inliner.reporter.error(
            'RFC number must be a number greater than or equal to 1; '
            '"%s" is invalid.' % text, line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    # Base URL mainly used by inliner.rfc_reference, so this is correct:
    ref = inliner.document.settings.rfc_base_url + inliner.rfc_url % rfcnum
    set_classes(options)
    node = nodes.reference(rawtext, 'RFC ' + utils.unescape(text), refuri=ref,
                           **options)
    return [node], []

register_canonical_role('rfc-reference', rfc_reference_role)



******************
Existing Term Role
******************

http://docutils.sourceforge.net/docutils/parsers/rst/states.py

.. code-block:: python

******************
Hover Role
******************

http://docutils.sourceforge.net/docs/howto/rst-roles.html

https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/

.. code-block:: python

  def hover_reference_role(role, rawtext, text, lineno, inliner,
              options={}, content=[]):
      code...
  
  # Set function attributes for customization:
  role_fn.options = ...
  role_fn.content = ...

  register_canonical_role();


**************
Hover Box HTML
**************

CSS-Only Version
================

https://stackoverflow.com/questions/10243440/how-to-create-a-box-when-mouse-over-text-in-pure-css

.. code-block:: html

  <a href="#" class="info"> Term  <span>Definition</span></a>

Or possibly

.. code-block:: html

  <a href="#" class="info"> Term  <span>|Definition|</span></a>

JavaScript
==================
Based on Google AdWords docs:

.. code-block:: html

  <p>This article explains how to edit your cost-per-click (CPC) bids and your <a class="glossary-term" data-answer="6026409" href="/adwords/answer/6026409" st-ve="40">cost-per-thousand viewable impressions</a> (viewable CPM) bids.</p>

The URL may point to a single page,  in which case, the role should be a variation of the :code:`doc` role.

**********
Resources
**********

.. seealso::

  - `Better Documentation Through Automation: Creating docutils and Sphinx Extensions <https://doughellmann.com/blog/2013/03/16/better-documentation-through-automation-creating-docutils-sphinx-extensions/>`_
  - `An idiot’s guide to Python documentation with Sphinx and ReadTheDocs <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`_
  - `Docutils Hacker's Guide <http://docutils.sourceforge.net/docs/dev/hacking.html>`_
  - `Creating reStructuredText Directives <http://docutils.sourceforge.net/docs/howto/rst-directives.html#specify-directive-arguments-options-and-content>`_
  - http://inside.mines.edu/~jrosenth/hacking-docutils.html
  - `Creating reStructuredText Interpreted Text Roles <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`_
  - `Gist <https://gist.github.com/shimizukawa/3718712>`_
  - `CSS Tooltip <https://www.w3schools.com/css/css_tooltip.asp>`_
  - `How to create a box when mouse over text in pure CSS? <https://stackoverflow.com/questions/10243440/how-to-create-a-box-when-mouse-over-text-in-pure-css>`_

