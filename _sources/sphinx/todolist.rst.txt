####################################
Tutorial: Writing a Simple Extension
####################################

http://www.sphinx-doc.org/en/1.5.1/extdev/tutorial.html

*****************
Important Objects
*****************
Key APIs used to write extensions:

.. list-table:: Important Objects
  :header-rows: 1

  * - Object
    - Definition
    - API
  * - Application
    - An instance of Sphinx. It controls high-level functionality, such as setup of extentions, event dispatching, and logging. 
    - :code:`env.app` 
  * - Environment
    - An instance of :code:`BuildEnvironment`.  Parses the source documents, stores all metadata about the document collection and is serialized to disk after each build.

      Its API provides methods to do with access to metadata, resolving references, etc. It can also be used by extensions to cache information that should persist for incremental rebuilds. To learn more, see `Builder API <http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx>`_

    - :code:`app.env`, :code:`builder.env` 
  * - Builder
    - An instance of a specific subclass of :code:`Builder`. Each builder class knows how to convert the parsed documents into an output format, or otherwise process them (e.g. check external links). To learn more, see `Builder API <http://www.sphinx-doc.org/en/master/extdev/builderapi.html#sphinx.builders.Builder>`_
    - :code:`app.builder` 
  * - Config
    - An instance of :code:`Config`. The :code:`config` object makes the values of alll config values available as attributes. 
      
      It is exposed via the :code:`sphinx.application.Application.config` and :code:`sphinx.environment.Environment.config` attributes. For example, to get the value of language, use either :code:`app.config.language` or :code:`env.config.language`.  
    - :code:`app.config`, :code:`env.config` 

.. code-block:: python
  :caption: todo.py
  :linenos:


  """"
  Setup function
  """"

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

  """"
  Node classes
  """"

  from docutils import nodes

  class todo(nodes.Admonition, nodes.Element):
    pass

  class todolist(nodes.General, nodes.Element):
    pass

  def visit_todo_node(self, node):
      self.visit_admonition(node)
  
  def depart_todo_node(self, node):
    self.depart_admonition(node)

  """"
  Directive classes

  A directive class is a class deriving usually from docutils.parsers.rst.Directive. The directive interface is also covered in detail in the docutils documentation; the important thing is that the class should have attributes that configure the allowed markup, and a run method that returns a list of nodes.
  """"


  """"
  todolist node
  """"

  from docutils.parsers.rst import Directive

  class TodolistDirective(Directive):
  
      def run(self):
          return [todolist('')]

  """"
  todo node
  """"

  from sphinx.util.compat import make_admonition
  from sphinx.locale import _
  
  class TodoDirective(Directive):
  
      # this enables content in the directive
      has_content = True
  
      def run(self):
          env = self.state.document.settings.env
  
          targetid = "todo-%d" % env.new_serialno('todo')
          targetnode = nodes.target('', '', ids=[targetid])
  
          ad = make_admonition(todo, self.name, [_('Todo')], self.options,
                               self.content, self.lineno, self.content_offset,
                               self.block_text, self.state, self.state_machine)
  
          if not hasattr(env, 'todo_all_todos'):
              env.todo_all_todos = []
          env.todo_all_todos.append({
              'docname': env.docname,
              'lineno': self.lineno,
              'todo': ad[0].deepcopy(),
              'target': targetnode,
          })
  
          return [targetnode] + ad
  
  """"
  Event handlers
  """"
  
  """"
  env-purge-doc event
  """"
  
  def purge_todos(app, env, docname):
      if not hasattr(env, 'todo_all_todos'):
          return
      env.todo_all_todos = [todo for todo in env.todo_all_todos
                            if todo['docname'] != docname]

  
  """"
  doctree-resolved event
  """"

  def process_todo_nodes(app, doctree, fromdocname):
    if not app.config.todo_include_todos:
        for node in doctree.traverse(todo):
            node.parent.remove(node)

    # Replace all todolist nodes with a list of the collected todos.
    # Augment each todo with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(todolist):
        if not app.config.todo_include_todos:
            node.replace_self([])
            continue

        content = []

        for todo_info in env.todo_all_todos:
            para = nodes.paragraph()
            filename = env.doc2path(todo_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, todo_info['lineno']))
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = todo_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, todo_info['docname'])
            newnode['refuri'] += '#' + todo_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # Insert into the todolist
            content.append(todo_info['todo'])
            content.append(para)

        node.replace_self(content)

