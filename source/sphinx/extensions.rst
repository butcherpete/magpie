.. include:: <isopub.txt>
 
#########################
Extensions 
#########################

An :term:`extension` is simply a Python module. When an extension is loaded, Sphinx imports this module and executes its setup() function, which in turn notifies Sphinx of everything the extension offers – see the extension tutorial for examples.

Sphinx is extensible at several levels:

- You can add new builders to support new output formats or actions on the parsed documents. 
- Then, it is possible to register custom reStructuredText roles and directives, extending the markup. 
- And finally, there are so-called “hook points” at strategic places throughout the build process, where an extension can register a hook and run specialized code.
- When the extension is loaded, Sphinx imports this module and executes its :code:`setup()` function, which notifies Sphinx of everything the extension offers.
- The configuration file itself can be treated as an extension if it contains a setup() function. All other extensions to load must be listed in the `extensions configuration <http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions>` value.

************************************
Discovery of Builders by Entry Point
************************************
`Builder extensions <http://www.sphinx-doc.org/en/master/glossary.html#term-builder>` can be discovered by means of `entry points <https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins>` so that they do not have to be listed in the extensions configuration value.

Builder extensions should define an entry point in the :code:`sphinx.builders` group. The name of the entry point needs to match your builder’s name attribute, which is the name passed to the :code:`sphinx-build -b` option. The entry point value should equal the dotted name of the extension module. 

Here is an example of how an entry point for ‘mybuilder’ can be defined in the extension’s :code:`setup.py`:

.. code-block:: python

  setup(
      # ...
      entry_points={
          'sphinx.builders': [
              'mybuilder = my.extension.module',
          ],
      }
  )

Note that it is still necessary to register the builder using :code:`add_builder(`) in the extension’s :code:`setup(`) function.

******************
Extension Metadata
******************
The :code:`setup(`) function can return a dictionary. This is treated by Sphinx as metadata of the extension. Metadata keys currently recognized are:

:code:`version` 
  A string that identifies the extension version. It is used for extension version requirement checking (see `needs_extensions <http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-needs_extensions>`) and informational purposes. If not given, "unknown version" is substituted.

:code:`env_version` 
  An integer that identifies the version of env data structure if the extension stores any data to environment. It is used to detect the data structure has been changed from last build. The extensions have to increment the version when data structure has changed. If not given, Sphinx considers the extension does not stores any data to environment.

:code:`parallel_read_safe`
  A boolean that specifies if parallel reading of source files can be used when the extension is loaded. It defaults to :code:`False`, i.e. you have to explicitly specify your extension to be :code:`parallel-read-safe` after checking that it is.

:code:`parallel_write_safe`
  A boolean that specifies if parallel writing of output files can be used when the extension is loaded. Since extensions usually don’t negatively influence the process, this defaults to :code:`True`.


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


*********
Resources
*********

.. see also::

  - `Developing Extensions for Sphinx <http://www.sphinx-doc.org/en/master/extdev/index.html#dev-extensions>`
  - `The Docutils Document Tree: A Guide to the Docutils DTD <http://docutils.sourceforge.net/docs/ref/doctree.html>`_
