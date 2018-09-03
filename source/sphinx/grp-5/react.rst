#####################################
Adaptive Modern Product Documentation
#####################################

.. highlights::

  - https://hackernoon.com/adaptive-modern-product-documentation-7d792fd8696d
  - https://gist.github.com/hishnash/933ce146289faf88dd633c249eb5f228

********
Overview
********

- Combines Sphinx and React
- Use custom directives
- Builds pages dynamically based on the AST (abstract syntax tree): "Within our documentation, we have many cases where we have used custom directives to drive unique UI and logical components."

*****************
Custom Directives
*****************

"Sphinx refers to these nested objects as directives each one can take some options and child content." 

There the are four different custom directives in use:

- :code:`tab`
- :code:`dv` (dynamic value) this expects two child components that subclass our custom :code:`tab` directive.
- :code:`dvvis` is the directive that manages the visual tab (seen on the left below), this expects a figure.
- :code:`dvspec` is a more complex tab component that is rendered on the right below.

"Within our documentation, we have many cases where we have used custom directives to drive unique UI and logical components."

"Each such directive can take some custom config that is used to manages its rendering. As an example below is the source for our HMAC dynamic value."

.. code-block:: rest

  .. dv:: URL Encoding
      :keywords: url-encoding
  
      .. dvvis:: Visual
  
          .. figure:: /Images/encoding_crypto/URLEncodingDynamicValue.png
  
              A `Percent-encoding <http://en.wikipedia.org/wiki/Percent-encoding>`_ converter conforming to `RFC3986 <http://tools.ietf.org/html/rfc3986>`_.
  
      .. dvspec:: Code
          :identifier: com.luckymarmot.URLEncodingDynamicValue
  
          .. arg:: input
              :type: DynamicString
  
              Text input to be encoded/decoded.
  
          .. arg:: charset
              :type: string
              :default: ``utf-8``
  
              Charset to be used.
  
          .. arg:: mode
              :type: number
              :default: ``0`` (Encode)
  
              Operation mode (0: Encode, 1: Decode).
  
          .. code-block:: javascript
  
              function evaluate(context){
                  var dv = new DynamicValue('com.luckymarmot.URLEncodingDynamicValue', {
                      'input': 'Something to be URL-encoded'
                  });
                  return dv.getEvaluatedString();
              };


**************
Tabs Directive
**************
Above we have looked at a few custom directives, but how do we set up these Sphinx extensions.

.. code-block:: python
  :caption: tab.py
  :linenos:

  class TabSection(Directive):
      has_content = True  # this directive can have children
      required_arguments = 1  # has 1 arg
      optional_arguments = 0
      
       # add a kwarg `keyworks` these are used for search
      option_spec = {'keywords': directives.unchanged} 
      
      # we need a new line after the args before the child content
      final_argument_whitespace = True
  
      def run(self):
          """
          This function is called when sphinx builds an AST out of the source files.
          Should return a list of nodes for the AST that will be appended in this location.
          """
          keywords = self.options.get('keywords', None)
          if keywords is not None and len(keywords) > 0:
              keywords = keywords.split(' ')
          else:
              keywords = []
          
          # we need to create some things inside this AST
          node = Element()
          node.document = self.state.document
          
          # build the AST for the child content
          nested_parse_with_titles(self.state, self.content, node)
          
          # get the tab's title
          title = self.arguments[0]
          
          # use the node we set up
          # (this is another class not shown here that subclasses Frame)
          frame = TabFrameNode(
            title=title,
            ids=[title.replace(' ', '_')],
            names=[title],
            index_keywords=keywords
          )
          frame += nodes.title(text=title)
          for child in node:
              if isinstance(child, TabNode):
                  frame.append(child)
          return [frame]

***********
React & AST
***********
"To allow us to render these docs in React, we need to pass the AST that Sphinx uses before it renders this to a HTML page. 

"This is done in a custom `build script <https://gist.github.com/hishnash/933ce146289faf88dd633c249eb5f228>`_. 

"The script produces a JSON dump of the AST for each file, these are uploaded to an Amazon S3 bucket and then served through AWS AWS CloudFront (a CDN service) to the client. As the user navigates the docs, the single page app pulls the needed JSON ASTs from CloudFront as and when needed."

.. code-block:: py

  """
  This is an example gist combining a few different source files from our build
  script.
  
  licensed to be under MIT
  copywrite: Matthaus Woolard 2016 matthaus.woolard@gmail.com
  """
  
  import json
  import os
  
  import errno
  import re
  import warnings
  
  from docutils import nodes
  from docutils.nodes import Text
  from docutils.parsers.rst import Directive, directives
  from sphinx.builders.html import StandaloneHTMLBuilder
  from sphinx.util import ensuredir, copyfile
  from sphinx.util.nodes import inline_all_toctrees, nested_parse_with_titles
  from sphinx.util.console import bold, darkgreen, brown
  from algoliasearch import algoliasearch
  import hashlib
  
  from docutils.nodes import title
  from sectiontile.sectiontile import SectionTileNode
  
  # we need to do some image magic :)
  IMAGE_RX = re.compile(r'^(?P<mainname>[^@.]+)(?P<res>\@2x)?.(?P<postfix>[^\s]+)$')
  
  # set this
  DOC_BASE_URL = ''
  
  algolia_to_index = []
  
  class BreadcrumbContainerNode(SectionTileNode):
      @staticmethod
      def visit_node(self, node):
          self.body.append(
              self.starttag(node, 'div'))
  
      @staticmethod
      def depart_node(self, node):
          self.body.append('</div>\n')
  
  
  class BreadCrumbs(Directive):
      final_argument_whitespace = True
      has_content = True
      required_arguments = 0
      optional_arguments = 0
      option_spec = {
          'icon': directives.unchanged,
          'keywords': directives.unchanged
      }
  
      def run(self):
          keywords = self.options.get('keywords', None)
          if keywords is not None and len(keywords) > 0:
              keywords = keywords.split(' ')
          else:
              keywords = []
          node = BreadcrumbContainerNode(icon=self.options.get('icon', None), index_keywords=keywords)
          node.document = self.state.document
          nested_parse_with_titles(self.state, self.content, node)
          return [node, ]
  
  
  
  def dict_children(children, docname=None, no_index=False, page_title=None,
                    category=None):
      """
      Convert the AST to a dict that is ready to upload and be used by React
  
      warning this is a reclusive function
      """
      child_dicts = []
      text = ''
      keywords = []
  
      for child in children:
          child_dict = {
              'module': child.__class__.__module__,
              'type': child.__class__.__name__
          }
  
          child_dict['children'], _text, kw = dict_children(child.children,
                                                            docname=docname,
                                                            no_index=no_index,
                                                            page_title=page_title,
                                                            category=category)
          text += ' ' + _text
          keywords += kw
  
          try:
              attributes = child.attributes
              child_dict['attributes'] = attributes
          except AttributeError:
              pass
          else:
              # a parent node will aggregate all the keywords of its children
              # these are used for searching.
              keywords += attributes.get('index_keywords', [])
              if attributes.get('indexed', False) and not no_index:
                  index(child_dict, _text, docname,
                        kw + attributes.get('index_keywords', []), page_title,
                        category)
          if isinstance(child, Text):
              # We collect all text and merge into one long string for search
              child_dict['attributes'] = {'text': child.astext()}
              text += ' ' + child.astext()
  
          child_dicts.append(child_dict)
  
  
      return child_dicts, text, keywords
  
  
  def index(child_dict, text, docname, keywords, page_title, category):
      """
      Index a page item and push to Algolia search
      """
  
      new_dict = child_dict.copy()
      del new_dict['children']
      version = os.environ.get('DOC_VERSION', None)
      if version is None:
          return
      ref = find_reference(child_dict['attributes'])
      add_to_algolia_search({
          'title': child_dict['attributes']['index_title'],
          'docname': docname,
          'content': new_dict,
          'text': text,
          'priority': child_dict['attributes'].get('index_priority', 0),
          'ref': ref,
          'keywords': keywords,
          'version': version,
          'page_title': page_title,
          'category': category,
          'url': DOC_BASE_URL + '/{docname}#{ref}'.format(
              docname=docname,
              ref=ref,
          ),
      })
  
  
  def index_page(doc_tree, docname, text, keywords, category):
      """
      Index a page, push it to algolia
      """
      if docname == 'index':
          return
      t = find_title(doc_tree)
  
      version = os.environ.get('DOC_VERSION', None)
      if version is None:
          return
  
      add_to_algolia_search({
          'title': t,
          'docname': docname,
          'content': {'type': 'page', 'module': 'page'},
          'text': text,
          'priority': 0,
          'keywords': keywords,
          'version': version,
          'page_title': t,
          'category': category,
          'url': DOC_BASE_URL + '/{docname}'.format(docname=docname),
      })
  
  
  def find_reference(attributes):
      """
      helper function to extract info for indexing creation of links
      """
      return attributes.get('ids', [''])[0]
  
  
  def find_category(doctrees):
      """
      Find the Breadcrumbs on this pages AST
      """
      for doctree in doctrees:
          for node in doctree.traverse(BreadcrumbContainerNode):
              for node in node.traverse(Text):
                  return node.astext()
  
  
  def find_title(doctrees):
      """
      Get the page title
      """
      for doctree in doctrees:
          for node in doctree.traverse(title):
              _, text, _ = dict_children([node], no_index=True)
              return text
  
  
  def add_to_algolia_search(data):
      """
      Add an item to be pushed to algolia
      """
      algolia_to_index.append(data)
  
  
  def push_to_algolia_search():
      if len(os.environ.get('DOC_VERSION', '')) < 12:
          raise ValueError('Invalid DOC_VERSION NO INDEXING DONE')
  
      client = algoliasearch.Client(
          os.environ.get('ALGOLIA_KEY', ''),
          os.environ.get('ALGOLIA_SECRET', '')
      )
      index = client.init_index(os.environ.get('ALGOLIA_INDEX'))
      index.delete_by_query('', {'facetFilters': 'version:{}'.format(
          os.environ.get('DOC_VERSION', None))})
      index.add_objects(algolia_to_index)
  
  
  class JsonHTMLBuilder(StandaloneHTMLBuilder):
      """
      Build both the html output but at the same time intercept the AST
  
      dump it to json and write the backup html for non javascript pages.
      """
      name = 'json-html-build'
      format = 'html'
      out_suffix = '.html'
  
      def __init__(self, *args, **kwargs):
          """
          We need to extract some images and build a map of these to replace
          the image names, we append the md5 of the image into the image name.
          :param args:
          :param kwargs:
          """
          super().__init__(*args, **kwargs)
          self._raw_images = {}
          self.images_1x = {}
          self.images_2x = {}
          self.image_map = {}
  
      def write_doc(self, docname, doctree: nodes.document):
          """
  
          This method is called to write the AST to html it is called once per
          page.
  
          """
  
          page_title = find_title(doctree)
          category = find_category(doctree)
          dict, page_text, keywords = dict_children(doctree.children, docname,
                                                    page_title=page_title,
                                                    category=category)
          index_page(doctree.children, docname, page_text, keywords, category)
          # we also build a ast dump of the toc
          toc, _, _ = dict_children([self.env.get_toc_for(docname, self)],
                                    docname, no_index=True)
          toc_filename = os.path.join(self.outdir, docname + '.toc.json')
          filename = os.path.join(self.outdir, docname + '.json')
          if not os.path.exists(os.path.dirname(filename)):
              try:
                  os.makedirs(os.path.dirname(filename))
              except OSError as exc:  # Guard against race condition
                  if exc.errno != errno.EEXIST:
                      raise
          with open(filename, 'w') as fp:
              json.dump(
                  {
                      'data': dict,
                      'toc': toc
                  }, fp)
  
          with open(toc_filename, 'w') as fp:
              json.dump(toc, fp)
  
          super().write_doc(docname, doctree)
  
      def copy_image_files(self):
          """
          We want to just update images if they change so users browser
          cache works well
          """
          # copy image files
          if self.images_1x:
              # evey image must have a 1x version
              ensuredir(os.path.join(self.outdir, self.imagedir))
              for _src in self.app.status_iterator(self.images_1x,
                                                   'copying images... ',
                                                   brown, len(self.images_1x)):
                  src, _, dest = self.images_1x[_src]
                  try:
                      copyfile(os.path.join(self.srcdir, src),
                               os.path.join(self.outdir, self.imagedir, dest))
                  except Exception as err:
                      self.warn('cannot copy image file %r: %s' %
                                (os.path.join(self.srcdir, src), err))
  
                  if _src in self.images_2x:
                      src, _, dest = self.images_2x[_src]
                      try:
                          copyfile(os.path.join(self.srcdir, src),
                                   os.path.join(self.outdir, self.imagedir,
                                                dest))
                      except Exception as err:
                          self.warn('cannot copy image file %r: %s' %
                                    (os.path.join(self.srcdir, src), err))
  
          filename = os.path.join(self.outdir, 'image_mappings.json')
          with open(filename, 'w') as f:
              json.dump(self.image_map, f)
  
      def post_process_images(self, doctree):
          """Pick the best candidate for all image URIs."""
          for node in doctree.traverse(nodes.image):
              if '?' in node['candidates']:
                  # don't rewrite nonlocal image URIs
                  continue
              if '*' not in node['candidates']:
                  for imgtype in self.supported_image_types:
                      candidate = node['candidates'].get(imgtype, None)
                      if candidate:
                          break
                  else:
                      self.warn(
                          'no matching candidate for image URI %r' % node['uri'],
                          '%s:%s' % (node.source, getattr(node, 'line', '')))
                      continue
                  node['uri'] = candidate
              else:
                  candidate = node['uri']
              if candidate not in self.env.images:
                  # non-existing URI; let it alone
                  continue
              self._raw_images[candidate] = self.env.images[candidate][1]
              file, file_hashed, file_2x, file_2x_hashed = self.get_image_name(
                  candidate, self.env.images[candidate][1])
  
              self.images[candidate] = file_hashed
              path = os.path.join(os.path.dirname(candidate),
                                  file)
              self.images_1x[candidate] = (path, file, file_hashed)
              if file_2x:
                  path = os.path.join(os.path.dirname(candidate),
                                      file_2x)
                  self.images_2x[candidate] = (path, file_2x, file_2x_hashed)
  
              uri = node['uri']
  
              if uri in self.images_1x:
                  self.image_map[uri] = self.images_1x[uri][2]
                  node['uri'] = self.images_1x[uri][2]
              if uri in self.images_2x:
                  node['uri_2x'] = self.images_2x[uri][2]
  
              node.replace_self(node)
  
          for node in doctree.traverse(SectionTileNode):
              if node['icon'] is None:
                  continue
              _candidate = node['icon']
  
              if _candidate.startswith('/'):
                  candidate = _candidate[1:]
              else:
                  candidate = _candidate
              if candidate in self.env.images:
                  file_name = self.env.images[candidate][1]
              else:
                  file_name = candidate.split('/')[-1]
              self._raw_images[candidate] = file_name
              file, file_hashed, file_2x, file_2x_hashed = self.get_image_name(
                  candidate, file_name)
              self.images[candidate] = file_hashed
  
              if file is not None:
                  path = os.path.join(os.path.dirname(candidate), file)
                  self.images_1x[candidate] = (path, file, file_hashed)
              if file_2x:
                  path = os.path.join(os.path.dirname(candidate),
                                      file_2x)
                  self.images_2x[candidate] = (path, file_2x, file_2x_hashed)
  
              if candidate in self.images_1x:
                  self.image_map[_candidate] = self.images_1x[candidate][2]
                  node['icon'] = self.images_1x[candidate][2]
              if candidate in self.images_2x:
                  node['icon_2x'] = self.images_2x[candidate][2]
              node.replace_self(node)
  
      def get_image_name(self, image_path, file_name):
          fp = re.search(IMAGE_RX, file_name)
          if fp is None:
              raise ValueError('BAD IMAGE NAME:', image_path)
          mainname = fp.group('mainname')
          postfix = fp.group('postfix')
          res = fp.group('res')
  
          dir = os.path.dirname(image_path)
  
          if res == '@2x':
              hash_2x = self.get_file(dir, mainname, res, postfix)
              hash = self.get_file(dir, mainname, '', postfix)
          else:
              hash_2x = self.get_file(dir, mainname, '@2x', postfix)
              hash = self.get_file(dir, mainname, '', postfix)
  
          file_2x_hashed = None
          file_2x = None
          file_hashed = None
          file = None
  
          if hash_2x is not None:
              file_2x_hashed = '{}-{}-@2x.{}'.format(mainname, hash_2x, postfix)
              file_2x = '{}@2x.{}'.format(mainname, postfix)
          if hash is not None:
              file_hashed = '{}-{}.{}'.format(mainname, hash, postfix)
              file = '{}.{}'.format(mainname, postfix)
          return file, file_hashed, file_2x, file_2x_hashed
  
      def get_file(self, dir, mainname, res, postfix):
          file_name = mainname + res + '.' + postfix
          try:
              p = os.path.join(self.srcdir, dir, file_name)
              with open(p, 'rb') as f:
                  return hashlib.md5(f.read()).hexdigest()
          except FileNotFoundError:
              warnings.warn('Cant fine {}'.format(file_name))
          return None
  
      def finish(self, *args, **kwargs):
          super().finish(*args, **kwargs)
          if os.environ.get('DOC_VERSION', None) is not None:
              if os.environ.get('DOC_DEPLOY', None) == 'TRUE':
                  push_to_algolia_search()
  
  
  def setup(app):
      app.add_builder(JsonHTMLBuilder)
      app.add_directive('bc', BreadCrumbs)
  
      app.add_node(BreadcrumbContainerNode,
                   html=(BreadcrumbContainerNode.visit_node,
                         BreadcrumbContainerNode.depart_node))
