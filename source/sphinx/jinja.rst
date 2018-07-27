#########################
Jinja Templates 
#########################

http://www.sphinx-doc.org/en/stable/templating.html#script_files


*************************
Multiple Template Support
*************************

See http://www.sphinx-doc.org/en/stable/config.html#html-options 

:code:`html_additional_pages`

Additional templates that should be rendered to HTML pages, must be a dictionary that maps document names to template names.

.. code-block:: rest

  html_additional_pages = {
      'download': 'customdownload.html',
  }

This will render the template customdownload.html as the page download.html.
