:date: 2018-09-16 
:version: 1
:author: tes 
:information-type: api 
:platform: demand
:product: 
:description: |greek| 
:audience: external
:tags: tag1, tag2, tag3 
:keywords: keyword1, keyword2, keyword3 
:languages: english
:orphan:
:nocomments:

.. include:: /includes/include.txt

################
Webpack
################

.. container:: abstract
 
  |greek|

********
Overview
********
https://webpack.js.org/concepts/

  At its core, webpack is a :emphasis:`static module bundler` for modern JavaScript applications. When webpack processes your application, it internally builds a dependency graph which maps every module your project needs and generates one or more bundles.

Webpack is a build tool that can be run from the command line via a JavaScript configuration file (:code:`webpack.config.js`).

- Webpack enable JavaScript code to be compiled.
- Webpack allows npm packages to be used with browser code.
- Using loaders to compile ES6 and JSX code and load static assets via loaders.
- Code splitting for smart bundling of code into smaller packages.
- Builds code for the server or browser.
- Sourcemaps.
- Webpack dev server.
- Built-in watch option.

*********************
Webpack Configuration
*********************
The a :code:`webpack.config.js` enables you to overwrite and extend basic functionality. It's not required. 

To load the default config, compile the code, and output a bundle file that can be loaded in the browser, run the command:

.. code-block:: javascript

  $ ./node_modules/.bin/webpack

By default, webpack

- Uses :code:`src/index` as the entry point of your project.
- Outputs the result to :code:`dist/main.js` minified and optimized for production.

.. code-block:: javascript

  {
      "mode": "production",
      "entry": "src/index.js",
      "output": {
          "path": __dirname+'/static',
          "filename": "[name].[chunkhash:8].js"
      },
      "devtool": "source-map",
      "module": {
          "rules": [
              {
                  "enforce": "pre",
                  "test": /\.(js|jsx)$/,
                  "exclude": /node_modules/,
                  "use": "eslint-loader"
              },
              {
                  "test": /\.(js|jsx)$/,
                  "exclude": /node_modules/,
                  "use": {
                      "loader": "babel-loader",
                      "options": {
                          "presets": [
                              "env",
                              "react"
                          ]
                      }
                  }
              },
              {
                  "test": /\.scss$/,
                  "use": [
                      "style-loader",
                      "css-loader",
                      "sass-loader"
                  ]
              }
          ]
      }
  }

**********************
Command Line Interface
**********************
https://webpack.js.org/api/cli/

  For proper usage and easy distribution of this configuration, webpack can be configured with :code:`webpack.config.js`. Any parameters sent to the CLI will map to a corresponding parameter in the config file.

The CLI is great for debugging issues and working with small projects.

To generate a bundle:

.. code-block:: javascript

  $ node_modules/ .bin/webpack --entry ./src/entry.js --output-filename output.js --output-path ./ 



*******
Loaders
*******

*********
Debugging
*********
https://webpack.js.org/api/cli/#debug-options

**********
Sourcemaps
**********
https://blog.teamtreehouse.com/introduction-source-maps

  A source map provides a way of mapping code within a compressed file back to it’s original position in a source file. This means that – with the help of a bit of software – you can easily debug your applications even after your assets have been optimized. The Chrome and Firefox developer tools both ship with built-in support for source maps.

https://webpack.js.org/configuration/devtool/

Devtool enables you to choose a style of  `source mapping <https://blog.teamtreehouse.com/introduction-source-maps>`_ used to enhance the debugging process. These values can affect build and rebuild speed dramatically. Sourcemaps enable you to match code errors to your file structure.

  With sourcemaps enabled, webpack generates additional code (sometimes inline and sometimes in a separate file) that maps the generated code back to the original file structure. That's helpful when debugging, because tools like Chrome DevTools enables you to inspect the original code rather than the compile code.

.. code-block:: javascript

  module.exports = Object.assign(baseConfig, {
    output: {},
    devtool: 'source-map',
    plugins: []
    })

Developer Tool Support
======================

  Note: Support for source maps is enabled by default in Firefox’s developer tools. You may need to enable support manually in Chrome. To do this, launch the Chrome dev tools and open the Settings pane (cog in the bottom right corner). In the General tab make sure that Enable JS source maps and Enable CSS source maps are both ticked.

*********
Resources
*********
- https://webpack.js.org/
- `Generate Custom Webpack Configuration <https://generatewebpackconfig.netlify.com/>`_
- `Visual Tool for Creating Webpack Configs <https://webpack.jakoblind.no/>`_

