.. _ibmzci_docker:

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

- `osuosl/debian-s390x`_
- `osuosl/fedora-s390x`_
- `osuosl/ubuntu-s390x`_

These images are tested and verified to work on our infrastructure. If you have any issues or want to add support for
something, please visit https://github.com/osuosl/osl-dockerfiles.

.. _osuosl/debian-s390x: https://hub.docker.com/r/osuosl/debian-s390x
.. _osuosl/fedora-s390x: https://hub.docker.com/r/osuosl/fedora-s390x
.. _osuosl/ubuntu-s390x: https://hub.docker.com/r/osuosl/ubuntu-s390x

Notes on using your own containers
----------------------------------

The Docker Custom Build Environment plugin allows users to build and run any container they would like, however there
are some restrictions that need to be made before using it. The plugin requires the user running the build commands to
be the same as the Jenkins worker agent user. This means if you need to run root level commands inside of your
container, you need to do the following:

1. Ensure you create a user with the same UID/GID as our slave agent which is currently ``10000``
2. Ensure sudo is installed on the container and the user is allowed to run sudo commands

1. Create new Freestyle project
-------------------------------

First step is to create a new freestyle project. After you logged in at https://ibmz-ci.osuosl.org with you GitHub
account, click on the "New Item" option on the left menu as in the image below. Then, enter your item's name and select
"Freestyle project" under the textbox.

.. image:: /_static/images/powerci-new-item.png


2. Build inside a Docker container
----------------------------------

Next select the ``Build inside a Docker container`` under the ``Build Environment`` section for the job. You have two
options to select:

Pull a Docker image from a repository:

.. image:: /_static/images/powerci-build-inside-docker.png

Or build from a Dockerfile:

.. image:: /_static/images/powerci-build-dockerfile.png


3. Set any advanced options
---------------------------

To show advanced config options, click on the "Advanced..." button below the "Docker image to use" as in the image
below:

.. image:: /_static/images/powerci-advance-docker-settings.png

A lot more advanced config options will show up:

.. image:: /_static/images/powerci-build-advanced.png

In general, the default settings should work, however there are a few advanced options you can use. You can set things
such as:

- Private docker registries
- Volumes
- Running in privileged mode
- Setting memory limit / CPU shares

Use any of these options at your own risk.

4. Add build step
-----------------

Next, add a build step. You can choose any that work in the container but for this example we're just doing a simple
shell.

.. image:: /_static/images/powerci-docker-execute-shell.png

If all goes well, you should be able run the build and have it succeed!

GitHub Pull Request Integration
-------------------------------

We use **GitHub Pull Request Builder (ghprb)** (repo_, wiki_) to integrate Jenkins build with GitHub Pull Request.  You
can check out their detailed official documentation and from many other available guides elsewhere such as `this one`_.
We think the availability of such documentation for this plugin is good enough that we don't need to replicate more of
them here.

.. _repo: https://github.com/jenkinsci/ghprb-plugin
.. _wiki: https://plugins.jenkins.io/ghprb
.. _this one: https://devopscube.com/jenkins-build-trigger-github-pull-request
