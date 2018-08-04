####################################
Tutorial: Writing a Simple Extension
####################################

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



