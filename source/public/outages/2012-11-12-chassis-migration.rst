
.. _source/public/outages/2012-11-12-chassis-migration#2012-11-12_-_osl_core_networking_chassis_migration:

2012-11-12 - OSL Core Networking Chassis Migration
==================================================

.. _source/public/outages/2012-11-12-chassis-migration#summary:

Summary
-------

We are needing to migrating the core components of our current 6509 chassis into a newer chassis. This involves configuring the new router alongside the current router and migrate the line cards and ports one by one. To minimize the outage impact, we have chosen to only do one line card per evening and the outage will only be per server and should only last under a minute.

This page is to document what servers and projects will be impacted each night. Each outage is scheduled to happen at the time specified in the tables below.

.. _source/public/outages/2012-11-12-chassis-migration#schedule:

Schedule
--------

:doc:`url>https://docs.google.com/spreadsheet/pub`

.. _source/public/outages/2012-11-12-chassis-migration#special_notes:

Special Notes
-------------

Some hosts are a part of a cluster so we'll document those notes here:

  * All the private switches are used with the out-of-band and backend OSL network so any hosts in those racks will lose that connectivity.
  * gdev* hosts are for the ganeti-dev cluster
  * g1-g5 is the production ganeti cluster
  * orford/noot are the OSL ldap hosts
  * powerdev* hosts are the POWER7 machines
  * Some of these hosts are incorrectly labeled so I may have missed a few.

If you would like to see which rack your server is in with regard to the private backend switch outages, check out the following links:

  * :doc:`Row 1 <https///docs.google.com/spreadsheet/pub?key=0aqvvptulluaddeluzu43mjhjsw1fq0l1ddrkv3iyvgc&single=true&gid=1&output=html>`
  * :doc:`Row 2 <https///docs.google.com/spreadsheet/pub?key=0aqvvptulluaddeluzu43mjhjsw1fq0l1ddrkv3iyvgc&single=true&gid=3&output=html>`