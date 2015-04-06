
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
application. The agile development methodology is defined in the `Agile
Manifesto`_, which is required reading for
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
can sometimes be a fraught process, but the team is developing a detailed
process to minimize problems when upstream software or data changes.

.. _Agile Manifesto: http://www.agilemanifesto.org/

Tools We Use
------------
At the OSL developers use a variety of open source tools. Developers are expected to
have at least passing familiarity with all of these tools. New developers are
encouraged to research any of these tools they have not heard of.

Most OSL websites are written in Python using the Django web application
framework. Websites are deployed using Chef configuration management on CentOS
6.6. Most of our sites use the MySQL database, although some use PostGres.
Most OSL websites have a Docker development environment set up to make
development fast and easy. To learn how to use the Docker development
environment please consult the project documentation and the OSL's `internal
documentation`_.
The OSL uses ``git`` for version control and keeps projects on
GitHub_. The OSL uses the RedMine_ issue tracker because GitHub does not
support tracking how much time was spent on individual issues.

.. _internal documentation: https://docs.osuosl.org/development/docker-dev-environments.html
.. _GitHub: https://github.com/osuosl
.. _RedMine: https://code.osuosl.org

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

How to Write Python for Humans
------------------------------

A lot of the work here at the Open Source Lab involves reading other people's
code. To make this process less painful for everyone involved, it's best to
standardize how code is written. Python also has interesting idioms, like
decorators, which are not common in other languages, which the Django framework
makes extensive use of.


PEP8, and how to check for it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PEP8 is the "Style Guide for Python Code". Essentially, it's a document
detailing how to write Python that's homogeneous and easy to read. It's a long
document -- here are some of the more important, more common bits.

1. Limit lines to 79 characters
```````````````````````````````

Lines that are too long get hard to read. If a line is more than 79
characters long, break it to the next line:

.. code-block:: python

  # Don't do this
  data = json.loads(serializer.serialize([preparation], use_natural_foreign_keys=True)

  # Do this
  data = json.loads(
      serializer.serialize(
          [preparation],
          use_natural_foreign_keys=True
    )

  # Or this
  data = json.loads(
      serializer.serialize([preparation],
                           use_natural_foreign_keys=True
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

Put two blank lines in between classes, and in between functions. Put one blank
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

The lab uses yaml-based configuration for many of its Django projects. This
makes the configuration easier to read, and in general allows a slightly greater
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
database. Imagine a blogging platform that allows users to share public posts,
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
          or just put the object in the template.
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
Django's login_required decorator is being used. This decorator will make sure
the user is authenticated before running the view, and if they are not, will
redirect them to the login page.


Automated testing with Travis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automated testing with Travis CI is an incredibly powerful tool. Travis is a
continuous integration tool, meaning it's designed to run every time someone
pushes commits to a repository. In our case, it integrates directly into GitHub
and runs all of our tests, allowing code reviewers to see if a pull request
breaks something, or if a merge went horribly, horribly wrong.

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

How to Git Out of a Tight Corner
--------------------------------
Git is a powerful tool which is generally easy to use, but sometimes it is
possible to wind up in a weird state. This section of the document describes
some intermediate level features of git which may be useful to the developer
team. Developers may also want to read `tricks for configuring git
<configuring_git.html>`_.


When to Use the Powers of the Force
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sometimes changes are made which affect the past history of the local branch,
and when these changes are pushed to GitHub or another git server they will be
rejected because the history on the server does not match the local history. A
common example is rebasing a branch to pick up new changes, which is detailed
further in the next section. The server can be made to accept these changes
with the ``--force`` flag, but be careful! Force pushing is a dangerous
operation which will permanently rewrite history on the server. Junior
developers should consult more experienced colleagues before force pushing.

Developers must always use a fully qualified push command when force pushing,
naming both the git remote and branch. To force push to a branch named
``branch`` run

.. code:: bash

	git push --force origin branch

Do NOT run

.. code:: bash

	git push --force

Resolving Merge Conflicts
~~~~~~~~~~~~~~~~~~~~~~~~~
Hopefully I'll get one in this document so I can add it to this section

Rebasing and Squashing Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Often a developer will check out a new branch and while they are working on the
branch different changes will be merged into develop. To pick up changes on
develop, check out the working branch and run the following:

.. code:: bash

	$ git checkout fancy-changes
	$ git rebase develop

This will add all of the changes merged into develop since the branches
diverged onto ``fancy-new-changes``.

Sometimes a series of commits should be combined into one large commit. This
can be useful when there were many "work in progress" commits which do not need
to clutter the git history. This is called squashing commits. First, find the
oldest commit hash which should be squashed using ``git log``, in this example
``abcde12345``. Then run:

.. code:: bash

	$ git rebase -i abcde12345 # i stands for interactive

Git will open up the editor and provide detailed instructions on how to choose
which commits to keep or combine.

Cherry Picking
~~~~~~~~~~~~~~
Sometimes it will be necessary to move several commits from one branch to
another. This can be achieved simply by using ``git cherry-pick``. First, check
out the branch which the commits will be moved to. Then, find the hash
representing the commit using ``git log --all``, for example ``abcde12345``,
and run:

.. code::shell
	$ git cherry-pick abcde2345

This will add commit ``abcde12345`` to the current branch.


When Disaster Strikes
~~~~~~~~~~~~~~~~~~~~~
On occasion disaster will strike, and it will appear that all has been lost. It
is important not to panic, such mistakes can often be resolved. As long as the
``.git`` folder is intact, git keeps a log of the changes made to the
repository. If a change is made which affects git history, the hash of the
commit previous to the change will be stored in the special file
``.git/ORIG_HEAD``, for instance ``absde12345``. To go back to that commit, run
``git reset abcde12345``.


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

Just like Python code, tests are required for Chef cookbooks. Tests will help
ensure that new changes don't accidentally break existing functionality in
unexpected ways. Chef tests generally fall into two categories, unit testing
with ChefSpec, and integration testing with ServerSpec.

Test Kitchen
~~~~~~~~~~~~
`Test Kitchen`_ provides a standardized environment in which to develop
infrastructure code. Test kitchen can spin up a virtual machine on the
OpenStack cluster or locally using Vagrant. Test kitchen will converge the chef
cookbook and run any Serverspec_ and Chefspec_ tests. To start using test
kitchen with a cookbook, run the following:

.. code:: bash

    $ kitchen init
          create  .kitchen.yml
          create  test/integration/default
    Successfully installed kitchen-vagrant-0.15.0
    Parsing documentation for kitchen-vagrant-0.15.0
    1 gem installed
    $ ls -a
    .  ..  .kitchen/  .kitchen.yml  test/

`kitchen init` will add a .kitchen.yml file, a .kitchen directory, and a test
directory. The .kitchen.yml file specifies how to create a given virtual
machine and which recipes to converge it with. Kitchen is configured for the
project, the following commands can be used:

.. code:: text

    $ kitchen converge      # Runs the cookbook in a given VM, similar to `vagrant up`.
    $ kitchen destroy       # Destroys the VM, similar to `vagrant destroy`.
    $ kitchen verify        # Runs a given test suite for the project.
    $ kitchen test          # Converges the cookbook, runs tests, then destroys the VM if the tests pass.

Often a project will need to be run on specific operating systems with
different recipes. These options are specified in the `.kitchen.yml` file. Most
projects will also have a `.kitchen.cloud.yml` file which instructs kitchen how
to spin up a virtual machine on OpenStack instead of using Vagrant.
More information about how the various options in this config file can be found
in the `Chef Documentation about kitchen`_.

.. _Chef Documentation about kitchen: https://docs.chef.io/config_yml_kitchen.html

Using Test Kitchen With OpenStack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running Vagrant on the workstations is slow, and it is not uncommon for virtual
machines to hog resources or be killed and become corrupted. It's often faster
and easier to spin up virtual machines on the Lab's OpenStack cluster. The Lab
has extensive internal documentation on using `Test Kitchen with OpenStack`_.
After setting everything up, test kitchen will be just as easy to use, and
tests will run much faster.

.. _Test Kitchen with OpenStack: https://docs.osuosl.org/software/openstack/openstack_test_kitchen.html

ServerSpec Tests
~~~~~~~~~~~~~~~~
Serverspec_ is used to do `integration testing`_, that is, testing how all of
the pieces/modules/code works together. It is an implementation of RSpec_
tests for chef/puppet deployment. Tests are written in a declarative style to
check whether the cookbook put all the files in the right places, installed the
right packages, started the right daemons, etc. Here's a quick example from
their docs:

.. code:: ruby

    # In the file spec/target.example.jp/http_spec.rb
    # A typical ServerSpec test

    require 'spec_helper'

    describe '<name of the resource being tested>' do
      # tests ...
    end

Read the `Serverspec docs`_ for more info.

ChefSpec Tests
~~~~~~~~~~~~~~
Chefspec_ is used for `Unit Testing`_ which tests individual parts of
a Light Weight Resource Provider (see section below for more info on what a
LWRP is). Here's an example of a unit test from the yum chef cookbook:

.. code:: ruby

    require 'spec_helper'

    describe 'yum::default' do
      let(:chef_run) { ChefSpec::Runner.new.converge(described_recipe) }

      it 'creates yum_globalconfig[/etc/yum.conf]' do
        expect(chef_run).to create_yum_globalconfig('/etc/yum.conf')
      end

    end

Chef Linters
~~~~~~~~~~~~
Chef cookbooks need to be checked just like Python code to ensure they follow
style guidelines.


**Rubocop_** is a Ruby static code analyzer. Out of the box it will enforce
many of the guidelines outlined in the community `Ruby Style Guide`_. When
`rubocop` is run, it will lint the code, display errors, and describe how to
fix them. Rubocop can automatically fix many style errors, but this process is
not perfect and can lead to subtle bugs. Rubocop errors should generally be
fixed manually.

Some projects may also include a `.rubocop.yml`_ file for explicitly excluding
or including files to be analyzed by Rubocop.

**`Foodcritic`_** is a linter, like Rubocop, but it enforces style guidelines
specific to Chef cookbooks.  Foodcritic will check for conformance to `rules`_
outlined by the Chef community, such as FC002_

.. code:: bash

	$ foodcritic .
	FC002: Avoid string interpolation where not required:
	./providers/gunicorn.rb:89

.. code:: ruby

	# Don't do this:
	gunicorn_command = new_resource.virtualenv.nil? ? "gunicorn" :
	 "#{::File.join(new_resource.virtualenv, "bin    ", "gunicorn")}"
	# Do this instead:
	gunicorn_command = new_resource.virtualenv.nil? ? "gunicorn" :
	 ::File.join(new_resource.virtualenv, "bin    ", "gunicorn")



.. _Serverspec: http://serverspec.org/
.. _Serverspec docs: http://serverspec.org/tutorial.html
.. _Rake: http://docs.seattlerb.org/rake/
.. _Rubocop: http://batsov.com/rubocop/
.. _Ruby Style Guide: https://github.com/bbatsov/ruby-style-guide
.. _Test Kitchen: http://kitchen.ci/
.. _Rspec: http://rspec.info/
.. _integration testing: https://en.wikipedia.org/wiki/Integration_testing
.. _Unit Testing: https://en.wikipedia.org/wiki/Unit_testing
.. _Chefspec: http://sethvargo.github.io/chefspec/
.. _.rubocop.yml: https://github.com/osuosl-cookbooks/osl-haproxy/blob/master/.rubocop.yml
.. _Foodcritic: http://acrmp.github.io/foodcritic/
.. _rules: http://acrmp.github.io/foodcritic/

.. _FC002: http://acrmp.github.io/foodcritic/#FC002

How to Write a Recipe
---------------------

- How to add dependencies
- How to use a LWRP

How to Write a Light Weight Resource Provider
---------------------------------------------

A Light Weight Resource Provider, or LWRP, is a simple way to write custom
reusable components for configuration. For instance, one could copy a sysV init
file for apache into ``/etc/init.d`` in every cookbook which needs to setup
apache, or one could provide a resource which will set the status of the init
script, whether or not it is enabled etc., and automatically copies it over
for you.

.. code:: ruby

	service "apache" do
	  action [:enable]
	end

The implementation of an LWRP is split into two parts: a resource, which
declares the interface, and the provider, which is the logic executed when the
new resource is instantiated. LWRPs have a peculiar naming scheme which depends
both on the name of the cookbook and the name of the file. For instance, if the
``python-webapp`` cookbook has a provider in the file ``providers/common.rb``
and a resource in the file ``resources/common.rb`` it will have a LWRP called
``python_webapp_common``. It can be used like this:


.. code:: ruby

	python_webapp_common 'name goes here' do
	  # set attributes in here
	end

Note that if the LWRP is called ``default``, and has files in similar places,
the name of the LWRP will be ``python_webapp``.

How to Write a Resource
~~~~~~~~~~~~~~~~~~~~~~~

Resources are ruby files placed under the ``resources`` directory. Resources
define the attributes and default actions for an LWRP. Each attribute is a
hash, with a name, such as ``:path``, a ``'kind_of'``, which defines the type
of the attribute, and an optional default value. A resource should also specify
a default action.

.. code:: ruby
	# Put this file in resources/default.rb
	default_action :install

	attribute :path, 'kind_of' => String, 'default' => '/'
	attribute :on, 'kind_of' => [TrueClass, FalseClass], 'default' => true

How to Write a Provider
~~~~~~~~~~~~~~~~~~~~~~~

An LWRP needs a provider for each of its actions. A provider can have arbitrary
ruby code, and will likely use several other LWRPs. Often, the LWRP should
indicate that the resource was updated by the last action.


.. code:: ruby
	action :install do
	  if new_resource.on
	    # do things
	  end
	  # Create a file at the path using the file LWRP only if the on attribute
	  # is set
	  file "#{new_resource.path}/some_file" do
	    only_if { new_resource.on }
	    action :create
	  end
	  new_resource.updated_by_last_action(true)
	end


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
