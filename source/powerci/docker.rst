.. _powerci_docker::

Create Jenkins jobs using Docker
================================

This document describes how you create a Jenkins job which deploys as a docker container on our infrastructure. We'll
describe how you do this using a freestyle project, however it can be adapted to any other job types.

Overview
--------

The `Docker Custom Build Environment`_ plugin has been installed to allow the ability to run jobs inside of containers.
When a job is executed, the Jenkins master node connects to one of the worker nodes, deploys a container on the node
and reports the information back.

.. _Docker Custom Build Environment: https://plugins.jenkins.io/docker-custom-build-environment

OSL Pre-built images
--------------------

We are currently maintaining a list of container images to help assist with usage on the cluster. Here is the current
list of images we support:

- `osuosl/centos-ppc64le`_
- `osuosl/debian-ppc64le`_
- `osuosl/fedora-ppc64le`_
- `osuosl/ubuntu-ppc64le`_

These images are tested and verified to work on our infrastructure. If you have any issues or want to add support for
something, please visit https://github.com/osuosl/osl-dockerfiles.

.. _osuosl/centos-ppc64le: https://hub.docker.com/r/osuosl/centos-ppc64le
.. _osuosl/debian-ppc64le: https://hub.docker.com/r/osuosl/debian-ppc64le
.. _osuosl/fedora-ppc64le: https://hub.docker.com/r/osuosl/fedora-ppc64le
.. _osuosl/ubuntu-ppc64le: https://hub.docker.com/r/osuosl/ubuntu-ppc64le

Notes on using your own containers
----------------------------------

The Docker Custom Build Environment plugin allows users to build and run any container they would like, however there
are some restrictions that need to be made before using it. The plugin requires the user running the build commands to
be the same as the jenkins slave agent user. This means if you need to run root level commands inside of your
container, you need to do the following:

1. Ensure you create a user with the same UID/GID as our slave agent which is currently ``10000``
2. Ensure sudo is installed on the container and the user is allowed to run sudo commands

1. Create new Freestyle project
-------------------------------

First step is to create a new freestyle project.

2. Set label to restrict where the job runs
-------------------------------------------

.. image:: /_static/images/powerci-restrict-label.png

Please select either ``power8`` or ``power9`` to restrict where the job is run. The labels will deploy the container on
either a VM running on a POWER8 or a POWER9 based managed. Please **do not** directly select one of the nodes that you
might see drop down. We may take nodes offline or change the names.

3. Build inside a Docker container
----------------------------------

Next select the ``Build inside a Docker container`` under the ``Build Environment`` section for the job. You have two
options to select:

.. image:: /_static/images/powerci-build-inside-docker.png

Pull a Docker image from a repository.

.. image:: /_static/images/powerci-build-dockerfile.png

Build from a Dockerfile.

4. Set any advanced options
---------------------------

.. image:: /_static/images/powerci-build-advanced.png

In general, the default settings should work, however there are a few advanced options you can use. You can set things
such as:

- Private docker registries
- Volumes
- Running in privileged mode
- Setting memory limit / CPU shares

Use any of these options at your own risk.

5. Add build step
-----------------

Next, add a build step. You can choose any that work in the container but for this example we're just doing a simple
shell.

.. image:: /_static/images/powerci-docker-execute-shell.png

If all goes well, you should be able run the build and have it succeed!
