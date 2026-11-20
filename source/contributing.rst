.. _contributing:

Contributing to the Wiki
========================

:Last reviewed: 2026-10

This wiki is the public documentation for people who use OSL services:
hosted projects, OpenStack tenants, CI users and anyone else outside the
lab. Its source is
`osuosl/wiki on GitHub <https://github.com/osuosl/wiki>`_, and corrections
are welcome as pull requests.

What belongs here
-----------------

A page belongs on the wiki when its reader is outside OSL. It explains how
to use a service, in the second person, and ends with how to get help.

How OSL runs a service is documented separately, for staff. Keep these out
of the wiki:

* internal hostnames, management networks and private addresses
* ticket links or numbers, and who asked for what
* administrative accounts, and where credentials are kept
* staff procedures and hardware details beyond what a user needs

``make lint`` checks for most of these. If a user really has to type a
private address (the VPN gateway, for example), put this comment on the
line before it::

   .. style-ok: private-ip users ping the VPN gateway to test the tunnel

Building and checking
---------------------

You need Python 3.12 and graphviz. From the repository root::

   scripts/localbuild.sh                          # set up venv/ and build into build/html
   make html SPHINXBUILD=venv/bin/sphinx-build    # warnings are errors
   make lint_changed                              # check the .rst files you changed

``make lint_changed`` compares your branch with ``origin/master``. Run
``git fetch origin`` first.

Every pull request is built and published as a preview at
``https://wiki-<PR number>.staging.osuosl.org``, linked from the
**Published site URL** check.

Markup conventions
------------------

* **Page start:** every page starts with a kebab-case label
  (``.. _openstack-guests:``), then the title underlined with ``=``.
  Sections use ``-``, then ``^``, then ``"``. Use underlines only, no
  overlines.
* **Wrapping:** wrap prose at 80 columns. Code, tables and long URLs are
  exempt.
* **Lists:** bullets are ``*`` and numbered steps are ``#.``. A sub-list
  needs a blank line before it and an indent to the parent item's text.
* **Literals:** put commands, file names, options and package names in
  ``double backticks``.
* **Commands** go in a plain ``::`` block with no prompt, so they can be
  pasted as they are. Show the output the user should expect in a separate
  ``.. code-block:: text``.
* **Links:** inline, ```text <https://...>`_``, always ``https``. Link other
  wiki pages with ``:ref:`label```.
* **Images:** in ``source/_static/images/``, each with ``:alt:`` text.
* **Admonitions:** ``note``, ``warning``, ``tip`` or ``important``, used
  sparingly.
* **Label changes:** don't rename or remove a label listed in
  ``scripts/frozen_labels.txt``. OSL's internal documentation links to
  those labels, and the check fails if one disappears.

A user guide usually has this shape:

#. What the service lets you do, and who can use it.
#. Before you start: what you need, and how to request access.
#. Steps, numbered, with commands and expected output.
#. Troubleshooting: the errors users actually hit.
#. Getting help: email ``support@osuosl.org`` with a suggested subject line
   (``<Service>: <what you need> for <project>``), saying what to include.

Commits and pull requests
-------------------------

* **Branch:** work on a branch, never on ``master``.
* **Commits:** give each a short imperative subject (``openstack: document
  image properties``), a body that explains why, and a ``Signed-off-by``
  line (``git commit -s``).
* **Rebasing:** rebase on ``origin/master`` instead of merging ``master`` in.
* **Merging:** a member of OSL staff reviews and merges pull requests.
