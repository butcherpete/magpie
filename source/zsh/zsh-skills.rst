:date: 2018-09-19 
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
Zsh Skills
################

.. container:: abstract
 
  |greek|

********
Overview
********

`The Z Shell Manual <http://zsh.sourceforge.net/Doc/Release/zsh_toc.html#SEC_Contents>`_




**********
Operations
**********
http://reasoniamhere.com/2014/01/11/outrageously-useful-tips-to-master-your-z-shell/

.. code:: bash

  # create dummy files inside the data folder
  for country_folder in zsh_demo/data/*/*; do
      dd if=/dev/zero of="${country_folder}/population.txt" bs=1024 count=1
      dd if=/dev/zero of="${country_folder}/income.txt" bs=2048 count=1
      dd if=/dev/zero of="${country_folder}/literacy.txt" bs=4096 count=1
      # we say these are dummy files because they don't have any content,
      # but we are making them occupy disk space
  done


********
Globbing
********
http://reasoniamhere.com/2014/01/11/outrageously-useful-tips-to-master-your-z-shell/

.. code:: bash

  # list every file directly below the zsh_demo folder
  ls zsh_demo
  
  # list every file in the folders directly below the zsh_demo folder
  ls zsh_demo/*
  
  # list every file in every folder two levels below the zsh_demo folder
  ls zsh_demo/*/*
  
  # list every file anywhere below the zsh_demo folder
  ls zsh_demo/**/*
  
  # list every file that ends in .txt in every folder at any level below the zsh_demo folder
  ls zsh_demo/**/*.txt


Glob Operators
==============
"So, what else can you stick inside a glob besides asterisks? Glance at section 14.8.1 of the manual if you want to know all the options. Here are the ones that I find most useful:"

.. code-block:: bash

  # list text files that end in a number from 1 to 10
  ls -l zsh_demo/**/*<1-10>.txt
  
  # list text files that start with the letter a
  ls -l zsh_demo/**/[a]*.txt
  
  # list text files that start with either ab or bc
  ls -l zsh_demo/**/(ab|bc)*.txt
  
  # list text files that don't start with a lower or uppercase c
  ls -l zsh_demo/**/[^cC]*.txt

Glob Qualifiers
===============
http://reasoniamhere.com/2014/01/11/outrageously-useful-tips-to-master-your-z-shell/

"Glob qualifiers are surrounded in parentheses :code:`()`, and appear at the end of a glob to make it more stringent. Globs filter files by their name, and glob qualifiers filter by any other attribute (file type, size, modification date)."

.. code-block:: bash

  # show only directories
  print -l zsh_demo/**/*(/)
  
  # show only regular files
  print -l zsh_demo/**/*(.)
  
  # show empty files
  ls -l zsh_demo/**/*(L0)
  
  # show files greater than 3 KB
  ls -l zsh_demo/**/*(Lk+3)
  
  # show files modified in the last hour
  print -l zsh_demo/**/*(mh-1)
  
  # sort files from most to least recently modified and show the last 3
  ls -l zsh_demo/**/*(om[1,3])

************************
Variable Transformations
************************

**************
Magic Tabbling
**************

*********
Resources
*********
There is a ton of stuff we haven’t covered, but I can point you to other people’s awesome tips. They are all totally worth it:

- Andrew Hays encourages us to love our terminal by installing the elegant Solarized color scheme, and customizing our prompt. Follow his instructions and make all those hours in front of your terminal a more enjoyable experience.
- Danilo Petrozzi over at Zsh Wiki shares a powerful alternative to global aliases. If you find yourself typing stuff like | head | column -t | less -S at the end of your commands, check out his method to turn any sequence of characters into a convenient snippet.
- Also at Zsh Wiki, learn about a way to rename multiple files by using the zmv command. It’s extremely convenient for replacing spaces with underscores, changing file extensions, and renaming files located in a nested folder structure. Always run zmv using the -n option once, so you are know what the command will actually do.
- We used brace expansion multiple times in this tutorial, but we didn’t cover all of its features. Tomasz Muras wrote a nice post about it.
- I wasn’t able to find a blog post explaining associative arrays, but I’ve found them incredibly useful to deal with sets of parameters. If there’s interest, I might go into them in a future post.
