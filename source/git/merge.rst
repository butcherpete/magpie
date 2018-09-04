.. include:: <isopub.txt>
 
###############
Merge Conflicts
###############

Resolve merge conflict in favor of one file or the other:

1. Merge branches.

  .. code-block:: bash
  
    $ git pull origin master
    From git.ouroath.com:tes/ydn2-docs-brightroll-dsp
    * branch              master     -> FETCH_HEAD
    Auto-merging optimization/index.rst
    Auto-merging css/documentation.css
    CONFLICT (add/add): Merge conflict in css/documentation.css
    Automatic merge failed; fix conflicts and then commit the result.

2. Resolve conflict.

  To choose our file, the local copy rather than one being merged into the branch.

  .. code-block:: bash
  
    $ git checkout --ours css/documentation.css 

  To choose their file, the remote copy being merged into the branch.

  .. code-block:: bash
  
    $ git checkout --theirs css/documentation.css 

3. Commit changed file.

  .. code-block:: bash
  
    $ git checkout --ours css/documentation.css 
    Unmerged paths:
    (use "git add <file>..." to mark resolution)
    
    both added:      css/documentation.css
