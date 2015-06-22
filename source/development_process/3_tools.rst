3. Git and Friends
==================

One of the most important tools we use for collaboration at the lab is git.
Git is a powerful tool which is generally easy to use, but sometimes it is
possible to wind up in a weird state. This section of the document describes
some intermediate level features of git which may be useful to the developer
team. Developers may also want to read `tricks for configuring git
<configuring_git.html>`_.

.. warning:: Invalid link.

When to Use the Powers of the Force
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sometimes changes are made which affect the past history of the local branch,
and when these changes are pushed to GitHub or another git server, they will be
rejected because the history on the server does not match the local history. A
common example is rebasing a branch to pick up new changes, which is detailed
further in the next section. The server can be made to accept these changes
with the ``--force`` flag, but be careful! Force pushing is a dangerous
operation which will permanently rewrite history on the server. Junior
developers should consult more experienced colleagues before force pushing.

Developers must always use a fully qualified push command when force pushing,
naming both the git remote and branch. To force push to a branch named
``branch``, run:

.. code:: bash

	git push --force origin branch

Do NOT run:

.. code:: bash

	git push --force

Resolving Merge Conflicts
~~~~~~~~~~~~~~~~~~~~~~~~~
Merge conflicts are an unfortunate reality when working with peers on a large
code base. They are easy to fix, but they must be fixed with care as the
functionality of the code may be unintentionally changed. Always run tests
before pushing a branch which had merge conflicts. Merge conflicts can happen
when running ``git merge source_branch`` and when pulling or rebasing.

Git denotes merge conflicts with a series of angle brackets. After each series
of angle brackets is the name of the commit where the changes came from. In
this case, the code in the HEAD revision is older than the other revision, so
the code between ``<< HEAD`` and the equal signs should be removed. The line
with the angle brackets and the newer commit hash should also be removed. This
cannot be done automatically, because git doesn't know which lines to include
or whether some combination of the lines should be included.

.. code:: python

	<<<<<<< HEAD
			sortx_sql = sortx.aggregate.as_sql(qn, cn)
			sorty_sql = sorty.aggregate.as_sql(qn, cn)
	=======
			sortx_sql = sortx.aggregate.as_sql(qn, cn)[0]
			sorty_sql = sorty.aggregate.as_sql(qn, cn)[0]
	>>>>>>> 692b8936b466d8c651bb1ab39e96ca98c7c4714b

To resolve merge conflicts when running ``git merge``, add the files which were
corrected, and then commit. That commit will have its title automatically
generated -- do not change the title, but feel free to add more details to the
body of the commit about why the merge is happening.

Always run ``git grep '<<<'`` and ``git grep '>>>'`` before pushing code after
a merge conflict and run tests. It is possible that some merge-related code
escaped notice, and this should be fixed as soon as possible.

Rebasing and Squashing Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Often a developer will check out a new branch and while they are working on the
branch, different changes will be merged into develop. To pick up changes on
develop, check out the working branch and run the following:

.. code:: bash

	$ git checkout fancy-changes
	$ git rebase develop

This will add all of the changes merged into develop since the branches
diverged onto ``fancy-new-changes``.

Sometimes a series of commits should be combined into one large commit. This
can be useful when there were many "work in progress" commits which do not need
to clutter the git history. This is called squashing commits. First, find the
oldest commit hash which should be squashed using ``git log`` (in this example,
the hash is ``abcde12345``). Then run:

.. code:: bash

	$ git rebase -i abcde12345 # i stands for interactive

Git will open up the editor and provide detailed instructions on how to choose
which commits to keep or combine.

Cherry Picking
~~~~~~~~~~~~~~
Sometimes it will be necessary to move several commits from one branch to
another. This can be achieved simply by using ``git cherry-pick``. First, check
out the branch which the commits will be moved to. Then, find the hash
representing the commit using ``git log --all``. For example, if that hash were
``abcde12345``, run:

.. code:: shell

	$ git cherry-pick abcde12345

This will add commit ``abcde12345`` to the current branch.


When Disaster Strikes
~~~~~~~~~~~~~~~~~~~~~
On occasion, disaster will strike, and it will appear that all has been lost. It
is important not to panic as such mistakes can often be resolved. As long as the
``.git`` folder is intact, git keeps a log of the changes made to the
repository. If a change is made which affects git history, the hash of the
commit previous to the change will be stored in the special file
``.git/ORIG_HEAD``, for instance ``abcde12345``. To go back to that commit, run
``git reset abcde12345``.

Miscellaneous Git Tips
~~~~~~~~~~~~~~~~~~~~~~

* To undo the last commit, run ``git reset HEAD~1``
* To amend the last commit *which has not been pushed* and fix anything which
  was forgotten, first add any files which were changed or forgotten, then run
  ``git commit --amend``
* To add part of a file, use ``git add -p`` and follow the interactive
  instructions
* To delete a remote branch named ``branch``, run ``git push origin :branch``
* To get a pretty view of git history, run ``git log --graph --all`` (some 
  developers alias this to ``git-net``)


