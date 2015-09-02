2. How a Project is Deployed
============================

The OSL uses Chef Configuration Management to deploy all modern projects.
Writing a chef cookbook is very similar to writing the rest of the project. The
Lab has internal resources explaining how to write a cookbook, so this is just
a summary. A cookbook describes the desired state of a server. A cookbook may
have several recipes for different operating systems or for different parts of
the server's configuration. Cookbooks can use pieces of code from other
cookbooks called resources. Here is an abridged version of the What's Fresh
cookbook's default recipe:

.. code:: ruby

	directory node['whats_fresh']['config_dir'] do
	  owner node['whats_fresh']['venv_owner']
	  group node['whats_fresh']['venv_group']
	  recursive true
	end

	python_webapp 'whats_fresh' do
	  create_user true
	  path node['whats_fresh']['application_dir']
	  owner node['whats_fresh']['venv_owner']
	  group node['whats_fresh']['venv_group']

	  repository node['whats_fresh']['repository']
	  revision node['whats_fresh']['git_branch']

	  config_template 'config.yml.erb'
	  config_destination "#{node['whats_fresh']['config_dir']}/config.yml"
	  django_migrate true
	  django_collectstatic true
	  interpreter 'python2.7'

	  gunicorn_port node['whats_fresh']['gunicorn_port']
	end

	nginx_app 'whats_fresh' do
	  template 'whats_fresh.conf.erb'
	  cookbook 'whats-fresh'
	end

This recipe uses several resources, including ``python_webapp``, ``nginx_app``,
and ``directory``. The section ``node['whats_fresh']['application_dir']`` is
just like a python dictionary with a specific configuration value, often a
string.


The Architecture of Chef, Abridged
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chef has several parts: a central server, which holds all of the cookbooks, and
a collection of nodes, which are managed by the chef server. Each node has
attributes which are essentially a hash or a dictionary of configuration values
and keys. Each node has a list of roles it serves, like web server or database
server, and a run list of recipes it will run. Every half hour or so, each node
checks with the chef server and converges to the state which the chef cookbook
specifies. Sysadmins can edit the attributes of a node on the chef server using
the ``knife`` tool.

Anatomy of a Cookbook
~~~~~~~~~~~~~~~~~~~~~
Most cookbooks begin with a table of contents, but Chef cookbooks are full of
files. Here is a summary of important files in a cookbook.

.. code:: text

	.
	├── attributes: A directory that contains ruby files that set attributes
	├── Berksfile: Defines where to find other cookbooks
	├── chefignore: Like a .gitignore, lists files which Chef won't upload
	├── Gemfile: Lists gem dependencies like python's requirements.txt
	├── .kitchen.yml: Used for running Test Kitchen with Vagrant
	├── .kitchen.cloud.yml: Used for running Test Kitchen on openstack
	├── metadata.rb: Like the Berksfile, defines dependencies and cookbook info
	├── libraries: Stores arbitrary Ruby library code
	├── recipes: Recipes are ruby files instructing Chef how to configure a
	│   │        node
	│   └── default.rb
	├── resources: Resources define the interface of a Light Weight Resource
	│              Provider
	├── templates: Holds Emedded Ruby (erb) templates for config files, etc.
	│   └── default: Templates for the default recipe
	├── test: Holds Test Kitchen tests
	│   └── integration
	│       └── default: Tests for the default recipe
	│           └── serverspec: Serverspec test files
	└── Vagrantfile: Used for starting Test Kitchen VMs


Starting a New Cookbook
~~~~~~~~~~~~~~~~~~~~~~~

To begin a new project, first clone the Lab's generator cookbook.

.. code-block:: bash

	$ git clone https://github.com/osuosl-cookbooks/code_generator

Next generate a cookbook by running:

.. code-block:: bash

	$ berks cookbook new-cookbook-name -g /path/to/code_generator/repo

Berks will create a skeleton cookbook and git repository. It may be useful to
create a file called ``.kitchen.cloud.yml`` which specifies how to run `Test
Kitchen VMs on OpenStack`_. Commit the generated code, and ask for a new
repository to be created under the osuosl-cookbooks organization on GitHub.
Some developers may also need to ask for permission to join that organization
so they can commit code there. Follow Github's guide on `importing the code to
Github`_. Cookbooks should use the Github issue tracker.

Most projects will use the default recipe and possibly a handful of platform
specific recipes.

.. warning::
    Test Kitchen VMs on OpenStack links to internal documentation.

.. _Test Kitchen VMs on OpenStack: https://docs.osuosl.org/software/openstack/openstack_test_kitchen.html?highlight=test%20kitchen%20openstack#test-kitchen
.. _importing the code to Github: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/#platform-linux

Writing Chef Tests
------------------

Just like Python code, tests are required for Chef cookbooks. Tests will help
ensure that new changes don't accidentally break existing functionality in
unexpected ways. Chef tests generally fall into two categories, unit testing
with ChefSpec and integration testing with ServerSpec.

Test Kitchen
~~~~~~~~~~~~
`Test Kitchen`_ provides a standardized environment in which to develop
infrastructure code. Test Kitchen can spin up a virtual machine on the
OpenStack cluster or locally using Vagrant. Test Kitchen will converge the chef
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
project; the following commands can be used:

.. code:: text

    $ kitchen converge      # Runs the cookbook in a given VM, similar to `vagrant up`.
    $ kitchen destroy       # Destroys the VM, similar to `vagrant destroy`.
    $ kitchen verify        # Runs a given test suite for the project.
    $ kitchen test          # Converges the cookbook, runs tests, then destroys the VM if the tests pass.

Often a project will need to be run on specific operating systems with
different recipes. These options are specified in the `.kitchen.yml` file. Most
projects will also have a `.kitchen.cloud.yml` file which instructs kitchen how
to spin up a virtual machine on OpenStack instead of using Vagrant.
More information about the various options in this config file can be found
in the `Chef Documentation about kitchen`_.

.. _Chef Documentation about kitchen: https://docs.chef.io/config_yml_kitchen.html

Using Test Kitchen With OpenStack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running Vagrant on the workstations is slow, and it is not uncommon for virtual
machines to hog resources or be killed and become corrupted. It's often faster
and easier to spin up virtual machines on the Lab's OpenStack cluster. The Lab
has extensive internal documentation on using `Test Kitchen with OpenStack`_.
After setting everything up, test kitchen will be just as easy to use and
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
Chefspec_ is used for `Unit Testing`_, which tests individual parts of
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


`Rubocop`_ is a Ruby static code analyzer. Out of the box it will enforce
many of the guidelines outlined in the community `Ruby Style Guide`_. When
`rubocop` is run, it will lint the code, display errors, and describe how to
fix them. Rubocop can automatically fix many style errors, but this process is
not perfect and can lead to subtle bugs. Rubocop errors should generally be
fixed manually.

Some projects may also include a `.rubocop.yml`_ file for explicitly excluding
or including files to be analyzed by Rubocop.

`Foodcritic`_ is a linter, like Rubocop, but it enforces style guidelines
specific to Chef cookbooks.  Foodcritic will check for conformance to `rules`_
outlined by the Chef community, such as FC002_.

.. code:: bash

	$ foodcritic .
	FC002: Avoid string interpolation where not required:
	./libraries/gunicorn.rb:89

.. code:: ruby

	# Don't do this:
	gunicorn_command = new_resource.virtualenv.nil? ? "gunicorn" :
	 "#{::File.join(new_resource.virtualenv, "bin    ", "gunicorn")}"
	# Do this instead:
	gunicorn_command = new_resource.virtualenv.nil? ? "gunicorn" :
	 ::File.join(new_resource.virtualenv, "bin", "gunicorn")



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
.. warning:: This section is incomplete.

- How to add dependencies
- How to use a LWRP

How to Write a Light Weight Resource Provider
---------------------------------------------

A Light Weight Resource Provider, or LWRP, is a simple way to write custom
reusable components for configuration. They can be used to do things like:

- Automating common tasks in your chef cookbooks
- Automating complex tasks in your chef cookbooks

An LWRP lets you call dozens of lines of code into something as simple as:

.. code:: ruby

    service "apache" do
      action [:enable]
    end

.. For instance, one could copy a sysV init
   file for apache into ``/etc/init.d`` in every cookbook which needs to setup
   apache, or one could provide a resource which will set the status of the init
   script, whether or not it is enabled etc., and automatically copies it over
   for you.

The implementation of an LWRP is split into two parts: a resource, which
declares the interface, and the provider, which is the logic executed when the
new resource is instantiated. LWRPs have a peculiar naming scheme which depends
both on the name of the cookbook and the name of the file. For instance, if the
``python-webapp`` cookbook has a provider in the file ``libraries/common.rb``
and a resource in the file ``resources/common.rb`` it will have a LWRP called
``python_webapp_common``. It can be used like this:


.. code:: ruby

	python_webapp_common 'name goes here' do
	  # set attributes in here
	end

Note that if the LWRP is called ``default``, and has files in similar places,
the name of the LWRP will be ``python_webapp``.

*For more information on LWRPs, check out the official* `LWRP docs`_.

.. _LWRP docs: https://docs.chef.io/lwrp.html

How to Write a Resource
~~~~~~~~~~~~~~~~~~~~~~~

Resources are ruby files placed under the ``resources`` directory. Resources
define the attributes and default actions for an LWRP. Each attribute is a hash.
Each hash has a:

- name: This can be something like ``:path`` or ``:on``
- ``kind_of``: Which describes the type of the attribute like ``String`` or
  ``TrueClass, FalseClass``
- default value: What the value is set to if the user does not specify
  a value, like a filesystem path of true/false for a boolean

.. code:: ruby

	# Put this file in resources/default.rb
	default_action :install

	attribute :path, 'kind_of' => String, 'default' => '/'
	attribute :on, 'kind_of' => [TrueClass, FalseClass], 'default' => true

How to Write a Provider
~~~~~~~~~~~~~~~~~~~~~~~

An LWRP needs a provider for each of its actions. A provider can have arbitrary
ruby code and will likely use several other LWRPs. Often, the LWRP should
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
