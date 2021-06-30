.. _ibmzci:

IBM-Z CI
========

This documentation covers the infrastructure which powers https://ibmz-ci.osuosl.org/ and how to use it.

Overview
--------

The IBM-Z CI cluster consists of the following components:

- Jenkins node

  - This node does not run any jobs locally, however it does connect to other worker nodes.
  - Its authentication uses Github OAuth
- Docker worker nodes

  - Two nodes run on s390x virtual machines hosted at `Marist College`_

.. _Marist College: http://www.marist.edu/

Table of Contents
-----------------

.. toctree::
  :maxdepth: 1
  :glob:

  *
