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


********************
Package.json Scripts
********************
https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9

Create bundles using scripts:

.. code-blocK:: javascript

   “scripts”: {
    //npm run build to build production bundles
    “build”: “webpack --config webpack.config.prod.js”,

    //npm run dev to generate development bundles and run dev. server
    “dev”: “webpack-dev-server”
   }


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
Use the CLI to generate production builds. Compare with Webpack-dev-sderver

https://webpack.js.org/api/cli/

  For proper usage and easy distribution of this configuration, webpack can be configured with :code:`webpack.config.js`. Any parameters sent to the CLI will map to a corresponding parameter in the config file.

The CLI is great for debugging issues and working with small projects.


Option 1:
=========

.. code-block:: javascript

  $ node_modules/ .bin/webpack --entry ./src/entry.js --output-filename output.js --output-path ./ 

Option 2:
=========
.. code-block:: javascript

  //Install it globally
  npm install webpack --g

  //Generate bundle using webpack.config.js 
  $ webpack 


Option 3:
=========

.. code-block:: javascript

  //Install it locally & add it to package.json
  npm install webpack --save

  //Add it to package.json's script 
  “scripts”: {
   “build”: “webpack --config webpack.config.prod.js -p”,
   ...
   }

  //Use it by running the following:
   $ npm run build

******************
Webpack Dev Server
******************
https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9

An Express node.js server that runs on port 8080.

- Enables live reloading
- Enables hot module replacement (HMR)


Option 1
========
.. code-block:: javascript

  //Install it globally
  npm install webpack-dev-server --save

  //Use it at the terminal
  $ webpack-dev-server --inline --hot

Option 2
========
Open browser at: http://localhost:8080

.. code-block:: javascript

  // Add it to package.json's script 
  
  “scripts”: {
   “start”: “webpack-dev-server --inline --hot”,
   ...
   }
  // Use it by running 
  $ npm start

*******
Loaders
*******
  Loaders are node modules that import files of various types into browser acceptable formats like JS and stylesheets. Further loaders also allow importing such files into JS via “require” or “import” in ES6.

Chaining Loaders
================
Multiple loaders can be chained together to work on the same file type. 

- Chain from left to right.
- Separate loaders with :code:`!`

For example, use two loaders (css-loader and style-loader) to dump our CSS file (:code:`myCssFile.css`) into the  :code:`<style>CSS content</style>` tag in our HTML:

.. code-block:: javascript

  module: {
   loaders: [{
    test: /\.css$/,
    loader: ‘style!css’ <--(short for style-loader!css-loader)
   }]

What happens:

  1. Webpack searches for CSS files dependencies inside the modules. That is Webpack checks to see if a JS file has “require(myCssFile.css)”. If it finds the dependency, then the Webpack gives that file first to the “css-loader”
  
  2. css-loader loads all the CSS and CSS’ own dependencies (i.e @import otherCSS) into JSON. Webpack then passes the result to “style-loader”.
  
  3. style-loader to take the JSON and add it to a style tag — <style>CSS contents</style> and inserts the tag into the index.html file.


Loaders Configuration
=====================
  Loaders themselves can be configured to work differently by passing parameters.
  
  In the example below, we are configuring url-loader to use DataURLs for images less than 1024 bytes and use URL for images that are larger than 1024 bytes. We can do this by passing “limit” parameter in the following two ways:

.. code-block:: json

  //Option 1: Use "?" just like in URLs
  { test: /\.png$/,
    loader: "url-loader?limit=1024"
  },

  //Option 2: Use "query" property
  { test: /\.png$/,
    loader: "url-loader",
    query: {limit: 1024}
  },

*********
Debugging
*********
https://webpack.js.org/api/cli/#debug-options

Command-line options for debugging webpack:

.. list-table:: Debug Options
  :header-rows: 1

  * - Parameter
    - Description
  * - :code:`--debug`
    - Switches loaders to debug mode:
  * - :code:`--display-error-details`
    - Displays details about errors.
  * - :code:`--progress`
    - Prints compiliation progress.
  * - :code:`--devtool`
    - Define `source map type <https://webpack.js.org/configuration/devtool/>`_ for the bundled resources.
  * - :code:`--inspect`
    - Enables you to see Node.js code in Chrome DevTools. To learn more, see https://nodejs.org/en/docs/inspector

Webpack Bundle Analyzer
=======================
https://www.npmjs.com/package/webpack-bundle-analyzer

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

