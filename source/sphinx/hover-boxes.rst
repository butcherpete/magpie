.. include:: <isopub.txt>

#########################
Glossary Hover Boxes 
#########################

**********
Goals
**********

**********
To Do List
**********

Test gist https://gist.github.com/shimizukawa/3718712 
Create custom role that copies the existing :code:`term` role.
Extend custom role to specify a unique CSS class.
Extend custom role to use JavaScript (if possible).
Define CSS class. 



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


*******************************
Defining Custom Roles in Sphinx
*******************************
https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/

**************************
Creating Custom Link Roles
**************************
http://protips.readthedocs.io/link-roles.html

The article describes a six-step process:

1. Create an :code:`_extensions` directory to hold extensions.
2. Add a custom search path in the :code:`conf.py` that includes the :code:`_extensions` directory.
3. Create the extension (:code:`bemuse.py`).
4. Add the extension to the  :code:`_extensions` directory. 
5. Add the extension to the :code:`extensions` list in the the :code:`conf.py`.
6 Mark up text using the custom roles.

**Directory Structure**

:tree:`assets` Image assets for use in the game.
  These assets can be referred from webpack code by ``require('assets/...')``.
:tree:`bin`
  Useful scripts for routine work.
  Examples include setting up Git commit hooks and releasing a new version.
:tree:`config`
  Configuration code for webpack and other things.

These three roles are rather limited:

- Each role links to a specific URL.
- Each role is defined by the :code:`reference` and :code:`external` classes.

**********
Resources
**********

-`An idiot’s guide to Python documentation with Sphinx and ReadTheDocs <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`_
- `Docutils Hacker's Guide <http://docutils.sourceforge.net/docs/dev/hacking.html>`_
- `Creating reStructuredText Directives <http://docutils.sourceforge.net/docs/howto/rst-directives.html#specify-directive-arguments-options-and-content>`_
- http://inside.mines.edu/~jrosenth/hacking-docutils.html
- `Creating reStructuredText Interpreted Text Roles <http://docutils.sourceforge.net/docs/howto/rst-roles.html>`_
- `Gist <https://gist.github.com/shimizukawa/3718712>`
