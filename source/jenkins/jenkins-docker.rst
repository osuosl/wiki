.. _jenkins_docker:

Create Jenkins Jobs using Docker
================================

This document describes how to create a Jenkins job which deploys as a Docker container on our infrastructure.

Overview
--------

The `Docker Custom Build Environment`_ plugin has been installed to allow the ability to run jobs inside of containers.
When a job is executed, the Jenkins primary node connects to one of the worker nodes, deploys a container on the node,
and reports the information back.

.. _Docker Custom Build Environment: https://plugins.jenkins.io/docker-custom-build-environment

OSL Pre-Built Images
--------------------

We currently maintain a list of container images to help with usage on the cluster. Here is the current
list of images we support:

- `osuosl/centos-ppc64le`_
- `osuosl/debian-ppc64le`_
- `osuosl/fedora-ppc64le`_
- `osuosl/ubuntu-ppc64le`_

These images are tested and verified to work on our infrastructure. Although you are not required to use these images
and, many projects use images from other sources without any problem. 

If you have any issues with our images or want to add support for something, please visit https://github.com/osuosl/osl-dockerfiles.

.. _osuosl/centos-ppc64le: https://hub.docker.com/r/osuosl/centos-ppc64le
.. _osuosl/debian-ppc64le: https://hub.docker.com/r/osuosl/debian-ppc64le
.. _osuosl/fedora-ppc64le: https://hub.docker.com/r/osuosl/fedora-ppc64le
.. _osuosl/ubuntu-ppc64le: https://hub.docker.com/r/osuosl/ubuntu-ppc64le

Notes on Using Your Own Containers
----------------------------------

The Docker Custom Build Environment plugin allows users to build and run any container they would like, however there
are some restrictions that need to be made before using it. The plugin requires the user running the build commands to
be the same as the jenkins secondary agent user. This means if you need to run root level commands inside of your
container, you need to do the following:

#. Ensure you create a user with the same UID/GID as our secondary agent, which is currently ``10000``.
#. Ensure sudo is installed on the container and the user is allowed to run sudo commands.

Creating a Basic Item
---------------------

This example shows how to create a simple Freestyle project. Other project types follow a similar basic layout, so this
example can be adapted to any other project type.

1. Create a New Freestyle Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Log in at the Jenkins dashboard (https://powerci.osuosl.org or https://ibmz-ci.osuosl.org) with your GitHub account.
Click on the "New Item" option on the left menu as in the image below. Then, enter your item's name and select
"Freestyle project" under the textbox.

.. image:: /_static/images/powerci-new-item.png


2. Build Inside a Docker Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next select the ``Build inside a Docker container`` under the ``Build Environment`` section for the job. You have two
options to select:

Pull a Docker image from a repository:

.. image:: /_static/images/powerci-build-repo.png

Or build from a Dockerfile:

.. image:: /_static/images/powerci-build-dockerfile.png


3. Set Any Advanced Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default settings should work in general, but to set advanced options, click the "Advanced..." button below the
"Docker image to use" section:

.. image:: /_static/images/powerci-build-advanced-settings.png

Available advanced options include:

- Private Docker registries
- Volumes
- Running in privileged mode
- Setting memory limit / CPU shares

.. image:: /_static/images/powerci-build-advanced.png

Use any of these options at your own risk.

4. Add a Build Step
^^^^^^^^^^^^^^^^^^^

Next, add a build step. You can choose any that work in the container but for this example we're just doing a simple
shell.

.. image:: /_static/images/powerci-docker-execute-shell.png

If all goes well, you should be able run the build and have it succeed!

GitHub Pull Request Integration
-------------------------------

Follow this example to create a Jenkins pipeline that will automatically build when a pull request is updated on
GitHub. This example uses the `GitHub Branch Source plugin`_.

Before starting, add a Jenkinsfile to your repository. This file is used for configuring the pipeline, including build
steps and agents. A simple starting example and documentation are available here:
https://www.jenkins.io/doc/book/pipeline/jenkinsfile/.

Here's a simple example of a declarative Jenkinsfile:

.. code-block::

   pipeline {
       agent {
           docker { image 'osuosl/centos-ppc64le' }
       }
       stages {
           stage('Build') {
               steps {
                   echo 'Building....'
                   sh 'gcc hello.c -o hello --std=gnu99'
               }
           }
           stage('Test') {
               steps {
                   echo 'Testing....'
                   sh './hello'
               }
           }
       }
   }

.. _GitHub Branch Source Plugin: https://plugins.jenkins.io/github-branch-source/

1. Add GitHub Credentials in Jenkins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Log in to the appropriate dashboard at https://powerci.osuosl.org or https://ibmz-ci.osuosl.org.
#. Click the Credentials tab in the left menu and then the System tab under the Credentials tab.
#. Click the "Global credentials (unrestricted)" domain in the table.

   .. image:: /_static/images/ghbsp-credentials1.png

#. Click Add Credentials in the left menu.
#. In the Kind dropdown, select "Username with password". Leave Scope as "Global".
#. In the Username field, enter your GitHub username (your account used to access the repository).
#. In the Password field, enter a GitHub Personal Access Token for your account. (See the `upstream documentation`__ to
   learn how to generate a Personal Access Token.)
#. Click "OK" to save the new credentials.

   .. image:: /_static/images/ghbsp-credentials2.png

.. __ : https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

2. Add a Webhook in the Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the Settings tab of your repository, click the Webhooks tab and click "Add a new webhook".

#. For the payload url, enter https://powerci-jenkins.osuosl.org/github-webhook/ or
   https://ibmz-ci.osuosl.org/github-webhook/. For content type, select "application/x-www-form-urlencoded".

   .. image:: /_static/images/ghbsp-webhooks1.png

#. Pick the events you'd like to trigger builds on. For a pull request trigger, the "Just the ``push`` event" option
   should be enough, but for the build details to be linked on the GitHub PR page and depending on Jenkins
   configuration, you may need to add the ``pull request`` event as well under "Let me select individual events".

   .. image:: /_static/images/ghbsp-webhooks2.png

   .. image:: /_static/images/ghbsp-webhooks3.png

#. Make sure the "Active" box is checked, then click "Add webhook" to save the new webhook.

The `upstream documentation`__ has more information about GitHub webhooks.

.. tip::

   If your payload url is correct, there should be a green checkmark next to your new webhook on the webhook dashboard
   page at https://github.com/your-user-or-org/your-repo/settings/hooks. You can also check that payloads are being
   sent and received by clicking "Edit" and selecting the "Recent Deliveries" tab. If these are correct and the build
   still doesn't trigger properly, the issue is probably on Jenkins' side.

__ : https://docs.github.com/en/webhooks-and-events/webhooks

3. Create a New Multibranch Pipeline Item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Return to the Jenkins Dashboard and click "New Item" in the left menu.
#. Name the item and select "Multibranch Pipeline", then click "OK".
#. Under Branch Sources, click "Add source" and select "GitHub". Under Credentials, select the
   ``<your-GH-username>/******`` credential from the dropdown. Enter the HTTPS URL for your repository in the
   Repository HTTPS URL field. (Click the "Validate" button to check that Jenkins is able to access the repository.)
   You can also pick specific behaviors to determine when builds will happen and on which branches/PRs.

   .. note::

       For a single build to trigger after one push to a PR, we suggest using these two options:

       - Discover branches: Exclude branches that are also filed as PRs
       - Discover pull requests from origin: The current pull request revision

       You will need to set the webhook to include both the ``push`` event and the ``pull request`` event.

#. Under Build Configuration, select "by Jenkinsfile" and a Script Path of "Jenkinsfile".
#. Add an agent under the Docker Label field; you can find a list of available labels by going back to the Dashboard
   and clicking the Labels Dashboard tab (or go to ``https://<dashboard>.osuosl.org/labelsdashboard/``). The list is
   under the "Nodes" header. If the Docker Label field is left blank, it will inherit a default agent.
#. Your configuration might now look something like the image below. Click "Save" at the bottom to save your changes.

.. image:: /_static/images/ghbsp-config1.png

Now return to your repository and try pushing a change to a pull request. It may take a few moments for the trigger to
be processed; when the build starts, you should see a box with a yellow circle at the bottom of the PR that displays
the status of the build.

.. note::

    We used to use the `GitHub Pull Request Builder (ghprb)`_ plugin to integrate Jenkins builds with GitHub pull
    requests, but it is now deprecated. You can still use `this tutorial`_ to learn more about this plugin.

.. _GitHub Pull Request Builder (ghprb): https://plugins.jenkins.io/ghprb
.. _this tutorial: https://devopscube.com/jenkins-build-trigger-github-pull-request
