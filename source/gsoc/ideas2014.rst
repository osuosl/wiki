Google Summer of Code 2014 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code
2014 idea page! Before applying please read over our :ref:`application guide
<gsoc-app-info>` for details specific to our organization.

Ideas
-----
- :ref:`gsoc2014-data-center-tools`
- :ref:`gsoc2014-ftp-mirror-syncing`
- :ref:`gsoc2014-osl-dashboard`
- :ref:`gsoc2014-ocw-android`
- :ref:`gsoc2014-centralized-osl-logging`
- :ref:`gsoc2014-other-projects`

.. _gsoc2014-data-center-tools:

Data Center Tools
~~~~~~~~~~~~~~~~~

Project: Infrastructure-wide IPMI Management Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explaination:**

We host a variety of systems in our data center which include a wide array of
vendors (i.e. Dell, HP, Sun, etc). Each of these machines utilize some type of
out-of-band (OOB) technology such as iLO or iDrac which allows direct access to
the machine power, console and other features. Unfortunately each OOB tool is
different between the command line access and the console access. However each
machine does support the IPMI standard which basically does the same thing.
There are several FOSS tools out there already that utilize IPMI in some
fashion, but none create a complete tool that stores a whole infrastructure into
an interface. This project would create a centralized application to connect to
each machine over IPMI.

**Expected Results**

Either a command line driven or web app driven interface that allows for
addition of machines, access to power, serial and vga console. Optionally show
event logs and any sensor data.

**Knowledge Prerequisite:**

General IPMI experience, basic understanding of production-grade server
hardware, ability to program in a programming language that works best with
IPMI.

**Mentor:** Lance (Ramereth)

------

.. _gsoc2014-ftp-mirror-syncing:

FTP Mirror Syncing
~~~~~~~~~~~~~~~~~~

Project: Re-architect OSL FTP Mirror Infrastructure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explanation:**

The OSL hosts a three-node FTP mirroring cluster to host various FOSS projects’
ISO images and package databases. Currently it comprises of some custom-made
bash scripts that utilize ssh, rsync and cron to coordinate the syncing process.
The architecture is a single master machine that syncs from upstream and then
triggers slave hosts to sync from it. This architecture has served us well over
the years but has limitations and needs updating to use more modern features.

There are a variety of methods for syncing the repositories but generally most
use rsync. Some have an ssh trigger system (i.e. Ubuntu/Debian) and others want
a post script to run to provide results upstream. Finally sometimes we are the
master mirror, meaning we are the starting point, so some projects either
manually upload and trigger a sync or we pull from a central source using cron.

In addition, we have some simple monitoring that should be updated. Ideally it
would be re-implemented as some type of dashboard showing any repo that is out
of sync, disk usage per repo over time, and some other simple statistics.

**Expected Results**

This project will look at the current architecture, research alternatives and
feature needs, design a new system and implement it. Preferably keeping the
system simple yet flexible and robust.

**Knowledge Prerequisite:**

General concepts of API design, mirror syncing technologies (rsync), proficient
in a language that fits with the design (possibly Python) and understand bash
(the current system uses bash a lot).

**Mentor:** Lance (Ramereth)

----

.. _gsoc2014-osl-dashboard:

OSL Dashboard
~~~~~~~~~~~~~

Project: Implement a status dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explanation:**

The OSL currently doesn’t have a system status dashboard. Historically, we
utilized some internal projects such as Touchscreen to have such a dashboard,
but they have been untouched for quite some time. Ideally we would like to
implement using something such as `dashing`_. We are hoping to incorporate a
variety of input data to show status on nagios alerts, bandwidth usage, FTP
mirror activity, and ticket queue statistics. In addition we hope to use this
dashboard at conferences as a way to showcase our project showing various cool
metrics. We already have a basic dashing board called `fenestra`_, but it has
little to no customization.

.. _dashing: http://shopify.github.io/dashing/
.. _fenestra: https://github.com/osuosl/fenestra

**Expected Results**

A fully functioning dashboard using dashing (or some alternative). This includes
the configuration of the project, any custom plugins that need to be written.

**Knowledge Prerequisite:**

Understanding of Ruby and the related technologies used by dashing. Basic API
understanding. Logging.

**Mentor:** Ken (kennric)

----

.. _gsoc2014-ocw-android:

OpenConferenceWare Android
~~~~~~~~~~~~~~~~~~~~~~~~~~

Project: Universal Scheduling API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explanation:**

OpenConferenceWare consists of an Android app and a Ruby on Rails back-end Web
app, its purpose is to provide access to conference scheduling data to Android
devices.

The object of this project is to design a universal API for serving conference
scheduling data, then implement this API as a module for the most popular
conference website platform (drupal, django, etc, based on research), replacing
the current RoR back-end application. The current OCW android app would then be
modified to consume data from this API.

**Expected Results**

A well-documented API for conference schedule data, a reference implementation
as a CMS module, and a working android application that connects to the CMS
module and effectively displays the schedule data.

**Knowledge Prerequisite:**

General concepts of API design, Android development experience, and ability to
program in the language of the desired reference CMS (PHP, Python or Ruby).

**Mentor:** Ken (kennric)

----

.. _gsoc2014-centralized-osl-logging:

Centralized OSL Logging
~~~~~~~~~~~~~~~~~~~~~~~

Project: Implement Graylog2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explanation:**

Currently the OSL sends most of their logs to a centralized loghost, however we
don’t have the logs in a searchable format outside of using grep. In addition we
have a problem with keeping track of all of the root and cron email that gets
sent. Ideally we’d like to have it in a centralized searchable database using
something such as Graylog2, then we could tie in other information for
dashboards, monitoring and other various tasks.

**Expected Results**

An implementation of Graylog2 setup and configured to work in our environment.
Research possible ways of setting it up and decide on a sane implementation.
Design an architecture that fits our specific needs and requirements.
Integration of automated email updates from hosted services into the system and
create search ability.

**Knowledge Prerequisite:**

Understanding of system logging and root mail. Understanding of how the various
technologies used by Graylog2 and how they interconnect. Experience in APIs and
scripting.

**Mentor:** Justin (pwnguin)

----

.. _gsoc2014-other-projects:

Other OSL Projects
~~~~~~~~~~~~~~~~~~

These are projects we don't have specific project proposals for, but you are
free to take a look at and discuss with us any you might be interested in doing.

Ganeti Web Manager
^^^^^^^^^^^^^^^^^^

`Ganeti Web Manager`_ (GWM) is a Django based web application that allows
administrators and clients access to their `Ganeti virtualization clusters`_.
Through Ganeti Web Manager users can deploy and manage virtual servers. Ganeti
Web Manager is being built by the Open Source Lab to support Supercell, a
testing cloud for open source projects.

.. _Ganeti Web Manager: http://ganeti-webmgr.readthedocs.org/en/latest/
.. _Ganeti virtualization clusters: http://code.google.com/p/ganeti/

GWM is in the midst of a major redesign this year so we are opting to not use it
as a part of GSoC. We are still working on a basic design document which
describes what changes will happen. There may be opportunities to have a GSoC
project be a part of this major redesign process, we just haven't decided on how
that would work yet. Feel free to talk with us in #ganeti-webmgr on Freenode for
more information. We have already started researching possible ways of using
OpenStack Horizon as a dashboard via our `Ganeti Horizon`_ experiment project.

.. _Ganeti Horizon: https://github.com/osuosl/ganeti_horizon

*Stay tuned for more information.*

vagrant-ganeti
^^^^^^^^^^^^^^

`Vagrant Ganeti`_ is a Vagrant environment used by developers of Ganeti Web
Manager to have a local Ganeti environment for testing. It provides an
environment with up to three nodes with Ganeti deployed and ready to use. It
currently uses a `puppet module`_ that is very specific to this environment.

.. _Vagrant Ganeti: https://github.com/osuosl/vagrant-ganeti
.. _puppet module: https://github.com/osuosl/puppet-ganeti-tutorial

There are a number of issues with the current way its used that would be great
to fix eventually. Some are (but not limited to:

- Difficult to keep up to date with upstream releases
- Puppet Module is not production quality
- Defaults to building Ganeti from source (which is becoming a difficult problem
  with the haskell requirements)
- No Chef cookbook for optional use
- Reduce the amount of platforms supported and simplify it
- Support for other projects such as Synnefo, and other instance providers

*Please talk with Ramereth in #osuosl-gsoc on Freenode if you want to propose an
idea for this project.*

Ganeti Instance Image
^^^^^^^^^^^^^^^^^^^^^

`Ganeti Instance Image`_ is a guest OS definition for Ganeti that uses either
filesystem dumps or tar ball images to deploy instances. The goal of this OS
definition is to allow fast and flexible installation of instances without the
need for external tools such as debootstrap. It was originally based on
ganeti-instance-debootstrap.

.. _Ganeti Instance Image: https://code.osuosl.org/projects/ganeti-image

Much of what Ganeti Instance Image was set out to do has been replaced by
`snf-image`_. So at this point I would like to see only bug fixes or minor
feature additions to this project.

.. _snf-image: https://code.grnet.gr/projects/snf-image

*Please talk to Ramereth in #osuosl-gsoc on Freenode if you want to propose an
idea for this project.*

Protein Geometry Database (PGD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Protein Geometry Database`_ is a specialized search engine for protein
geometry.  It allows you to explore either protein conformation or protein
covalent geometry or the correlations between protein conformation and bond
angles and lengths. It is primarily a django project with a lot of javascript
logic built into it. This project is a joint venture between the OSUOSL and the
Oregon State University Biochemistry department on campus.

.. _Protein Geometry Database: https://code.osuosl.org/projects/pgd

This project is currently in maintenance mode however we would love to have a
full audit of the code or any other minor cleanup/modifications. We would love
to re-architect this project someday but it likely won't happen.

*Please talk to kennric in #osuosl-gsoc on Freenode if you want to propose an
idea for this project.*

----

Template
--------

::

    Primary Project Name
    ~~~~~~~~~~~~~~~~~~~~

    Project: GSoC Idea
    ^^^^^^^^^^^^^^^^^^

    **Brief Explanation:**

    **Expected Results**

    **Knowledge Prerequisite:**

    Mentor:
