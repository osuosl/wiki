1. How a Project is Written
===========================
This is a guide for writing a Django website. It will not cover
how to write a website using Flask because the process is nearly identical.


How the Developer Team Interacts With Clients
---------------------------------------------
The needs of clients vary a surprising amount. The developer team is expected
to modify the development and maintenance schedule to suit the specific needs
of each customer. In the past, the OSL has adopted the agile methodology for
working with the BSG and the Sea Grant foundation. This contrasts with the more
conservative development and release cycle of the Protein Geometry Database,
where every major change and new release must be certified by scientists.

For the What's Fresh and Working Waterfronts websites, the developer team chose
to follow the agile methodology. The agile method promotes quick responses to
change and customer collaboration, which made it an ideal fit for working with
both the Sea Grant Foundation and the BSG on an integrated website and mobile
application. The agile development methodology is defined in the `Agile
Manifesto`_, which is required reading for
all developers, should the team choose to follow this methodology. When
following the agile methodology, the developer team meets every month to
discuss the state of the project and show their progress to the client. The Sea
Grant projects also followed the test driven development model, which dictates
that tests should be written before code. This ensures that all of the code is
tested and works properly.

The PGD project has a very different set of constraints. It is a large project
that is being maintained, but with little active development being done. The PGD
is a tool used by hundreds of scientists throughout the world, so it is very
important that changes do not introduce bugs which may affect ongoing research.
Every change to the PGD project must be approved by the scientists in charge of
the project. It is difficult to write tests to ensure that new changes don't
impact the science. Historically the PGD has had issues with upstream protein
repositories and antiquated closed-source dependencies. Even importing new data
can sometimes be a fraught process, but the team is developing a detailed
process to minimize problems when upstream software or data changes.

.. _Agile Manifesto: http://www.agilemanifesto.org/

Setting Up the Project
----------------------

Create the git repo:
~~~~~~~~~~~~~~~~~~~~

Unless instructed to do otherwise, or given
special permission in the `OSL organization github
<https://github.com/osuosl>`_, ask a full-time employee to make the repository.
All the repositories for the OSL should be owned by the OSL. Developers should
not make a repository under their own account. Once the repo is created use ``$
git clone <SSH URI>`` to start working on the project.

On some projects, the client will have their own Github organization, such as
the `OSU CASS`_ and `ORVSD`_. In that case, open the project under their
organization.

.. _OSU CASS: https://github.com/osu-cass/
.. _ORVSD: http://github.com/orvsd/

Create the project skeleton with Django
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Django <https://www.djangoproject.com/>`_ is a powerful python web
application framework that makes building web applications much
easier.  Framework is just a fancy word for "lots of helpful tools
that make life easier".  Django has `excellent documentation
<https://docs.djangoproject.com/en/1.7/>`_ and `tutorials
<https://docs.djangoproject.com/en/1.7/intro/tutorial01/#creating-a-project>`_
that are well worth looking at. To begin a project, get to the directory where
the site will live and run ``$ django-admin.py startproject mysite``.  Now the
skeleton of the project is ready to go!  Add, commit, and push it to github as
an initial commit if appropriate.

Create the Dockerfile
~~~~~~~~~~~~~~~~~~~~~

Docker is a tool for putting discrete parts of an application on their own
pretend operating systems. This is called containerization. The upshot is that
different parts of an application, like a web application and a database, don't
need to be configured together. Often off-the-shelf containers can be used
instead of developing custom solutions. One of Docker's biggest advantages for
developers is its speed -- rebuilding a development version of a website with
Docker takes seconds as opposed to the 20 minutes Chef may need to converge.
Writing a Dockerfile is easy. Here is a simplified example from the PGD
project:

.. code:: text

	FROM centos:7

	MAINTAINER OSU OSL support@osuosl.org

	EXPOSE 8000

	RUN yum update && yum install -y \
	  cairo \
	  gcc \
	  gcc-c++ \
	  git \
	  libcairo-devel \
	  libffi \
	  libffi-devel \
	  mysql \
	  mysql-devel \
	  osuosl-dssp \
	  pycairo \
	  python-setuptools \
	  python-devel

	RUN easy_install pip

	# Copy and configure pgd
	WORKDIR /opt/pgd
	# Copy requirements.txt separately for better caching
	COPY ./requirements.txt /opt/pgd/requirements.txt
	RUN pip install -r requirements.txt
	# NB: copying the settings file is not a good idea when using volumes!
	COPY . /opt/pgd/
	RUN cp /opt/pgd/settings.py.dist /opt/pgd/settings.py

	CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

More about writing Dockerfiles can be found in the `Docker documentation`_.
Docker also has a `document`_ specifying best practices.

.. _Docker documentation: http://docs.docker.com/reference/builder/
.. _document: https://docs.docker.com/articles/dockerfile_best-practices/

Create a Virtualenv:
~~~~~~~~~~~~~~~~~~~~

Virtual environments are a pythonic way of containing dependencies within a
project. Virtualenvs are directories with their own version of Python, Pip, and
all of the packages a python application needs. Virtual environments should
probably have a descriptive name and be project specific. Many developers
prefer to keep them in one place, such as ``~/.my_venvs/``. To create a virtual
environment for a project such as What's Fresh, run ``virtualenv
~/.my_venvs/whats_fresh``. A new directory will be created at that location.
Virtual environments must be activated to be used by running ``$ source
~/.my_venvs/whats_fresh/bin/activate``.  Once a virtual environment has been
activated, dependencies can be installed as usual. To install all of the
dependencies listed in a project's ``requirements.txt`` file, run ``$ pip
install -r requirements.txt``. Once finished with the virtual environment, run
``$ deactivate``.  More detailed documentation can be found in the
`python guide <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.


Create the project's default branch (if not master):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some projects use a different default branch than master. For instance, the
What's Fresh project had ``develop`` as its default branch before it was released.
`To set the project's default branch`_ on Github, use the repositories settings
(the little screwdriver in the sidebar). Remember that the branch needs to
exist first before it's made the default!

.. _To set the project's default branch: https://help.github.com/articles/setting-the-default-branch/

The Development Process
-----------------------

Developers will spend most of their time in the feedback loop which is the
development process. It begins by going to the issue tracker and picking an
open issue. In general, it is best to consult the project lead on which issues
are the highest priority. Issues should also document their dependencies on
other issues and pull requests, but look out, because sometimes they do not.

Create a new branch. Give the branch a descriptive name which is easy to
tab complete and has the issue number it fixes. A common naming scheme among
OSL projects is: ``<descriptive name>/<issue type>/<issue number>``. Having a
descriptive name in front makes the branch easy to tab complete. Having the
issue type makes it very clear whether the issue is a feature or a
bug, and the issue number indicates what issue the branch belongs to in the
issue tracker. 

.. note::

    Developers should branch off of the ``develop`` branch, not
    ``master``. Once it is time to make a release, ``develop`` will be merged into
    ``master``.

Now that a new branch has been checked out, start writing tests. Only after
tests have been written should the code be written. Once the code is at a point
where others' advice is useful, make a pull request. Typically, several
developers or sysadmins will review the code and make comments. Once everyone
is satisfied with the PR and two people have signed off by giving their ``+1``,
the code can be merged. If the issue number has been mentioned in the pull
request's conversation, then Github will automatically close it. Check to make
sure that it has been closed anyway since the system is not foolproof. Once the
issue has been closed, go back and choose a new issue.


How to Write Python for Humans
------------------------------

A lot of the work here at the Open Source Lab involves reading other people's
code. To make this process less painful for everyone involved, it's best to
standardize how code is written. Python also has interesting idioms -- like
decorators -- which are not common in other languages that the Django framework
makes extensive use of.


PEP8, and how to check for it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PEP8`_ is the "Style Guide for Python Code". Essentially, it's a document
detailing how to write Python that's homogeneous and easy to read. It's a long
document -- here are some of the more important, more common bits.

.. _PEP8: https://www.python.org/dev/peps/pep-0008/

1. Limit lines to 79 characters
```````````````````````````````

Lines that are too long get hard to read. If a line is more than 79
characters long, break it to the next line:

.. code-block:: python

  # Don't do this
  data = json.loads(serializer.serialize([preparation], use_natural_foreign_keys=True))

  # Do this
  data = json.loads(
      serializer.serialize(
          [preparation],
          use_natural_foreign_keys=True
    ))

  # Or this
  data = json.loads(
      serializer.serialize([preparation],
                           use_natural_foreign_keys=True
                          )
  )


When breaking just after an open-parenthesis, go in by four spaces as shown
in the first example. When breaking after a parameter, put the second parameter
indented to the same level as the first. The most important part to remember,
though, is that the code should be *readable*. Don't confuse future readers as
to what gets passed to what.

2. Indentation
``````````````

Use four spaces per indentation level. Don't use tabs. Any text editor
can be configured to insert spaces when tab is pressed. Do not leave trailing
whitespace at the end of lines or on otherwise blank lines.

3. Blank lines
``````````````

Put two blank lines in between classes and in between functions. Put one blank
line in between methods. This helps the reader understand how the code is
logically organized.

Docstrings
~~~~~~~~~~

Docstrings are comments that appear at the top of a function, class, or other
definition. Says `PEP 257`_, the Python Docstring Conventions document:

  All modules should normally have docstrings, and all functions and classes
  exported by a module should also have docstrings. Public methods (including
  the __init__ constructor) should also have docstrings.

Docstrings appear as triple-quoted strings at the top of a definition. If
they're one line long, the quotes can be on the same line as the comment; if
they're multiple lines, the first should be a quick summary, followed by a
blank line and the rest of the docstring.

.. _PEP 257: https://www.python.org/dev/peps/pep-0257/

Example docstrings from the PEP 257:

.. code-block:: python

  def complex(real=0.0, imag=0.0):
      """Form a complex number.

      Keyword arguments:
      real -- the real part (default 0.0)
      imag -- the imaginary part (default 0.0)
      """
      if imag == 0.0 and real == 0.0:
          return complex_zero
      ...

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

The Lab uses yaml-based configuration for many of its Django projects. This
makes the configuration easier to read, and in general, allows a slightly greater
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

Applications live in a subdirectory of the project. That is to say, if the project
is named ``project``, and the app is named ``app``, the directory structure will
look something like this::

  manage.py
  project/
    /project/settings.py
    /app/models.py

Example Model
~~~~~~~~~~~~~

A model consists of everything one might need to store about an object in a
database. Imagine a blogging platform that allows users to share public posts
and write private posts. The ``models.py`` for such a blog might include
something like this:

.. code-block:: python

  from django.db import models


  class Entry(models.Model):
      """This docstring contains information about the model."""
      name = models.CharField(max_length=100)
      text = models.TextField()
      created = models.DateTimeField(auto_now_add=True)
      public = models.BooleanField(default=False)

      def __unicode__(self):
          """Returns Entry's name

          The __unicode__ function allows Django to print which object
          is being dealt with. It uses this when it prints the object,
          or just puts the object in the template.
          """
          return self.name


Example View
~~~~~~~~~~~~

Imagine the same blog platform from before. The following view might be used
to view the details of an entry:

.. code-block:: python

  def entry(request, id=None):
      """ /entry/<id> method. Handles private/public entry page requests

      If the user is authenticated, this returns the details page for the
      requested entry. If the user is not authenticated, and it is a private
      post, the user is redirected to the login page.
      """
      entry = get_object_or_404(Entry, pk=id)
      if not entry.public and not request.user.is_authenticated():
          return HttpResponseRedirect(reverse('login'))
      return render(request, 'entry.html', {'entry': entry})

Here's another example view, this one used to create new Entries. Note that
this view can handle both GET requests, which are for the form before it's
been filled out, and POST requests, which save the form.

.. code-block:: python

  @login_required
  def new(request):
      """/entry/new. Handles new entry creation for auth'd users

      The form for creating a new entry. On a GET request, this returns the
      form that can be used to save the entry. On a POST request, it checks
      the validity of the form, and if it's valid, saves and redirects the
      user to its details page.
      """
      form = EntryForm(request.POST or None)
      if form.is_valid():
          entry = form.save()
          return HttpResponseRedirect(
              reverse('entry-details',
                      kwargs={'id': entry.id}))
      return render(request, 'new.html', {'form': EntryForm})

Notice the ``@login_required`` above the view function. This is a decorator,
a special Python function that "wraps" the function it's above. In this case,
Django's ``login_required`` decorator is being used. This decorator will make
sure the user is authenticated before running the view, and if they are not,
will redirect them to the login page.


Automated testing with Travis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automated testing with Travis CI is an incredibly powerful tool. Travis is a
continuous integration tool, meaning it's designed to run every time someone
pushes commits to a repository. In our case, it integrates directly into GitHub
and runs all of our tests, allowing code reviewers to see if a pull request
breaks something or if a merge went horribly, horribly wrong.

To set up Travis CI, make a ``.travis.yml`` file in the root of the repository.
It should look something like this::

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
database and extension needed for the app. The ``script`` is the actual test
run itself. If either command fails, the "build" will fail, and Travis will
report that it is not safe to merge.

Using the flake8 Python Linter in CI forces the team to keep code clean and
easy to read.

Writing Docs
------------

The OSL writes docs using the Sphinx Documentation generator. Write docs in the
Restructured Text format. There are `useful docs`_ for the restructured text
format as well as a handy `cheat sheet`_.

Sphinx is a Python package and should be included in the project's
``requirements.txt``. If the project doesn't have docs, add a docs directory
with the quick start script: ``sphinx-quickstart``.

To build the docs, run ``make html``. The generated docs will be in the
``build`` directory.

All API endpoints and error messages should be thoroughly documented. Error
messages should be clear, grepable and Googleable by outside developers. The
text of error messages should be explicitly included in documentation

All configuration variables and values should be throughly documented. Be sure
to include a description of possible values and problematic values.

Any instructions or tutorials should be vetted by other team members,
especially junior developers.

There are plenty of automated tools to make sure prose is easy to read. The
best is probably the `Hemingway app website`_. There is also a CLI called
`write-good`_ which will catch some common errors but is nowhere near as thorough.

.. _useful docs: http://sphinx-doc.org/rest.html
.. _cheat sheet: https://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _Hemingway app website: hemingwayapp.com
.. _write-good: https://github.com/btford/write-good

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

- **The student is new.**
  Their skillsets may not be as strong as other devs in areas like source
  control, documentation, IRC etiquette or deployment.  Patience and
  understanding will be greatly appreciated.  Help them become the kind of
  developer and team member the OSL would want to hire.
- **Coordinate big changes with mentors.**
  If the project has significant changes on the horizon, fellow devs should
  keep the mentor up-to-date on those changes to keep from blindsiding the
  student.  It is hard enough for the student to learn a new workflow;
  minimizing "surprises" is just common courtesy.
