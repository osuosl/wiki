Google Summer of Code 2013 Ideas
================================

.. note::

  This page is kept for historical purposes. Please check the latest year's
  ideas page for the most up to date information.

Welcome to the Oregon State University Open Source Lab Google Summer of Code
Ideas page.  

Ganeti Web Manager
------------------

`Ganeti Web Manager`__ is a Django based web application that allows
administrators and clients access to their `Ganeti virtualization clusters`__.
Through Ganeti Web Manager users can deploy and manage virtual servers.  Ganeti
Web Manager is being built by the Open Source Lab to support `Supercell`__, a
testing cloud for open source projects.

.. __: http://code.osuosl.org/projects/ganeti-webmgr
.. __: http://code.google.com/p/ganeti/
.. __: http://supercell.osuosl.org

If you would like to get started with playing with Ganeti, we recommend you
checkout our `Ganeti Vagrant Development/Testing Environment`__ (look at the
README for instructions). It uses VirtualBox to create a small Ganeti cluster on
your own computer so you can understand the basics. Additionally we recommend
you read the `Ganeti Walk-through documentation`__ to familiarize yourself with
Ganeti. You can also checkout this `Ganeti Tutorial Guide`__ to do some hands on
command line familiarization. 

.. __: https://github.com/ramereth/vagrant-ganeti
.. __: http://docs.ganeti.org/ganeti/current/html/walkthrough.html
.. __: http://www.lancealbertson.com/wp-content/uploads/2012/06/GanetiTutorialPDFSheet.pdf

Visit our irc channel **#ganeti-webmgr** on freenode for help getting started. 

Projects
~~~~~~~~

These projects are only suggested by us. Please feel free to look at the `GWM
Issue Tracker`__ for more ideas for projects. But please discuss any ideas with
us first.

.. __: https://code.osuosl.org/projects/ganeti-webmgr/issues

`Bulk Operations`__
^^^^^^^^^^^^^^^^^^^

.. __: http://code.osuosl.org/issues/2745

*Please talk with us about this project before submitting your proposal.*

We have started working on some of the Bulk operation tasks but this project
would likely be mostly focused on the `Bulk VM Creation`__ feature. This will
require quite a bit of thought on how the UI works and how it will interact with
the templating system we've implemented.

.. __: https://code.osuosl.org/issues/2751

`Add visualization of clusters, nodes, and or virtual machines`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. __: http://code.osuosl.org/issues/9537 

This would be for visualizating how the cluster works and how the virtual
machines and nodes interact. It does not use any real-time monitoring data other
than what Ganeti provides itself. The goal is to help cluster admins see how
their cluster is doing from a visual point of view.

Implement a mobile site
^^^^^^^^^^^^^^^^^^^^^^^

Currently GWM does not offer any mobile site solution. The goal of this project
would be to create a mobile version of some of the basic features GWM provides.
It wouldn't offer access to the console for example, but at least access to
control the VM's power state, see cluster status, deploy a new VM, etc. 

Vagrant
-------

`Vagrant`__ is an open source tool that we use at the lab quite a bit. It
currently supports `VirtualBox`__ and now more recently VMWare. Vagrant itself
is still in a bit of flux over this so we may need to work with upstream on the
viability of adding this feature.

.. __: http://www.vagrantup.com/
.. __: https://www.virtualbox.org/

.. _source/soc/ideas2013#projects:

Projects
~~~~~~~~

Add Ganeti provider to Vagrant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The project would be to create a `Ganeti`__ provider for Vagrant which will
allow users to power their virtual machines from a ganeti cluster instead of
depending on their local workstation. This is ideal for use cases such as
testing an environment with hundreds of VMs. Vagrant upstream recently made a
change to their code to that `writing a provider would be possible`__.  Ganeti
provides an `Remote API (RAPI)`__ to manage a cluster from however it doesn't
quite line up with a lot of other providers. 

.. __: http://code.google.com/p/ganeti/
.. __: http://docs.vagrantup.com/v2/plugins/providers.html
.. __: http://docs.ganeti.org/ganeti/current/html/rapi.html

The scope of the project would likely be:

- Write a basic provider that connects to the RAPI and can deploy/connect to a
  virtual machine using the normal Ganeti deployment strategy.
- Try to add other vagrant specific features if the RAPI supports it directly.
- Attempt to implement importing of boxes into Ganeti (this may not be easily
  possible).

Openconferenceware-Android
--------------------------

`Openconferenceware-android`__ is an open source project we started three years
ago to provide an android conference app for Open Source Bridge. Since then its
unfortunately been neglected by us and has been mostly taken care of by Igal's
`fork of OCW-Android`__. It was also used at OSCON in 2010. Please also take a
look at the `project page`__ for background info and documentation.

.. __: https://github.com/osuosl/ocw-android
.. __: https://github.com/igal/opensourcebridge-android
.. __: https://code.osuosl.org/projects/ocw-android

We intend to re-launch the project and try to merge in the changes that Igal and
others have done to try and unify the project.

Projects
~~~~~~~~

Some of these can be merged into one large task:

Merge all forked code into a unified code-base
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test all the code from various forks and try to merge any useful features or
commits. Try to generalize any site specific code that might be included in the
other projects. Update the documentation.

Add new useful features
^^^^^^^^^^^^^^^^^^^^^^^

We don't have any specific features we'd like to add but taking a look at the
various issue trackers might be a good place to start.

Make the app more flexible to other conference data formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Right now the application will only work with `Openconferenceware's`__ data
format which isn't very flexible. In the past we wrote a small Django
application called `ocw-android-oscon-dataservice`__ which screen scraped the
OSCON site to generate a format that worked. Its not the most ideal solution but
it worked at the time. It would be nice to have a more unified way to make this
work whether you're using Drupal to run a conference or whatever else.

.. __: https://github.com/igal/openconferenceware
.. __: https://github.com/osuosl/ocw-android-oscon-dataservice

.. _source/soc/ideas2013#ganeti_instance_image:

Ganeti Instance Image
---------------------

`Ganeti Instance Image`__ is a guest OS definition for Ganeti that uses either
filesystem dumps or tar ball images to deploy instances. The goal of this OS
definition is to allow fast and flexible installation of instances without the
need for external tools such as debootstrap. It was originally based on
`ganeti-instance-debootstrap`__.

.. __: https://code.osuosl.org/projects/ganeti-image
.. __: https://code.google.com/p/ganeti/

Projects
~~~~~~~~

- `Add support for OS Parameters <http://code.osuosl.org/issues/9549>`_
- `Add support for shared file <https://code.osuosl.org/issues/12159>`_

Ganeti
------

`Ganeti`__ is an open source project run by Google and used heavily at the lab.
It provides a manangement layer on open of various open source hypervisors such
as KVM and Xen to provider a stable virtualization platform.

.. __: http://code.google.com/p/ganeti/

Projects
~~~~~~~~

Improve support for LXC hypervisor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently Ganeti has limited support for `LXC`__ and has an open `feature bug`__
for improving the support. We'd like to work with the upstream project and have
a GSoC student work on improving this feature. This would require quite a bit
of knowledge of how LXC and Ganeti works so only advanced students need apply.
They would likely need to know a fair bit about python as well and possibly a
little bit of haskell.

.. __: http://lxc.sourceforge.net/
.. __: http://code.google.com/p/ganeti/issues/detail?id=249

Other OSL Projects
------------------

We have other projects that you might be interested in however we don't have a
specific idea in mind for GSoC. You might take a look at their issue trackers
and see if any of them interest you. Some are old projects that we haven't
touched in a while because of other priorities so please keep that in mind.

Protein Geometry Database (PGD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Protein Geometry Database`__ is a specialized search engine for protein
geometry. It allows you to explore either protein conformation or protein
covalent geometry or the correlations between protein conformation and bond
angles and lengths. It is primarily a django project with a lot of javascript
logic built into it. This project is a joint venture between the OSUOSL and the
`Oregon State University Biochemistry department`__ on campus.

.. __: https://code.osuosl.org/projects/pgd
.. __: http://biochem.science.oregonstate.edu/

Feel free to take a look at the `PGD Issue Tracker`__ for ideas but *please
discuss any potential ideas with us first before pursuing them*.

.. __: https://code.osuosl.org/projects/pgd/issues

Touchscreen
~~~~~~~~~~~

`Touchscreen`__ is a framework for developing interactive kiosk displays.
Touchscreen powers the display screen used outside the Open Source Lab's server
room. We use a 42" LCD flat screen, with a 17" touchscreen display to control
it. Screens are built using HTML, CSS, and Javascript and the backend is powered
via Django. Touchscreen was a :ref:`GSoC 2010 <gsoc2010-touchscreen20>` project
and was very successful.

.. __: https://code.osuosl.org/projects/touchscreen

Unfortunately over time the project has been left unmaintained due to staff time
and it horribly outdated (i.e. still uses a very old version of Django). We
would like to revive the project with some renewed focus. Please take a look at
the project and discuss with us any ideas you are interested in.

