.. include:: <isopub.txt>
 
#########################
Custom Roles 
#########################

**********
Goals
**********
Define custom roles.

Text line.

To Do List
==========

|check| `Creating Custom Link Roles <http://protips.readthedocs.io/link-roles.html>`_

|check| Test gist https://gist.github.com/shimizukawa/3718712 

- Create custom role that copies the existing :code:`term` role.


************************
Define the Role Function
************************
http://docutils.sourceforge.net/docs/howto/rst-roles.html

The role function creates and returns inline elements (nodes) and does
any additional processing required.  Its signature is as follows:

.. code-block:: python
  :caption: role signature
  :linenos:

    def role_fn(name, rawtext, text, lineno, inliner,
                options={}, content=[]):
        code...

    # Set function attributes for customization:
    role_fn.options = ...
    role_fn.content = ...

The role function parameters are as follows:

* ``name``: The local name of the interpreted role, the role name
  actually used in the document.

* ``rawtext``: A string containing the enitre interpreted text input,
  including the role and markup.  Return it as a ``problematic`` node
  linked to a system message if a problem is encountered.

* ``text``: The interpreted text content.

* ``lineno``: The line number where the interpreted text begins.

* ``inliner``: The ``docutils.parsers.rst.states.Inliner`` object that
  called role_fn.  It contains the several attributes useful for error
  reporting and document tree access.

* ``options``: A dictionary of directive options for customization
  (from the `"role" directive`_), to be interpreted by the role
  function.  Used for additional attributes for the generated elements
  and other functionality.

* ``content``: A list of strings, the directive content for
  customization (from the `"role" directive`_).  To be interpreted by
  the role function.

Role functions return a tuple of two values:

* A list of nodes which will be inserted into the document tree at the
  point where the interpreted role was encountered (can be an empty
  list).

* A list of system messages, which will be inserted into the document tree
  immediately after the end of the current block (can also be empty).

****************************
Generic Cross Reference Role
****************************
A generic cross-reference role.

https://github.com/sphinx-doc/sphinx/blob/master/sphinx/roles.py

.. code-block:: python
  :caption: :code:`XRefRole(object)` class in :file:`roles.py`
  :linenos:

  class XRefRole(object):
      """
      A generic cross-referencing role.  To create a callable that can be used as
      a role function, create an instance of this class.
      The general features of this role are:
      * Automatic creation of a reference and a content node.
      * Optional separation of title and target with `title <target>`.
      * The implementation is a class rather than a function to make
        customization easier.
      Customization can be done in two ways:
      * Supplying constructor parameters:
        * `fix_parens` to normalize parentheses (strip from target, and add to
          title if configured)
        * `lowercase` to lowercase the target
        * `nodeclass` and `innernodeclass` select the node classes for
          the reference and the content node
      * Subclassing and overwriting `process_link()` and/or `result_nodes()`.
      """
  
      nodeclass = addnodes.pending_xref  # type: Type[nodes.Node]
      innernodeclass = nodes.literal
  
      def __init__(self, fix_parens=False, lowercase=False,
                   nodeclass=None, innernodeclass=None, warn_dangling=False):
          # type: (bool, bool, Type[nodes.Node], Type[nodes.Node], bool) -> None
          self.fix_parens = fix_parens
          self.lowercase = lowercase
          self.warn_dangling = warn_dangling
          if nodeclass is not None:
              self.nodeclass = nodeclass
          if innernodeclass is not None:
              self.innernodeclass = innernodeclass
  
      def _fix_parens(self, env, has_explicit_title, title, target):
          # type: (BuildEnvironment, bool, unicode, unicode) -> Tuple[unicode, unicode]
          if not has_explicit_title:
              if title.endswith('()'):
                  # remove parentheses
                  title = title[:-2]
              if env.config.add_function_parentheses:
                  # add them back to all occurrences if configured
                  title += '()'
          # remove parentheses from the target too
          if target.endswith('()'):
              target = target[:-2]
          return title, target
  
      def __call__(self, typ, rawtext, text, lineno, inliner,
                   options={}, content=[]):
          # type: (unicode, unicode, unicode, int, Inliner, Dict, List[unicode]) -> Tuple[List[nodes.Node], List[nodes.Node]]  # NOQA
          env = inliner.document.settings.env
          if not typ:
              typ = env.temp_data.get('default_role')
              if not typ:
                  typ = env.config.default_role
              if not typ:
                  raise SphinxError('cannot determine default role!')
          else:
              typ = typ.lower()
          if ':' not in typ:
              domain, role = '', typ  # type: unicode, unicode
              classes = ['xref', role]
          else:
              domain, role = typ.split(':', 1)
              classes = ['xref', domain, '%s-%s' % (domain, role)]
          # if the first character is a bang, don't cross-reference at all
          if text[0:1] == '!':
              text = utils.unescape(text)[1:]
              if self.fix_parens:
                  text, tgt = self._fix_parens(env, False, text, "")
              innernode = self.innernodeclass(rawtext, text, classes=classes)
              return self.result_nodes(inliner.document, env, innernode,
                                       is_ref=False)
          # split title and target in role content
          has_explicit_title, title, target = split_explicit_title(text)
          title = utils.unescape(title)
          target = utils.unescape(target)
          # fix-up title and target
          if self.lowercase:
              target = target.lower()
          if self.fix_parens:
              title, target = self._fix_parens(
                  env, has_explicit_title, title, target)
          # create the reference node
          refnode = self.nodeclass(rawtext, reftype=role, refdomain=domain,
                                   refexplicit=has_explicit_title)
          # we may need the line number for warnings
          set_role_source_info(inliner, lineno, refnode)  # type: ignore
          title, target = self.process_link(
              env, refnode, has_explicit_title, title, target)
          # now that the target and title are finally determined, set them
          refnode['reftarget'] = target
          refnode += self.innernodeclass(rawtext, title, classes=classes)
          # we also need the source document
          refnode['refdoc'] = env.docname
          refnode['refwarn'] = self.warn_dangling
          # result_nodes allow further modification of return values
          return self.result_nodes(inliner.document, env, refnode, is_ref=True)
  
      # methods that can be overwritten
  
      def process_link(self, env, refnode, has_explicit_title, title, target):
          # type: (BuildEnvironment, nodes.reference, bool, unicode, unicode) -> Tuple[unicode, unicode]  # NOQA
          """Called after parsing title and target text, and creating the
          reference node (given in *refnode*).  This method can alter the
          reference node and must return a new (or the same) ``(title, target)``
          tuple.
          """
          return title, ws_re.sub(' ', target)
  
      def result_nodes(self, document, env, node, is_ref):
          # type: (nodes.document, BuildEnvironment, nodes.Node, bool) -> Tuple[List[nodes.Node], List[nodes.Node]]  # NOQA
          """Called before returning the finished nodes.  *node* is the reference
          node if one was created (*is_ref* is then true), else the content node.
          This method can add other nodes and must return a ``(nodes, messages)``
          tuple (the usual return value of a role function).
          """
          return [node], []



Two modes of customization:

- What does it mean to supply constructor parameters?
- What does it mean to subclass and overwrite the :code:`process_link()` and :code:`result_nodes()` metric.


************************************
Tutorial: Writing a Simple Extension
************************************
http://www.sphinx-doc.org/en/1.5.1/extdev/tutorial.html

.. code-block:: python
  :caption: todo.py
  :linenos:

  def setup(app):
  app.add_config_value('todo_include_todos', False, 'html')

  app.add_node(todolist)
  app.add_node(todo,
               html=(visit_todo_node, depart_todo_node),
               latex=(visit_todo_node, depart_todo_node),
               text=(visit_todo_node, depart_todo_node))

  app.add_directive('todo', TodoDirective)
  app.add_directive('todolist', TodolistDirective)
  app.connect('doctree-resolved', process_todo_nodes)
  app.connect('env-purge-doc', purge_todos)

  return {'version': '0.1'}   # identifies the version of our extension



*******************
Better Custom Roles
*******************
http://inside.mines.edu/~jrosenth/hacking-docutils.html#quick-dirty-custom-roles


.. code-block:: python
  :caption: slides.py
  :linenos:

  import docutils.parsers.rst as rst
  import docutils.nodes as nodes
  
  def slides_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
      with open('source/slides/{}.rst'.format(text)) as f:
          title = f.readline().strip()
      return [
          nodes.reference(rawtext, title, refuri='/slides/{}.html'.format(text), internal=True),
          nodes.Text(', ('),
          nodes.reference(rawtext, '4:3 PDF', refuri='/_static/slides/{}-43.pdf'.format(text), internal=True, newtab=True),
          nodes.Text(', '),
          nodes.reference(rawtext, '16:9 PDF', refuri='/_static/slides/{}-169.pdf'.format(text), internal=True, newtab=True),
          nodes.Text(', '),
          nodes.reference(rawtext, '16:10 PDF', refuri='/_static/slides/{}-1610.pdf'.format(text), internal=True, newtab=True),
          nodes.Text(')'),
      ], []
  rst.roles.register_local_role('slides', slides_role)


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

In Use
======
These three roles (:code:`github`, :code:`module`, and :code:`tree`) are rather limited:

- Each role links to a specific URL.
- Each role is defined by the :code:`reference` and :code:`external` classes.

.. code-block:: rest
  :caption: bemuse.py roles markup
  
  :tree:`assets` Image assets for use in the game.
    These assets can be referred from webpack code by ``require('assets/...')``.
  :tree:`bin`
    Useful scripts for routine work.
    Examples include setting up Git commit hooks and releasing a new version.
  :tree:`config`
    Configuration code for webpack and other things.

Which are rendered as:

:tree:`assets` Image assets for use in the game.
  These assets can be referred from webpack code by ``require('assets/...')``.
:tree:`bin`
  Useful scripts for routine work.
  Examples include setting up Git commit hooks and releasing a new version.
:tree:`config`
  Configuration code for webpack and other things.


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


An example in use:

This is an :strike:`example of a strikethrough`.

This is an :red:`example of a red text highlight`.

**********
Resources
**********

- http://www.sphinx-doc.org/en/stable/templating.html#script_files
- https://github.com/ryan-roemer/sphinx-bootstrap-theme
