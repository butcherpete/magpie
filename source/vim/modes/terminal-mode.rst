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

http://vimcasts.org/episodes/neovim-terminal/

****************
Launch the Shell
****************

You can supply a command to the Terminal emulator.

.. code-block:: vim

  :terminal
  :te
  :terminal top
  :terminal rails server


To open nvim in Terminal mode:

.. code-block:: vim

  $ nvim +terminal

**********************
Activate Terminal Mode
**********************
To activate terminal mode, press :code:`i`, :code:`a`, :code:`I`, or :code:`A`. 

In Normal mode, these commands switch to Insert mode.

**********************************
Switch Back to Normal Mode
**********************************

.. code-block:: vim

  <C-\><C-n>
  <Esc> 

Set mapping to escape Terminal mode.

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
