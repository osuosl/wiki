
.. _osl-development-process:

The OSL Development Workflow Guide
======

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
--------------------------------
A step by step guide to writing the project

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

The Development Process
-----------------------

- Pick an issue
- Write tests (with a sample Django test)
- Write the code
- Make a PR
- Merge it
- Close the issue

A Brief Introduction to Django
------------------------------
- Sample manage.py commands (runserver, collectstatic, migrate)
- How to write a very simple model
- How to write a very simple view

How to git out of a tight corner
--------------------------------
- Common git configuration tricks
- When and when not to force push
- How to rebase code
- How to cherry-pick
- How to reflog
- How to add remotes and set upstream branches
- 
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

.. toctree::
    :maxdepth: 1
    :glob:

    *
