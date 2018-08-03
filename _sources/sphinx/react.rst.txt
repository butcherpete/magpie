#####################################
Adaptive Modern Product Documentaiton
#####################################

.. highlights::

  - https://hackernoon.com/adaptive-modern-product-documentation-7d792fd8696d
  - https://gist.github.com/hishnash/933ce146289faf88dd633c249eb5f228


**************
Tabs Directive
**************
Test script.

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
