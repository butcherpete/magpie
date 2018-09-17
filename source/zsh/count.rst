:date: 2018-09-11 
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
Counting Images
################

.. container:: abstract
 
  |greek|

********
Overview
********

Level-3
=======

.. code-block:: bash

  find . -type f -print0 | xargs -0 file -i | grep -i image | wc -l

  ls -lR **/*.png | wc -1


Count objects with extensions:

.. code-block:: bash

  git ls-files | grep "\.js$" | wc -l



https://stackoverflow.com/questions/1265040/how-to-count-total-lines-changed-by-a-specific-author-in-a-git-repository


