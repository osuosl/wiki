Google Summer of Code 2012 Ideas
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

Projects
~~~~~~~~

- `Realtime Metrics for virtual machines`__
- `Basic Puppet Integration - configuration management`__
- `Implement Node Groups`__
- `Bulk Operations`__
- `Add visualization of clusters, nodes, and or virtual machines`__

.. __: http://code.osuosl.org/issues/3615
.. __: http://code.osuosl.org/issues/3609
.. __: http://code.osuosl.org/issues/6795
.. __: http://code.osuosl.org/issues/2745
.. __: http://code.osuosl.org/issues/9537

.. _source/soc/ideas2012#ganeti_instance_image:

Ganeti Instance Image
---------------------

`Ganeti Instance Image`__ is a guest OS definition for Ganeti that uses either
filesystem dumps or tar ball images to deploy instances. The goal of this OS
definition is to allow fast and flexible installation of instances without the
need for external tools such as debootstrap. It was originally based on
ganeti-instance-debootstrap.

.. __: https://code.osuosl.org/projects/ganeti-image

Projects
~~~~~~~~

- Complete `version 0.6 release`__ tasks
- `Add support for OS Parameters`__
- `FreeBSD OS support`__
- `Add support for AMI images`__
- `Add support for OpenStack Images`__

.. __: http://code.osuosl.org/projects/ganeti-image/versions/339
.. __: http://code.osuosl.org/issues/9549
.. __: http://code.osuosl.org/issues/225
.. __: http://code.osuosl.org/issues/9555
.. __: http///code.osuosl.org/issues/9561

OSL Systems
-----------

OSL Systems are projects assist in the hosting infrastructure of the OSL.

Projects
~~~~~~~~

- `check_hwraid LSI/MegaRAID/HP RAID Nagios Plugin`__
- `Infrastructure-wide IPMI Management Console`__
- `Create & Implement status.osuosl.org`__

.. __: http://code.osuosl.org/issues/8715
.. __: http://code.osuosl.org/issues/9543
.. __: http://code.osuosl.org/issues/6765
