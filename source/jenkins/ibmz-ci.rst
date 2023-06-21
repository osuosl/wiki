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

Creating a Jenkins Job with Docker on IBM-Z CI
----------------------------------------------

Go to the IBM-Z Jenkins dashboard at https://ibmz-ci.osuosl.org and follow the :ref:`jenkins_docker` documentation.
