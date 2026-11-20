OSUOSL Public Documentation
===========================

The public documentation for people who use Open Source Lab services,
published at https://wiki.osuosl.org/. OSL's internal staff documentation
lives in the private ``osuosl/docs`` repository.

How to contribute, what belongs here and the markup conventions are in
``source/contributing.rst``.

Building locally
----------------

You need Python 3.12 and graphviz::

   scripts/localbuild.sh          # create or refresh venv/ and build into build/html
   make html SPHINXBUILD=venv/bin/sphinx-build   # warnings are errors (-W)
   make lint_changed     # rstcheck + scripts/check_style.py --public on changed .rst files
   make lint             # the same on every file
   make linkcheck        # check external links; report in build/linkcheck/output.json

Publishing
----------

``Jenkinsfile`` drives a multibranch Jenkins job. A pull request is linted,
built with ``-W`` and published as a preview at
``https://wiki-<PR number>.staging.osuosl.org``. A merge to ``master``
publishes https://wiki.osuosl.org/.

Updating dependencies
---------------------

Direct dependencies live in ``requirements.in``; ``requirements.txt`` is a
lock file generated from it with
`pip-compile <https://pip-tools.readthedocs.io/>`_. Dependabot updates the
lock file weekly. To change or upgrade dependencies by hand::

   pip install pip-tools
   pip-compile --strip-extras requirements.in            # re-lock after editing requirements.in
   pip-compile --strip-extras --upgrade requirements.in  # upgrade everything

Never edit ``requirements.txt`` by hand.

Shared style checker
--------------------

``scripts/check_style.py`` is shared with OSL's internal documentation and
kept identical in both repositories. Change it there first, then copy it
here.
