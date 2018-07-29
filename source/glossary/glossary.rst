.. include:: <isopub.txt>
 
.. include:: /includes/include.txt

########
Glossary
########

.. glossary::

  application
    The application object (usually called app) is an instance of Sphinx. It controls most high-level functionality, such as the setup of extensions, event dispatching and producing output (logging).

    If you have the environment object, the application is available as env.app.

  environment
    The build environment object (usually called env) is an instance of BuildEnvironment. It is responsible for parsing the source documents, stores all metadata about the document collection and is serialized to disk after each build.

    Its API provides methods to do with access to metadata, resolving references, etc. It can also be used by extensions to cache information that should persist for incremental rebuilds.

    If you have the application or builder object, the environment is available as app.env or builder.env.

  builder
    The builder object (usually called builder) is an instance of a specific subclass of Builder. Each builder class knows how to convert the parsed documents into an output format, or otherwise process them (e.g. check external links).

    If you have the application object, the builder is available as app.builder.

  config
    The config object (usually called config) provides the values of configuration values set in conf.py as attributes. It is an instance of Config.

    The config is available as app.config or env.config.

  extension
    An extension is simply a Python module. When an extension is loaded, Sphinx imports this module and executes its :code:`setup()` function, which in turn notifies Sphinx of everything the extension offers – see the extension tutorial for examples.    

  Sphin
    Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

  interpreted text
    Interpreted text is text that is meant to be related, indexed, linked, summarized, or otherwise processed, but the text itself is typically left alone. Interpreted text is enclosed by single backquote characters. http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#interpreted-text

  role
    Roles all have a common syntax, based on the interpreted text feature of reStructuredText. 

  role processor
    The docutils parser works by converting the input text to an internal tree representation made up of different types of nodes. The tree is traversed by a writer to create output in the desired format. To add a directive or role, you need to provide the hooks to be called to handle the markup when it is encountered in the input file. A role processor is defined with a function that takes arguments describing the marked-up text and returns the nodes to be included in the parse tree.

  RST
    |rst| is an easy-to-read, what-you-see-is-what-you-get plain text markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents. |rst| is designed for extensibility for specific application domains. The |rst| parser is a component of Docutils.

  Sublime Text
    Sublime Text is a sophisticated text editor for code, markup and prose. You'll love the slick user interface, extraordinary features and amazing performance.

  template 
    Sphinx supports changing the appearance of its HTML output via themes. A theme is a collection of HTML templates, stylesheet(s) and other static files. Additionally, it has a configuration file which specifies from which theme to inherit, which highlighting style to use, and what options exist for customizing the theme’s look and feel.

  theme
    Sphinx supports changing the appearance of its HTML output via themes. A theme is a collection of HTML templates, stylesheet(s) and other static files. Additionally, it has a configuration file which specifies from which theme to inherit, which highlighting style to use, and what options exist for customizing the theme’s look and feel.
