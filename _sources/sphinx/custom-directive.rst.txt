.. include:: <isopub.txt>

#########################
Custom Directives 
#########################

- Many extensions will not have to create their own node classes and work fine with the nodes already provided by docutils and Sphinx.

**********
Goals
**********
Define custom directives and roles. 

|check| Add links to documenation.

- Do Sphinx tutorial: `Tutoral: Writing a Simple Extension <http://www.sphinx-doc.org/en/master/extdev/tutorial.html>`_.



****************
To Do  Tutorial
****************

Setup Function
==============

- Add new module named :file:`todo.py`. Where is this module/file saved?

.. code-block:: python

  def setup(app):
      app.add_config_value('todo_include_todos', False, 'html')
  
      app.add_node(todolist)
      app.add_node(todo, html=(visit_todo_node, depart_todo_node), latex=(visit_todo_node, depart_todo_node), text=(visit_todo_node, depart_todo_node))
  
      app.add_directive('todo', TodoDirective)
      app.add_directive('todolist', TodolistDirective)
      app.connect('doctree-resolved', process_todo_nodes)
      app.connect('env-purge-doc', purge_todos)
  
      return {'version': '0.1'}   # identifies the version of our extension

**********
Resources
**********

.. seealso::

  - `Developing Extensions for Sphinx <http://www.sphinx-doc.org/en/master/extdev/index.html>`_
  - `Tutorial: Writing a simple extension <http://www.sphinx-doc.org/en/master/extdev/tutorial.html>`_
  - `Application API <http://www.sphinx-doc.org/en/master/extdev/appapi.html>`_
  - http://www.sphinx-doc.org/en/stable/templating.html#script_files
