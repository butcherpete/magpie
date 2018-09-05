.. include:: <isopub.txt>
 
########
Metadata
########

********
Overview
********

*********************
Build Environment API
*********************
http://www.sphinx-doc.org/en/stable/markup/misc.html#metadata

.. code-block:: py

  class.sphinx.environment.BuildEnviroment

metdata
  Dictionary mapping docnames to metadata.

File metadata is stored in :code:`env.metadata[docname]` and :code:`doctree[0]`.

*********************
File-Wide Metadata
*********************

http://www.sphinx-doc.org/en/stable/markup/misc.html#metadata

  A field list near the top of a file is parsed by docutils as the :emphasis:`docinfo`, which is normally used to record the author, date of publication, and other metadata. 

  In Sphinx, a field list preceding any other markup is moved from the docinfo to the Sphinx environment as document metadata and is not displayed in the output; a field list appearing after the document title will be part of the docinfo as normal and will be displayed in the output.
  
  At the moment, these metadata fields are recognized:
  
  tocdepth
    The maximum depth for a table of contents of this file.
  
  nocomments
    If set, the web application won’t display a comment form for a page generated from this source file.

  orphan
    If set, warnings about this file not being included in any toctree will be suppressed.


***********
To Do Items
***********
.. todo:: Learn to parse metadata
.. todo:: Learn to generate tags
