.. include:: <isopub.txt>
 
#########################
Custom Roles 
#########################

**********
Goals
**********
Define custom directives and roles. 

**********
To Do List
**********

|check| `Creating Custom Link Roles <http://protips.readthedocs.io/link-roles.html>`

- Test gist https://gist.github.com/shimizukawa/3718712 
- Create custom role that copies the existing :code:`term` role.

*******************************
Defining Custom Roles in Sphinx
*******************************
https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/

**************************
Creating Custom Link Roles
**************************
http://protips.readthedocs.io/link-roles.html

The article describes a six-step process:

1. Create an :code:`_extensions` directory to hold extensions.
2. Add a custom search path in the :code:`conf.py` that includes the :code:`_extensions` directory.
3. Create the extension (:code:`bemuse.py`).
4. Add the extension to the  :code:`_extensions` directory. 
5. Add the extension to the :code:`extensions` list in the the :code:`conf.py`.
6. Mark up text using the custom roles.


**Directory Structure**

:tree:`assets` Image assets for use in the game.
  These assets can be referred from webpack code by ``require('assets/...')``.
:tree:`bin`
  Useful scripts for routine work.
  Examples include setting up Git commit hooks and releasing a new version.
:tree:`config`
  Configuration code for webpack and other things.

These three roles are rather limited:

- Each role links to a specific URL.
- Each role is defined by the :code:`reference` and :code:`external` classes.

**********
Resources
**********

- http://www.sphinx-doc.org/en/stable/templating.html#script_files
- https://github.com/ryan-roemer/sphinx-bootstrap-theme
