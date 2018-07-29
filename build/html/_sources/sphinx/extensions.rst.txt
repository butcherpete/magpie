.. include:: <isopub.txt>
 
#########################
Extensions 
#########################

An :term:`extension` is simply a Python module. When an extension is loaded, Sphinx imports this module and executes its setup() function, which in turn notifies Sphinx of everything the extension offers – see the extension tutorial for examples.

Sphinx is extensible at several levels:

- You can add new builders to support new output formats or actions on the parsed documents. 
- Then, it is possible to register custom reStructuredText roles and directives, extending the markup. 
- And finally, there are so-called “hook points” at strategic places throughout the build process, where an extension can register a hook and run specialized code.

- Implement extensions: http://www.sphinx-doc.org/en/master/develop.html
- Develop extensions: http://www.sphinx-doc.org/en/master/extdev/tutorial.html#exttut
