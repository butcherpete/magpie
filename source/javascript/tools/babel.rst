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
Babel
################

.. container:: abstract
 
  |greek|

********
Overview
********
"Babel is a toolchain that is mainly used to convert ECMAScript 2015+ code into a backwards compatible version of JavaScript in current and older browsers or environments."

*******
Babelrc
*******
https://babeljs.io/docs/en/next/config-files#file-relative-configuration

  Babel loads :code:`.babelrc` (and :code:`.babelrc.js` / :code:`package.json#babel`) files by searching up the directory structure starting from the "filename" being compiled. This can be powerful because it allows you to create independent configurations for subsections of a repository. File-relative configurations are also merged over top of project-wide config values, making them potentially useful for specific overrides, though that can also be accomplished through "overrides".


The :code:`.babelrc`  defines two presets for the compiler to use:

.. code-block:: javascript

  {
    "presets": ["es2015", "react"],
    "plugins": [
      "transform-es2015-destructuring",
      "transform-es2015-parameters",
      "transform-object-rest-spread"
    ]
  }

*********
Resources
*********

- https://babeljs.io/docs/en/next/config-files
- https://sebastiandedeyne.com/whats-in-our-babelrc
