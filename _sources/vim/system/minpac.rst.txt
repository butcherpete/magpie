######
Minpac
######

.. contents::
  :local:
  :depth: 1

************
Add Packages
************

.. code-block:: bash

  :write
  :source %
  :call minpac#update()


**********
Reviewing 
**********
As minpac handles each plugin, it echoes a message. These usually go by too quickly to read, but if you want to review them afterward, run the following:


.. code-block:: bash

  :messages


**********
Removing
**********

.. code-block:: bash

  :write
  :source %
  :call minpac#clean()
