:date: 2018-09-14 
:version: 1
:author: tes 
:information-type: api 
:platform: demand
:product: |api|
:description: |greek| 
:audience: external
:tags: tag1, tag2, tag3 
:keywords: keyword1, keyword2, keyword3 
:languages: english
:orphan:
:nocomments:

.. include:: /includes/include.txt

################
Handlebars Notes
################

.. container:: abstract
 
  |greek|

********
Overview
********

- Handlebars.js was developed by the same people who are behind Ember.js
- Handlebars.js is based on Mustache. 

Handlebars.js adds a couple of additional features to make writing templates easier and also changes a tiny detail of how partials work.

- Nested Paths
- Helpers
- Block Expressions
- Literal Values
- Delimited Comments


***********
Expressions
***********
- Dynamic elements are called :emphasis:`expressions`

- simple expressions that represent dynamic values. "Simple expressions are identifiers that tell Handlebars.js which variable to use to replace the template contents at runtime."
- block expressions that contain logic

Simple Expressions
==================

Block Expressions
=================

"A block expression has not only a value but also a body that can contain plain markup, simple expressions, or even other block expressions. 

Handlebars.js identifies a block expression by its prepending pound, or hash, symbol (#). 
- # A # preceeding the helper name 
- / A closing mustache, /, of the same name. The block expression ends by prepending a backslash (/) to the ending block helper. 
  
"Anything that’s listed between the start and end tag is part of the block expression and builds up the block expression’s body."

Built-in Block Expressions
==========================

- :code:`{{each}}`: Iterates over an array of items and generates a template for each item inside the array,
- :code:`{{if}}`: Evaluates the value of a single parameter to determine whether the body of the expression is rendered. 
- :code:`{{if-else}}` The :code:`{{else}}` expression doesn’t start with a hash symbol because that expression is part of the :code:`{{if}}` expression.
- :code:`{{unless}}`: Evaluates the value of a single parameter to determine whether the body of the expression is rendered.
- :code:`{{with}}`:  Shortens the paths for each of the expressions inside the :code:`{{with}}` block, whcih enables you define long, complex paths.
- :code:`{{comments}}`

Ember.js Block Expressions
==========================

- :code:`{{view}}`
- :code:`{{bind-attr}}`
- :code:`{{action}}`
- :code:`{{outlet}}`
- :code:`{{unbound}}`
- :code:`{{partial}}`
- :code:`{{link-to}}`
- :code:`{{render}}`
- :code:`{{control}}`
- :code:`{{input}}`
- :code:`{{textarea}}`
- :code:`{{yield}}`



**************
Precompilation
**************

*********
Execution
*********

*************
HTML Escaping
*************

****************
Handlebars Paths
****************

*****************
Template Comments
*****************


********
Literals 
********

********
Partials
********
http://handlebarsjs.com/partials.html

Handlebars allows for template reuse through partials. Partials are normal Handlebars templates that may be called directly by other templates.

In order to use a partial, it must be registered via :code:`Handlebars.registerPartial`.

.. code-block:: js

  Handlebars.registerPartial('myPartial', '{{name}}')

This call will register the  :code:`myPartial` partial. Partials may be precompiled and the precompiled template passed into the second parameter.
 
Calling the partial is done through the partial call syntax:

.. code-block:: js

  {{> myPartial }}

.. seealso::
