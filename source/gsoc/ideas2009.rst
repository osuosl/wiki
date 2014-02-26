Google Summer of Code 2009 Ideas
================================

.. note::

  This page is kept for historical purposes. Please check the latest year's
  ideas page for the most up to date information.


Welcome to the Oregon State University Open Source Lab Google Summer of Code
Ideas page.  

One of the things we learned in the past three Summer of Code programs is that
the more time spent on collecting and refining the proposed project ideas, the
better the summer goes.  So with that in mind ... ta-dah!  A new SoC ideas page.

AndroidIRC(name?)
-----------------

AndroidIRC(name?) is a completely open source IRC client for Google's Android
mobile platform (http://code.google.com/android/).

Planned Features for AndroidIRC(name?)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Allow direct connection to any IRC server and provide all the functionality a
  client should have. (see RFC1459 -
  http://www.ietf.org/rfc/rfc1459.txt?number=1459).
- Multi-server and multi-channel support. 
- Develop a sane way of dealing with several servers and channels on very low
  amounts of screen real estate. 
- Follow all user interface guidelines and match usability/functionality
  standards of other included "IM" applications for the Android platform. 
- Develop an external, and optional, message-queuing service that works with our
  client. The idea is to devise a way to allow persistent connections to IRC
  channels so that users can idle, send, and receive messages via the mobile
  client but minimize the time that the network stack is active, thus saving
  battery life and network traffic. (This can be accomplished by writing our own
  "server", or leveraging already existing open source technology)
- Use encrypted connections/data whenever possible. 

Projects
~~~~~~~~

There are 3 logical divisions of labor for this project:

- IRC client communication backend: Handle connections and sending and receiving
  messages.
- GUI: Use the exposed backend functions to craft an aesthetically pleasing and
  easy to use interface.
- External message-queuing service: Write/implement a simple message-queuing
  server for our client, allowing us to "idle" and receive/send messages when
  the application is in the foreground or on a specific time interval without
  wasting battery life or network traffic. 

Pydra
-----

Pydra is an open source parallel and clustered computing solution written in
python using Twisted.Python and Django.  Pydra is a new project that is working
towards it's first public release.

`Read more about pydra <http://pydra-project.osuosl.org>`_

Project Ideas
~~~~~~~~~~~~~

Contribute to Pydra
^^^^^^^^^^^^^^^^^^^

There are a lot of features on the wishlist for pydra.  Pick and choose from
these ideas, or check out the `task tracker`_:

.. _task tracker: http://pydra-project.osuosl.org/report/2

- `Network Auto-Discovery`_
- `Map-Reduce support`_
- `Multi-Master`_ / `Multi-Main support`_
- `Function Wrapper (ie. function call from regular python app gets run on the
  cluster)`__

.. _Network Auto-Discovery: https://pydra-project.osuosl.org/ticket/8
.. _Map-Reduce support: https://pydra-project.osuosl.org/ticket/64
.. _Multi-Master: https://pydra-project.osuosl.org/ticket/67
.. _Multi-Main support: https://pydra-project.osuosl.org/ticket/68
.. __: https://pydra-project.osuosl.org/ticket/20

Write Applications Using Pydra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Develop an application that uses Pydra to reduce its run time.  Here are some
suggestions, feel free to come up with your own ideas.

- Web Crawler
- Document Indexer

Touchscreen 2.0
---------------

Touchscreen is software for running interactive slideshows/demos.  Touchscreen
allows standalone slideshows or interactive displays using controls such as a
touchscreen interface.  It is primarily used at the OSL on the large
flatscreen+touchscreen directly outside our server room.  It displays various
statistics and realtime data about the lab.

We are in the process of rewriting touchscreen to use Django, Jquery,
javascript, HTML, and CSS.

`Learn more about Touchscreen <http://trac.osuosl.org/touchscreen>`_

Project Ideas
~~~~~~~~~~~~~

Write a Screen Plugin(s)
^^^^^^^^^^^^^^^^^^^^^^^^

Write new plugin(s) that showcases things happening at the osl.  We'll supply
the data, you supply an exciting representation of it.  

Here are some screens we have already produced:

- `Plotting Locations of Our FTP Users on a World Map in Realtime`_
- `OSL Bandwidth Usage`_
- `FTP Bandwidth map`_
- `Campus Webcams`_

.. _Plotting Locations of Our FTP Users on a World Map in Realtime: https://trac.osuosl.org/touchscreen/ticket/19
.. _OSL Bandwidth Usage: https://trac.osuosl.org/touchscreen/ticket/16
.. _FTP Bandwidth map: https://trac.osuosl.org/touchscreen/ticket/20
.. _Campus Webcams: https://trac.osuosl.org/touchscreen/ticket/11

Suggestions for new screens:

- rewrite ftp user's map using google maps.

Work on Touchscreen Core
^^^^^^^^^^^^^^^^^^^^^^^^

Here are some suggestions of things to be worked on, or take a look at the `task
tracker`__ 

.. __: http://trac.osuosl.org/touchscreen/report/1

- `Screen control/configuration interface`__
- `Menuing configuration interface`__
- `Menu Generation`__
- `Convert Existing Screens into 2.0`__

.. __: https://trac.osuosl.org/touchscreen/ticket/15
.. __: https://trac.osuosl.org/touchscreen/ticket/12
.. __: https://trac.osuosl.org/touchscreen/ticket/13
.. __: https://trac.osuosl.org/touchscreen/query?milestone=screens+migrated&order=priority&col=id&col=summary&col=status&col=type&col=priority

Protein Geometry Database
-------------------------

The Protein Geometry Database is a tool for searching and correlating geometric
structures within proteins.  It is used to derive empirical information about
protein geometry which will produce improved modeling techniques.  Highly
detailed protein models will ultimately result in knowledge of how diseases
function, and what drugs will inhibit them.  The software is being developed by
the OSL for the Oregon State University Department of Biochemistry & Biophysics

PGD is in an early beta state.  We have a usable version there are many features
planned for 1.0 that have not been implemented yet

Check out the `demo <http://dev.osuosl.org/pgd/>`_

Project Ideas
~~~~~~~~~~~~~
Here are some example tasks to choose from, or take a look at the `Task
Tracker`__ and suggest your own idea.

.. __: https://xray.science.oregonstate.edu/trac/pgd/report/2

- `Add JMol applet for easy structure viewing`__
- `Add additional fields to splicer import tool`__

.. __: https://xray.science.oregonstate.edu/trac/pgd/ticket/70
.. __: https://xray.science.oregonstate.edu/trac/pgd/query?status=accepted&status=assigned&status=new&status=reopened&description=~import&component=splicer&order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone

Unify
-----

Unify is a unifed package building system using gentoo ebuilds as the "build
scripts". Its primary purpose is to create proper binary packages for deb, rpm,
and Solaris package types. The basics of the application was created last year
in the previous SoC. Check out the project `here`_.

.. _here: http://trac.osuosl.org/trac/unify

Project Ideas
~~~~~~~~~~~~~

Package Dependency
^^^^^^^^^^^^^^^^^^

Currently Unify has no concept of package build dependencies. Each package
format has their own naming scheme for package dependencies. Gentoo also has no
concept of sub-packages like most binary packages have (i.e. -devel, -libs,
etc). The logic and concept for this needs to be created and implemented.

Solaris Support
^^^^^^^^^^^^^^^

The original goal for the project was creating a sane system for building
solaris packages using gentoo ebuilds. Implementing support for at least Solaris
9 and 10 would be great. It would require knowledge of Solaris and its packaging
sytem (which is mostly closed sourced). It also has no real package manager, so
that would need to be accounted for possibly.

VirtAdmin
----------

`VirtAdmin`_ is a project at the OSL to create a web interface for managing
virtual infrastructure. The goals are to simplify management and eventually to
be able to give projects limited access to virtualized infrastructure we host
for them (for example allowing them to get on the console or reboot a virtual
machine).

.. _VirtAdmin: http://trac.osuosl.org/virtadmin

Project Ideas
~~~~~~~~~~~~~

Here are a few of the ideas we have for the project:

- Console access from the web interface
- Monitoring/Graphing
- Storage Management
- Design and Integrate an extensible plugin system
- Provisioning of virtual machines from the web interface

BeaverSource
------------

Beaversource (http://beaversource.oregonstate.edu) is a collaborative effort
among many different departments on campus to create a code community for open
source development at OSU. It attempts to provide a constructive and positive
environment for FOSS software developers on campus. 

Project Ideas
~~~~~~~~~~~~~

- Expand the BeaverSource framework to be useful for other schools that want to
  set up their own OSS-based curriculum around a education based hosting
  framework.

OSWALD
------

OSWALD (http://beaversource.oregonstate.edu/projects/cspfl) is a
student-developed Ultra-mobile PC, made for undergraduate students to explore CS
concepts hands-on. To do this, the OSWALD is powerful, flexible, and
incorporating some of the latest technology available, while keeping the cost to
a minimum.

Project Ideas
~~~~~~~~~~~~~
- Port android to the OSWALD device to open up more opportunities for teaching
  and projects with the device (especially in the mobile area).

Trust the Vote - Open Source Digital Voting
-------------------------------------------

The `Open Source Digital Voting (OSDV) Foundation`_ serves as a supporting
organization for a collection of open source digital voting technology projects.
The purpose of the Foundation is to provide support and protection for the
development of the specifications, draft standards, and reference
implementations of high assurance, high veracity digital voting technology

.. _Open Source Digital Voting (OSDV) Foundation: http://osdv.org

We propose that one or more Google Summer of Code students work with OSL staff
on the design and development of a demonstration digital voting service that
uses high assurance voting system "reference implementations" which meet the
draft standard guidelines, specifications, and potential assessment standards.

Project Ideas
~~~~~~~~~~~~~

Please note that some of these ideas may be too large or too small for a Summer
of Code project.  Please keep that in mind while formulating your proposal.

Building a reduced kernel platform for high-integrity embedded applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Goal: create a substantially minimized Linux distro and build process for simple
embedded applications.  This distro will be the basis for voting systems
designed by OSDV.  The reasoning for a reduced distro is to reduce the amount of
source code in the distro.  Both the build system and all source code must be
certified by an independent test lab prior to use in U.S. elections.  Less
source code simplifies and speeds up the certification process.

- Start with a bare Linux kernel add only the features required for a working
  kernel that can support a simple embedded application that does no networking,
  no IPC, requires only the basic sequential file system, and uses the most
  generic devices and drivers for keyboard, video, and one form of removable
  media for both reading and writing.
- kernel must include hardened kernel patches
- Create a LiveCD image that runs a hello-world++ program on reduced kernel,
  doing some reading from a removable medium, and some appending to a removable
  medium.
- Build Process for the LiveCD must be automated.

Build a Minimal Distribution of Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Goal: Build a distribution of Python that has the minimal set of functionality
needed for voting systems.

- Determine what is the minimum set of Linux packages that is needed to support
  a python application execution environment. By itself this would be a big
  achievement. Some technical support from python.org folks maybe available.
- Experiment with changes to the standard python distribution to reduce it in
  order to eliminate some package dependencies. Using Ka Ping Yee's definition
  of a thin python subset ("pthin" see www.pvote.org), modify the python
  interpreter to implement only pthin rather than the full python.
- Using Yee's pvote sample application in pthin as a guide, determine what parts
  of the python runtime can be exised as unneeded for pthin applications.
  Eliminate these from the python build, and determine whether more package
  dependencies have been eliminated.
- Demonstrate pvote running on your reduced distribution.
- Assess the difficulty of the task of developing custom-build software that
  automates the modification of the standard python distribution.

Highly auditable ballot tabulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Goal: create a first version of the BCCS component that creates the final
election results by totaling up partial election results.

Background:

- Election Markup Language (EML) includes schema for both a ballot format
  (sequence of contests, candidates in each contest, etc.) and tallies in a
  format (for each item in the format, a number of votes cast for that item).
- A highly auditable program is one that is relatively easy for independent
  readers to audit (read, understand, develop test plans) due in part to the
  care with which the program is written, in part to low inherent complexity,
  and in part by using a high-level language that was designed for readability
  and comprehensibility.

In such a language (python preferred), develop a program to meet these
functional requirements:

- Consume an input schema in EML that defines a ballot format
- Choose a subset of EML's ballot definition schema if needed to reduce the
  scope of the programming task
- Consume an input dataset of multiple EML tally datasets in the input schema
- Create an output dataset in EML's schema for ballots tallies, recording the
  total number of votes for each contest/candidate or measure /choice.
- In computing the ballot totals, use a vote-for-at-most-one voting model, and
  detect (and not count) overvotes
- Create an output dataset in ad hoc format that records numbers of undervotes
  and overvotes for each contest.

Auditable high-integrity transaction-secure Web browser appliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Goal: The end result is a LiveCD image that boots a system that runs exactly one
program, which is a customized Web browser in which security configurations
(including certificates) are unchangable. Some assitance from mozilla,org folks
may be available.

- As a starting point, use a standard Linux distro, and the XULrunner toolkit
  for building embedded browsing into other applications.
- The application to be embedded in is simply part of the Linux system
  initialization software.
- Along the way from this starting point, you will excise the parts of XUL
  runner that are not needed in order to support simple forms-based Web
  applications, e.g., no active content. (A specific example Web application
  will be provided.)
- Time permitting, determine what packages of the Linux distro can be eliminated
  because the browser does not depend on them.

Background: The eventual objective is to create a browser appliance that is more
auditable than the standard alternative (full browser distro running on full OS
distro) by virtue of lower size and complexity. Auditability, in turn, is
central to developing assurance of the embedded security properties of the
browser appliance.

Basic ballot marking extension of pvote
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Goal: enhance pvote (a balloting software package, see pvote.org) to print a
paper artifact that resembles an official ballot

- Record each pvote-captured ballot as an e-ballot in EML, for a specific ballot
  definition (to be supplied)
- Using pre-created paper ballot format (which will be supplied) to create a
  paper ballot image corresponding to the e-ballot
- Print the ballot image
- Create a liveCD image for testing of this electronic ballot marking software,
  including the audio ballot function

High-fidelity electronic ballot marking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Goal: create ballot marking software with a presentation layer that closely
mimics the presentation of a paper ballot

Electronic ballot marking devices present an unusual challenge in high-assurance
system development and user interface design: an EBM system must present ballot
information a choice that are exactly the same as that presented by a paper
ballot; and ensure that users have the same progress tracking information as
offered in a paper ballot; and select the proper ballot that captures the user's
choices, with a minimum of software complexity and a maximum of software
auditability. Using as an example a real election paper ballot, and building on
previous work in pre-rendered user interfaces, implement a visual navigation
scheme that shows the whole ballot, selection and zooming to particular
contests, selection and marking of each contest, progress tracking showing
completed sections of the ballot, and selection of a pre-rendered ballot image
to be printed. Demonstrate strong software separation between UI functions,
ballot-data storage functions, and ballot image prep and printing functions.

Optical scan/tally device presentation layer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Background: Ballot browser is an existing open source software package that
consumes a set of ballot image files, performing image processing to extract
marks representing votes, and to record ballot, vote, and tally information in a
local database.

Goal: augment Ballot Browser with functions for creating pre-defined reports,
and for simple user-user-driven ad hoc queries.

- Using standard Linux and Python distros, build an embedded system for running
  Ballot Browser on a fixed set of ballots (to be provided), and package as a
  liveCD image.
- Create additional software, and associated UI, for the creation of pre-defined
  reports derived from the database after the ballot scanning is complete
- Create additional software, and associated UI, some simple ad hoc queries
  against the database
- Package extended system as a liveCD image

Voter Registration System and Election Management System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OSDV is building an open source Voter Registration System and Election
Management System, using ruby/rails. Contributions range from joining the
ongoing implementation team for voter registration, to finishing the design and
starting the development for election management. An extensive set of functional
requirements is available at
http://www.sos.ca.gov/elections/bidders_library/final-rfp-changes-accepted/add8-section-VI-2008-changes-accepted.pdf
pages 12 to 95.

OpenOffice.org
--------------

Project Ideas
~~~~~~~~~~~~~

Migrate Extensions site to Drupal 6 modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OSL hosts Openoffice.org's `Extensions website`_ which is powered by Drupal
5.  Unfortunately most of the modifications that were made to the site were done
directly to the core Drupal code which makes upgrading it nearly impossible.
This project would entail going through the existing code base, proposing a plan
for how it could be implemented as one or more modules in Drupal 6, writing the
modules, and finally testing the modules. We're currently working on a
detailed list of changes that were made which should be posted soon. 

.. _Extensions website: http://extensions.services.openoffice.org/
