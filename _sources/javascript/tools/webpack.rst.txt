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


*************
Configuration
*************
A configuration file is not required. 

By default, webpack
- Uses :code:`src/index` as the entry point of your project.
- Outputs the result to :code:`dist/main.js` minified and optimized for production.

To overwrite and extend basic functionality, define a :code:`webpack.config.js` in the root directory. 

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


*********
Resources
*********
- https://webpack.js.org/
- `Generate Custom Webpack Configuration <https://generatewebpackconfig.netlify.com/>`_
- `Visual Tool for Creating Webpack Configs <https://webpack.jakoblind.no/>`_

