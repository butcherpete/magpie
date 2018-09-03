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
***********
Layout HTML
***********

Finally, edit your override file :code:`source/_templates/layout.html`:

.. code-block:: py

  {% extends "basic/layout.html" %}
  
  {% if theme_bootstrap_version == "3" %}
    {% set bootstrap_version, navbar_version = "3.3.7", "" %}
    {% set bs_span_prefix = "col-md-" %}
  {% else %}
    {% set bootstrap_version, navbar_version = "2.3.2", "-2" %}
    {% set bs_span_prefix = "span" %}
  {% endif %}
  
  {% set script_files = script_files + [
      '_static/js/jquery-1.11.0.min.js',
      '_static/js/jquery-fix.js',
      '_static/bootstrap-' + bootstrap_version + '/js/bootstrap.min.js',
      '_static/bootstrap-sphinx.js'
    ]
  %}
  
  {%- set render_sidebar = (not embedded) and (not theme_nosidebar|tobool) and sidebars %}
  
  {%- set bs_content_width = render_sidebar and "9" or "12"%}
  
  {%- block doctype -%}
  <!DOCTYPE html>
  {%- endblock %}
  
  {# Sidebar: Rework into our Bootstrap nav section. #}
  {% macro navBar() %}
  {% include "navbar" + navbar_version + ".html" %}
  {% endmacro %}
  
  {% if theme_bootstrap_version == "3" %}
    {%- macro bsidebar() %}
        {%- if render_sidebar %}
        <div class="{{ bs_span_prefix }}3">
          <div id="sidebar" class="bs-sidenav" role="complementary">
            {%- for sidebartemplate in sidebars %}
              {%- include sidebartemplate %}
            {%- endfor %}
          </div>
        </div>
        {%- endif %}
    {%- endmacro %}
  {% else %}
    {%- macro bsidebar() %}
        {%- if render_sidebar %}
        <div class="{{ bs_span_prefix }}3">
          <div id="sidebar" class="bs-sidenav well" data-spy="affix">
            {%- for sidebartemplate in sidebars %}
              {%- include sidebartemplate %}
            {%- endfor %}
          </div>
        </div>
        {%- endif %}
    {%- endmacro %}
  {% endif %}
  
  {%- block extrahead %}
  <meta charset='utf-8'>
  <meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1'>
  <meta name="apple-mobile-web-app-capable" content="yes">
  {% endblock %}
  
  {# Silence the sidebar's, relbar's #}
  {% block header %}{% endblock %}
  {% block relbar1 %}{% endblock %}
  {% block relbar2 %}{% endblock %}
  {% block sidebarsourcelink %}{% endblock %}
  
  {%- block content %}
  {{ navBar() }}
  <div class="container">
    <div class="row">
      {%- block sidebar1 %}{{ bsidebar() }}{% endblock %}
      <div class="{{ bs_span_prefix }}{{ bs_content_width }} content">
        {% block body %}{% endblock %}
      </div>
      {% block sidebar2 %} {# possible location for sidebar #} {% endblock %}
    </div>
  </div>
  {%- endblock %}
  
  {%- block footer %}
  <footer class="footer">
    <div class="container">
      <p class="pull-right">
        <a href="#">Back to top</a>
        {% if theme_source_link_position == "footer" %}
          <br/>
          {% include "sourcelink.html" %}
        {% endif %}
      </p>
      <p>
      {%- if show_copyright %}
        {%- if hasdoc('copyright') %}
          {% trans path=pathto('copyright'), copyright=copyright|e %}&copy; <a href="{{ path }}">Copyright</a> {{ copyright }}.{% endtrans %}<br/>
        {%- else %}
          {% trans copyright=copyright|e %}&copy; Copyright {{ copyright }}.{% endtrans %}<br/>
        {%- endif %}
      {%- endif %}
      {%- if last_updated %}
        {% trans last_updated=last_updated|e %}Last updated on {{ last_updated }}.{% endtrans %}<br/>
      {%- endif %}
      {%- if show_sphinx %}
        {% trans sphinx_version=sphinx_version|e %}Created using <a href="http://sphinx-doc.org/">Sphinx</a> {{ sphinx_version }}.{% endtrans %}<br/>
      {%- endif %}
      </p>
    </div>
  </footer>
  {%- endblock %}


.. seealso::
