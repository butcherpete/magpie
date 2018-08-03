.. include:: <isopub.txt>
 
#########################
Custom Roles 
#########################

**********
Goals
**********
Define custom directives and roles. 

To Do List
==========

|check| `Creating Custom Link Roles <http://protips.readthedocs.io/link-roles.html>`_

- Test gist https://gist.github.com/shimizukawa/3718712 
- Create custom role that copies the existing :code:`term` role.


******************
Underlying Objects
******************

:code:`XRefRole(object)` class in :file:`roles.py`

.. code-block:: python

  A generic cross-referencing role.  To create a callable that can be used as a role function, create an instance of this class.
  
  The general features of this role are:
  
  * Automatic creation of a reference and a content node.
  * Optional separation of title and target with `title <target>`.
  * The implementation is a class rather than a function to make customization easier.
  
  Customization can be done in two ways:
  
  * Supplying constructor parameters:
  
    * `fix_parens` to normalize parentheses (strip from target, and add to title if configured)
    * `lowercase` to lowercase the target
    * `nodeclass` and `innernodeclass` select the node classes for the reference and the content node
  
  * Subclassing and overwriting `process_link()` and/or `result_nodes()`.


Two modes of customization:

- What does it mean to supply constructor parameters?
- What does it mean to subclass and overwrite the :code:`process_link()` and :code:`result_nodes()` metric.




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
6. Mark up text using the custom roles.


.. code-block:: python
  :caption: conf.py

  sys.path.insert(0, os.path.abspath('.') + '/_extensions')

  extensions = [
      'sphinx.ext.autodoc',
      'sphinx.ext.doctest',
      'sphinx.ext.intersphinx',
      'sphinx.ext.todo',
      'sphinx.ext.coverage',
      'sphinx.ext.mathjax',
      'sphinx.ext.ifconfig',
      'sphinx.ext.viewcode',
      'sphinx.ext.githubpages',
      'bemuse'
  ]

.. code-block:: python
  :caption: bemuse.py

  from docutils import nodes
  
  def setup(app):
      app.add_role('github', autolink('https://github.com/%s'))
      app.add_role('module', autolink('https://github.com/bemusic/bemuse/tree/master/src/%s'))
      app.add_role('tree', autolink('https://github.com/bemusic/bemuse/tree/master/%s'))
  
  def autolink(pattern):
      def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
          url = pattern % (text,)
          node = nodes.reference(rawtext, text, refuri=url, **options)
          return [node], []
      return role



..
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

******************************************
Define Original Roles and Styles in Sphinx
******************************************

https://gist.github.com/shimizukawa/3718712

Register the role:

.. code-block:: python
  :caption: conf.py

  sys.path += ['.']
  extensions += ['sphinxcontrib_roles']
  
  # configuration case.1: define roles as list (define only roles)
  roles = ['strike', 'red']
  
  
  # configuration case.2: define roles as dict (define roles and its style on HTML)
  roles = {'strike': "text-decoration: line-through;",
           'red': "color: red;" }

Define the role. 

.. code-block:: python
  :caption: sphinxcontrib_roles.py

  # -*- coding: utf-8 -*-
  import os
  from docutils.parsers.rst import roles
  
  
  def _define_role(name):
      base_role = roles.generic_custom_role
      role = roles.CustomRole(name, base_role, {'class': [name]}, [])
  
      roles.register_local_role(name, role)
  
  
  def on_builder_inited(app):
      for name in app.builder.config.roles:
          _define_role(name)
  
  
  def on_html_collect_pages(app):
      if isinstance(app.builder.config.roles, dict) and app.builder.config.roles:
          cssdir = os.path.join(app.builder.outdir, '_static')
          cssfile = os.path.join(cssdir, 'roles.css')
          if not os.path.exists(cssdir):
              os.makedirs(cssdir)
  
          fd = open(cssfile, 'wt')
          for name, style in app.builder.config.roles.items():
              fd.write("span.%s { %s }\n" % (name, style))
          fd.close()
             
      return ()
  
  
  def html_page_context(app, pagename, templatename, context, doctree):
      if isinstance(app.builder.config.roles, dict) and app.builder.config.roles:
          if 'css_files' in context:
              context['css_files'].append('_static/roles.css')
  
  
  def setup(app):
      app.add_config_value('roles', [], 'html')
      app.connect("builder-inited", on_builder_inited)
      app.connect("html-collect-pages", on_html_collect_pages)
      app.connect("html-page-context", html_page_context)

**********
Resources
**********

- http://www.sphinx-doc.org/en/stable/templating.html#script_files
- https://github.com/ryan-roemer/sphinx-bootstrap-theme
