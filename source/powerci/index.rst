.. _powerci:

POWER CI
========

This documentation covers the infrastructure which powers https://powerci.osuosl.org/ and how to use it.

Overview
--------

The POWER CI cluster consists of the following components:

- Jenkins node

  - This node does not run any jobs locally, however it does connect to other worker nodes.
  - Its authentication uses Github OAuth
- Docker worker nodes

  - Two nodes run on POWER8 virtual machines
  - Two nodes run on POWER9 virtual machines

Table of Contents
-----------------

.. toctree::
  :maxdepth: 1
  :glob:

  *
