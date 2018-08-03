.. include:: <isopub.txt>
 
#########################
Glossary Hover Boxes 
#########################

**********
Goals
**********
Identify and implement a role-based glossary term solution that using CSS-based hover boxes to display glossary term definitions. The solution with include custom roles, css, and possibility custom JS.

Two options:

- A role based on the existing :code:`abbr` role. The author must specify text or a variable in the role defintion. The hover box is defined in CSS and not as a HTML tool-tip.
- A role based on the existing :code:`term` role. The role creates a reference to the glossary definition that is handled with as a CSS hover box. Woud require JavaScript.

Worth research:

- http://docutils.sourceforge.net/docutils/parsers/rst/roles.py
- The term role may be built in the Sphinx glossary defintion.

**********
To Do List
**********

- Understand how a role specifies a new CSS class.
- Understand how a role is built. Many improvements  can be made changing how Sphinx builds a directive/role in HTML and assigns CSS.
- Understand how/when substitutions occur. May effect custom role builds.
- Extend custom role to specify a unique CSS class.
- Extend custom role to use JavaScript (if possible).
- Define CSS class. 

******************
Existing Abbr Role
******************

:file:`sphinx/roles.py`

.. code-block:: python

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


:abbr:`LIFO (last-in, first-out)`

:hover:`LIFO (last-in, first-out)`


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



**********
Resources
**********
- `Better Documentation Through Automation: Creating docutils and Sphinx Extensions <https://doughellmann.com/blog/2013/03/16/better-documentation-through-automation-creating-docutils-sphinx-extensions/>`_
- `An idiot’s guide to Python documentation with Sphinx and ReadTheDocs <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`_
- `Docutils Hacker's Guide <http://docutils.sourceforge.net/docs/dev/hacking.html>`_
- `Creating reStructuredText Directives <http://docutils.sourceforge.net/docs/howto/rst-directives.html#specify-directive-arguments-options-and-content>`_
- http://inside.mines.edu/~jrosenth/hacking-docutils.html
- `Creating reStructuredText Interpreted Text Roles <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`_
- `Gist <https://gist.github.com/shimizukawa/3718712>`
