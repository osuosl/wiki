
.. _osl-development-process:

The OSL Development Workflow Guide
==================================

The OSL builds websites for a variety of clients including the Oregon Virtual
School Districts, the Oregon Sea Grant Foundation, the OSU Biology department
and Google. When the initial development is finished, the OSL will host and
maintain the websites. This document will guide developers through the steps of
creating a new website for a client. New developers are encouraged to read this
document to understand how the developer team works, and experienced developers
are encouraged to review this document to brush up their knowledge of parts of
the process they may not be intimately familiar with. This workflow description
will also be available to clients so they can understand how the OSL developer
team works.

How the Developer Team Interacts With Clients
---------------------------------------------
The needs of clients vary a surprising amount. The developer team is expected
to modify the development and maintenance schedule to suit the specific needs
of each customer. In the past, the OSL has adopted an agile methodology for
working with the BSG and the Sea Grant foundation. This contrasts with the more
conservative development and release cycle of the Protein Geometry Database,
where every major change and new release must be certified by scientists.

For the What's Fresh and Working Waterfronts website the developer team chose
to follow the agile methodology. The agile method promotes quick responses to
change and customer collaboration, which made it an ideal fit for working with
both the Sea Grant Foundation and the BSG on an integrated website and mobile
application. The agile development methodology is defined in `the agile
manifesto <http://www.agilemanifesto.org/>`_, which is required reading for
all developers should the team choose to follow this methodology. When
following the agile methodology the developer team meets every month to
discuss the state of the project and show their progress to the client. The Sea
Grant projects also followed the test driven development model, which dictates
that tests should be written before code. This ensures that all of the code is
tested and works properly.

The PGD project has a very different set of constraints. It is a large project
which is being maintained, but little active development is being done. The PGD
is a tool used by hundreds of scientists throughout the world, so it is very
important that changes do not introduce bugs which may affect ongoing research.
Every change to the PGD project must be approved by the scientists in charge of
the project. It is difficult to write tests to ensure that new changes don't
impact the science. Historically the PGD has had issues with upstream protein
repositories and antiquated closed-source dependencies. Even importing new data
can sometimes be a fraught process, but we are developing a detailed process to
minimize problems when upstream software or data changes.

Tools We Use
------------
At the OSL we use a variety of open source tools. Developers are expected to
have at least passing familiarity with all of these tools. New developers are
encouraged to research any of these tools they have not heard of.

Most OSL websites are written in Python using the Django web application
framework. Websites are deployed using Chef configuration management on CentOS
6.6. Most of our sites use the MySQL database, although some use PostGres.
Most OSL websites have a Docker development environment set up to make
development fast and easy. To learn how to use the Docker development
environment please consult the project documentation and the `OSL's internal
documentation
<https://docs.osuosl.org/development/docker-dev-environments.html>`_.
The OSL uses ``git`` for version control and keeps projects on
`GitHub <https://github.com/osuosl>`_. The OSL uses the `RedMine issue tracker
<https://code.osuosl.org>`_ because GitHub does not support time tracking.

How a Typical Project is Written
================================
This is a step by step guide for writing a Django website. It will not cover
how to write a website using Flask because the process is nearly identical and
the team has indicated that Django is to be preferred for new projects.

Determine Requirements
----------------------
- Meet with client
- determine requirements
- determine milestones
- internally determine code sprints

Setting Up the Project
----------------------
- Create the git repo
- Create the issue tracker
- Create the project skeleton with Django
- Create the Dockerfile
- Create a virtualenv
- Create the projects default branch (if not master)

The Development Process
-----------------------
- Pick an issue
- Checkout a new branch (with a branch naming scheme)
- Write tests (with a sample Django test)
- Write the code
- Make a PR
- Merge it
- Close the issue

A Brief Introduction to Django at the OSL
-----------------------------------------

The Django project has a `great beginner's tutorial`_ that requires very little
knowledge of Python.

.. _great beginner's tutorial: https://docs.djangoproject.com/en/dev/intro/tutorial01/

Lots of OSL projects are written in Django, including Ganeti Web Manager,
What's Fresh, Working Waterfronts, and PGD. Here are some notes about Django
at the OSL:

Configuration
~~~~~~~~~~~~~

We use yaml-based configuration for many of our Django projects. This makes
the configuration easier to read, and in general allows a slightly greater
degree of freedom in setting up. To see how this is set up, take a look at
`What's Fresh's settings.py`_.

.. _What's Fresh's settings.py: https://github.com/osu-cass/whats-fresh-api/blob/master/whats_fresh/settings.py

In general, apps will attempt to load settings from environmental variables.
This is most commonly used with our Docker-based developer environments. If
the environment variables are not set, it'll load settings from a yaml config
file, generally stored at ``/opt/app_name/config/config.yml`` by default. This
can also be overridden with an environment variable.

Application location
~~~~~~~~~~~~~~~~~~~~

Applications live in a subdirectory of the project. That is to say, if my project
is named ``project``, and my app is named ``app``, the directory structure will
look something like this::

  manage.py
  project/
    /project/settings.py
    /app/models.py

Automated testing with Travis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automated testing with Travis CI is an incredibly powerful tool. Travis is a
continuous integration tool, meaning it's designed to run every time someone
commits code to a repositoy. In our case, it integrates directly into GitHub
and runs all of our tests, allowing code reviewers to see if a pull request
breaks something, or if a merge went horribly, horribly wrong.

To set this up, make a ``.travis.yml`` file in the root of the repo. It should
look something like this::

  language: python
  python:
    - "2.7"
  # command to install dependencies
  install:
    - "python setup.py develop"
    - "pip install flake8"
  # command to run tests
  script:
    - flake8 working_waterfronts/
    - django-admin test working_waterfronts --settings="working_waterfronts.settings"
  addons:
    postgresql: "9.3"
  before_script:
    - psql -c 'create database working_waterfronts;' -U postgres
    - psql -U postgres -c "create extension postgis;" working_waterfronts

Any command put in the ``before_script`` will be run. This allows us to create
database and extension needed for the app. The ``script`` is the actual test run
itself. If either command fails, the "build" will fail, and Travis will report
that it is not safe to merge.

Using flake8 in Travis forces us to keep our code clean and easy to read.

How to Git Out of a Tight Corner
--------------------------------
Git is a powerful tool which is generally easy to use, but sometimes it is
possible to wind up in a weird state. This section of the document describes
some intermediate level features of git which may be useful to the developer
team. Developers may also want to read `tricks for configuring git
<configuring_git.html>`_.


- When and when not to force push

Resolving Merge Conflicts
~~~~~~~~~~~~~~~~~~~~~~~~~
Hopefully I'll get one in this document so I can add it to this section

Rebasing and Squashing Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Often a developer will check out a new branch and while they are working on the
branch different changes will be merged into develop. To pick up changes on
develop, check out the working branch and run the following:

.. code::shell
	$ git checkout fancy-changes
	$ git rebase develop

This will add all of the changes merged into develop since the branches
diverged onto ``fancy-new-changes``.

Sometimes a series of commits should be combined into one large commit. This
can be useful when there were many "work in progress" commits which do not need
to clutter the git history. This is called squashing commits. First, find the
oldest commit hash which should be squashed using ``git log``, in this example
``abcde12345``. Then run:

.. code::shell
	$ git rebase -i abcde12345 # i stands for interactive

Git will open up the editor and provide detailed instructions on how to choose
which commits to keep or combine.

Cherry Picking
~~~~~~~~~~~~~~
Sometimes it will be necessary to move several commits from one branch to
another. This can be achieved simply by using ``git cherry-pick``. First, check
out the branch which the commits will be moved to. Then, find the hash
representing the commit using ``git log``, for example ``abcde12345``, and run:

.. code::shell
	$ git cherry-pick abcde2345

This will add commit ``abcde12345`` to the current branch.


When Disaster Strikes
~~~~~~~~~~~~~~~~~~~~~
On occasion disaster will strike, and it will appear that all has been lost. It
is important not to panic, such mistakes can often be resolved with ``git
reflog``. As long as the ``.git`` folder is intact, git keeps a log of the
the changes made to the repository. Running ``git reflog`` will show a summary
of recent actions on the repository. Choose the hash representing the state
which should be restored to, for instance ``absde12345`` and run ``git reset
abcde12345``.


Common Python Errors and How to Fix Them
----------------------------------------
- I can't think of any...

Writing the Chef Cookbook
-------------------------

- Pretty much the same as the rest of the project
- Setting up test kitchen (link to updated internal chef docs)
- Create the git repo
- Create the issue tracker
- Create the project skeleton with Berks

Writing Chef Tests
------------------

- Serverspec
- A test cookbook
- A Rakefile?
- Bats?

How to Write a Recipe
---------------------

- How to add dependencies
- How to use a LWRP

How to Write a Light Weight Resource Provider
---------------------------------------------

- What is an LWRP and how are they useful
- Write a resource
- Write a provider

Common Chef Errors and How to Fix Them
--------------------------------------

Google Summer of Code
---------------------
The OSL has been part of the `GSoC
<https://www.google-melange.com/gsoc/homepage/google/gsoc2015>`_ since 2006.
This program has linked thousands of students from around the world with hundreds
of open source projects resulting in millions of lines of additional code.
Just about every development project at the OSL is available for students around
the world to join, as long as qualified mentors are available for the duration
of the program.  Any devs contributing to projects that are also being worked
on by a GSoC student should keep the following things in mind:

- The student is new.
  Their skillsets may not be as strong as other devs in areas like source
  control, documentation, IRC etiquette or deployment.  Patience and
  understanding will be greatly appreciated.  Help them become the kind of
  developer and team member the OSL would want to hire.
- Coordinate big changes with mentors.
  If the project has significant changes on the horizon, fellow devs should
  keep the mentor up-to-date on those changes to keep from blindsiding the
  student.  It is hard enough for the student to learn a new workflow;
  minimizing "surprises" is just common courtesy.

Related Documents:
------------------
.. toctree::
    :maxdepth: 1
    :glob:

    *
