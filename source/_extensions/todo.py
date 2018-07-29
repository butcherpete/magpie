#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tes <tes@C02T72XNG8WL-lm>
#
# Distributed under terms of the MIT license.

"""
We want the extension to add the following to Sphinx:

A “todo” directive, containing some content that is marked with “TODO”, and only shown in the output if a new config value is set. (Todo entries should not be in the output by default.)
A “todolist” directive that creates a list of all todo entries throughout the documentation.

http://www.sphinx-doc.org/en/master/extdev/tutorial.html
"""


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

"""
Node classes usually don’t have to do anything except inherit from the standard docutils classes defined in docutils.nodes. todo inherits from Admonition because it should be handled like a note or warning, todolist is just a “general” node.

Many extensions will not have to create their own node classes and work fine with the nodes already provided by docutils and Sphinx.

"""

from docutils import nodes

class todo(nodes.Admonition, nodes.Element):
    pass

class todolist(nodes.General, nodes.Element):
    pass

def visit_todo_node(self, node):
    self.visit_admonition(node)

def depart_todo_node(self, node):
    self.depart_admonition(node)


"""
A directive class is a class deriving usually from docutils.parsers.rst.Directive. The directive interface is also covered in detail in the docutils documentation; the important thing is that the class should have attributes that configure the allowed markup, and a run method that returns a list of nodes.

The todolist directive is quite simple:
"""

from docutils.parsers.rst import Directive

class TodolistDirective(Directive):

    def run(self):
        return [todolist('')]

"""
An instance of our todolist node class is created and returned. The todolist directive has neither content nor arguments that need to be handled.

The todo directive function looks like this:
"""

from sphinx.locale import _

class TodoDirective(Directive):

    # this enables content in the directive
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = "todo-%d" % env.new_serialno('todo')
        targetnode = nodes.target('', '', ids=[targetid])

        todo_node = todo('\n'.join(self.content))
        todo_node += nodes.title(_('Todo'), _('Todo'))
        self.state.nested_parse(self.content, self.content_offset, todo_node)

        if not hasattr(env, 'todo_all_todos'):
            env.todo_all_todos = []
        env.todo_all_todos.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'todo': todo_node.deepcopy(),
            'target': targetnode,
        })

        return [targetnode, todo_node]


"""
event handler
Since we store information from source files in the environment, which is persistent, it may become out of date when the source file changes. Therefore, before each source file is read, the environment’s records of it are cleared, and the env-purge-doc event gives extensions a chance to do the same. Here we clear out all todos whose docname matches the given one from the todo_all_todos list. If there are todos left in the document, they will be added again during parsing.

"""
def purge_todos(app, env, docname):
    if not hasattr(env, 'todo_all_todos'):
        return
    env.todo_all_todos = [todo for todo in env.todo_all_todos
                          if todo['docname'] != docname]

"""
event handler

This event is emitted at the end of phase 3 and allows custom resolving to be done:

It is a bit more involved. If our new “todo_include_todos” config value is false, all todo and todolist nodes are removed from the documents.

If not, todo nodes just stay where and how they are. Todolist nodes are replaced by a list of todo entries, complete with backlinks to the location where they come from. The list items are composed of the nodes from the todo entry and docutils nodes created on the fly: a paragraph for each entry, containing text that gives the location, and a link (reference node containing an italic node) with the backreference. The reference URI is built by app.builder.get_relative_uri which creates a suitable URI depending on the used builder, and appending the todo node’s (the target’s) ID as the anchor name.

"""

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
