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

Creating a Jenkins Job with Docker
----------------------------------

Go to the POWER CI Jenkins dashboard at https://powerci.osuosl.org and follow the :ref:`jenkins_docker` documentation.
