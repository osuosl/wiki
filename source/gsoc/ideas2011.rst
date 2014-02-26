Google Summer of Code 2011 Ideas
================================

.. note::

  This page is kept for historical purposes. Please check the latest year's
  ideas page for the most up to date information.

Welcome to the Oregon State University Open Source Lab Google Summer of Code
Ideas page.  

Ganeti Web Manager
------------------

`Ganeti Web Manager`_ is a Django based web application that allows
administrators and clients access to their `Ganeti virtualization clusters`_.
Through Ganeti Web Manager users can deploy and manage virtual servers.  Ganeti
Web Manager is being built by the Open Source Lab to support `Supercell`_, a
testing cloud for open source projects.

.. _Ganeti Web Manager: http://code.osuosl.org/projects/ganeti-webmgr
.. _Ganeti virtualization clusters: http://code.google.com/p/ganeti/
.. _Supercell: http://supercell.osuosl.org

Visit our irc channel #ganeti-webmgr on freenode for help getting started.

.. _source/soc/ideas2011#projects:

Projects
~~~~~~~~

- `REST API that other applications and scripts can use for automated
  deployments to a GWM enabled cluster`__.
- `LIBCloud driver for Ganeti Web Manager REST API`__.
- `Add Selenium tests to the test suite`__
- `Xen support`__
- `Realtime Metrics for virtual machines`__
- `Basic Puppet Integration - configuration management`__
- `Update the cache synchronizer to use twisted and support synchronization of
  all ganeti objects`__
- Add visualization of clusters, nodes, and or virtual machines.

.. __: http://code.osuosl.org/issues/3573
.. __: http://code.osuosl.org/issues/3579
.. __: http://code.osuosl.org/issues/2655
.. __: http://code.osuosl.org/issues/663
.. __: http://code.osuosl.org/issues/3615
.. __: http://code.osuosl.org/issues/3609
.. __: http://code.osuosl.org/issues/3831

.. _source/soc/ideas2011#django_object_permissions:

Django Object Permissions
-------------------------

Object permissions is an implementation of row level permissions.  It also
includes functionality for editing Groups.

Projects
~~~~~~~~

- Improving User Actions Related to group membership

  - `Create a custom widget for selecting users and groups`__
  - `Allowing bulk selection of users`__
  - `Allow bulk deleting users`__
- `Finish implementation of Related object queries`__:

  - Tickets are partially implemented with unittests.  Some queries did not work
    and need to be rewritten to generate proper SQL.
  - This project requires in depth knowledge of django QuerySets including Q
    clauses and F clauses.

.. __: http://code.osuosl.org/issues/339
.. __: http://code.osuosl.org/issues/2763
.. __: http://code.osuosl.org/issues/2763
.. __: http://code.osuosl.org/issues/2415

Django Object Log
-----------------

Object Log is a pluggable django app providing the ability to log user actions
on model instances.  It allows verbose messages defined by other apps.

Projects
~~~~~~~~
- Add the ability to store arbitrary data, and automatically cache data for log entries:

    - `Allow Log entries to store arbitrary data in addition to ForeignKeys to
      objects`__
    - `Allow LogActions (types) to register a cache processing function`__

.. __: http://code.osuosl.org/issues/3819
.. __: http://code.osuosl.org/issues/3825
