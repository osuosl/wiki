The OSL Development Workflow
============================

The OSL builds websites for a variety of clients including the Oregon Virtual
School Districts, the Oregon Sea Grant Foundation, the OSU Biology department,
and Google. When the initial development is finished, the OSL will host and
maintain the websites. This document will guide developers through the steps of
creating a new website for a client. New developers are encouraged to read this
document to understand how the developer team works, and experienced developers
are encouraged to review this document to brush up their knowledge of parts of
the process they may not be intimately familiar with. This workflow description
will also be available to clients so they can understand how the OSL developer
team works.

.. toctree::
  :maxdepth: 1
  :glob:

  *

Tools The Team Uses
-------------------


At the OSL developers use a variety of open source tools. Developers are
expected to have at least passing familiarity with all of these tools. New
developers are encouraged to research any of these tools with which they are
unfamiliar.

Most OSL websites are written in Python using the Django web application
framework. Websites are deployed using Chef configuration management on CentOS
6.6. Most of our sites use the MySQL database, although some use Postgres.
Most OSL websites have a Docker development environment set up to make
development fast and easy. To learn how to use the Docker development
environment, please consult the project documentation.
The OSL uses ``git`` for version control and keeps projects on
GitHub_. The OSL uses the Github issue tracker.

.. _GitHub: https://github.com/osuosl
