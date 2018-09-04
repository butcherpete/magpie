:date: 2018-09-03 
:version: 1
:author: tes 
:information-type: api 
:platform: demand
:product: vim 
:description: |greek| 
:audience: external
:tags: tag1, tag2, tag3 
:keywords: keyword1, keyword2, keyword3 
:languages: english
:orphan:
:nocomments:

.. include:: /includes/include.txt

################
Terminal Mode
################

|greek|

********
Overview
********
"Terminal mode is only available in terminal buffers, where you can activate the mode by pressing i, a, I, or A. In a regular text buffer, these same commands would switch to Insert mode, but that mode is not available in a terminal buffer."

http://vimcasts.org/episodes/neovim-terminal/

****************
Launch the Shell
****************

.. code-block:: vim

  :terminal
  :te
  :terminal top
  :terminal rails server

**********************************
Switch Between Terminal and Normal
**********************************

.. code-block:: vim

  <Esc> 

********************************
Open Terminal Buffers in Windows
********************************

Run the commands:

.. code-block:: vim

  :split
  :te

The table summarizes commands:

.. list-table::
  :header-rows: 1

  * - Command
    - Effect
  * - :code:`:terminal {cmd}`
    - Create terminal buffer in current window
  * - :code:`:split | terminal {cmd}`
    - Create terminal buffer in horizontal split 
  * - :code:`:vsplit | terminal {cmd}`
    - Create terminal buffer in vertical split 
  * - :code:`:tabedit | terminal {cmd}`
    - Create terminal buffer in new tab page 
