:date: 2018-09-02 
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
.. .. include:: /includes/include.txt

################
Themes Again
################

.. container:: abstract
 
  |greek|

********
Overview
********
- https://stackoverflow.com/questions/14622698/customize-sphinxdoc-theme
- https://github.com/sphinx-doc/sphinx/blob/master/doc/templating.rst 
- `Page-specific Template Overrides <https://stackoverflow.com/questions/13209597/override-html-page-template-for-a-specific-sphinx-document>`_


***********************
Extending Layout.html
***********************
https://ryan-roemer.github.io/sphinx-bootstrap-theme/

As a more “hands on” approach to customization, you can override any template in this Sphinx theme or any others. A good candidate for changes is “layout.html”, which provides most of the look and feel. 

First, take a look at the :code:`layout.html` file that the theme provides, and figure out what you need to override. As a side note, we have some theme-specific enhancements, such as the navbarextra template block for additional content in the navbar.

`sphinx-bootstrap-theme/bootstrap/layout.html <https://github.com/ryan-roemer/sphinx-bootstrap-theme/blob/master/sphinx_bootstrap_theme/bootstrap/layout.html>`_

Then, create your own :code:`_templates` directory and :code:`layout.html` file (assuming you build from a :code:`source` directory):

.. code-block:: bash 

  $ mkdir source/_templates
  $ touch source/_templates/layout.html

Then, configure your :code:`conf.py`:

.. code-block:: rst 

  templates_path = ['_templates']

Finally, edit your override file :code:`source/_templates/layout.html`:

.. code-block:: rst 

  {# Import the theme's layout. #}
  {% extends "!layout.html" %}
  
  {# Add some extra stuff before and use existing with 'super()' call. #}
  {% block footer %}
    <h2>My footer of awesomeness.</h2>
    {{ super() }}
  {% endblock %}


**************
Customizations
**************
http://jinja.pocoo.org/docs/2.10/templates/#template-objects

HTML Template
=============
.. code-block:: html

  {% extends layout_template %  }

RST Page
=============
http://www.sphinx-doc.org/en/stable/markup/misc.html#file-wide-metadata

.. code-block:: html

  :page_template: custom/index.html
  <your normal index.rst content>
  


.. seealso::
