.. _creating-instances:

Creating Instances on OpenStack
===============================

This is a walkthrough for people using our clusters for virtual machines.

Entering Your User Account
--------------------------

We will create a project and user for you. The project will have a quota for resources, image and flavor settings, and
security settings. You will be sent a temporary password; log in to the appropriate OpenStack dashboard and change your
password as soon as possible.

Our OpenStack dashboards can be accessed at the following locations:

* x86: https://openstack.osuosl.org
* POWER: https://openpower-openstack.osuosl.org
* AARCH64: https://arm-openstack.osuosl.org

Launching a New Instance
------------------------

Log in to your account and enter Compute > Instances through the left menu. Hit the "Launch Instance" button.

.. image:: /_static/images/openstack-instance0.png

This popup allows you to configure the instance. Enter a name for your VM ("my-instance" in the example below), then
click "Next" to proceed to the "Source" tab.

.. image:: /_static/images/openstack-instance1.png

Selecting an Image
------------------

Ensure "Image" is selected in the "Select Boot Source" dropdown and "Create New Volume" is set to "No". Choose an image
for your instance from the list by clicking the corresponding up arrow "↑" button. The "Allocated" section indicates
your chosen image.

.. image:: /_static/images/openstack-instance1-source2.png

Click "Next" to proceed to the "Flavor" tab.

Selecting a Flavor
------------------

Choose a flavor that corresponds with the amount of CPU, RAM and disk you want to deploy your instance with. Clicking
the arrow ">" icon next to a flavor shows a preview of what your quota usage would be if you chose that flavor for the
instance. Click "Next" to proceed to the "Networks" tab.

.. image:: /_static/images/openstack-instance1-flavor.png

.. _flavor-storage-types:

Local storage and Ceph flavors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each flavor puts the instance's disk either on our Ceph storage or on fast local
NVMe storage on the compute node. These flavors use local storage:

* x86: flavors with ``local`` in the name, such as ``m2.local.8c8m100d``
* POWER: every POWER10 flavor, and the POWER9 ``p9.nvme`` flavors
* AARCH64: none yet

A few projects have flavors of their own that don't follow these names. If yours
does, ask us which kind it is.

The two trade off differently. Ceph keeps three copies of every disk across many
servers, so we can move your instance between compute nodes, usually without
downtime. Local storage gives much faster disk I/O, but the disk lives on a
single compute node, so maintenance on that node usually means some downtime for
your instance.

.. warning::

   Don't resize an instance between a local storage flavor and a Ceph flavor.
   OpenStack doesn't copy the disk, so the instance boots with a fresh disk
   built from its image. Email support@osuosl.org and we'll move it for you
   instead.

Resizing between flavors of the same kind works as usual. To check which kind
your instance uses, look at the Flavor column on the dashboard's Instances page,
or run this with the OpenStack command-line client::

  openstack server show <NAME> -c flavor

Instances that boot from a volume aren't affected, since their disk is a
separate volume that stays with the instance whatever flavor it uses.

If a resize has already left your instance with a fresh disk, don't confirm the
resize, and don't delete or rebuild the instance. Email support@osuosl.org right
away: we can often still recover the old disk, especially before the resize is
confirmed.

Selecting a Network
-------------------

We have multiple public networks that your instance can be deployed on; typically, the one with the highest-numbered
suffix will have the most openings for new instances. Choose a network and click "Next" to proceed to the "Security
Groups" section.

.. image:: /_static/images/openstack-instance1-networks.png

Selecting Security Groups
-------------------------

Security groups can be thought of as groupings of firewall rules; clicking the arrow ">" icon next to a security group
shows more information about each group. Generally, the default security group should be all you need, but you can
stack other security groups on as needed.

.. important:: The default security group allows no traffic in. If you want to access your instance from the outside,
               you will need to add rules to allow traffic.

.. image:: /_static/images/openstack-instance1-security-groups.png

Selected security groups are indicated under the "Allocated" section; click the down arrow "↓" button next to a group to
remove it from your selection.

After selecting the group(s) for your instance, click "Next" to proceed to the "Key Pair" tab.

Selecting Key Pairs
-------------------

The next screen allows you to add SSH public keys to the instance. OpenStack will add them to the instance at launch
using `cloud-init`_.

.. _cloud-init: https://docs.cloud-init.io/en/latest/

.. image:: /_static/images/openstack-instance2.png

If you've already added keys to OpenStack, they will be displayed in the "Available" section. You can also use "Import
Key Pair" to upload or paste a public key of your choice, or use "Create Key Pair" to generate new keys.

Launching the Instance
----------------------

Once you are happy with your chosen settings, click the blue "Launch Instance" button to create the instance. You can
monitor the status of the new instance and find its IP address in the Compute > Instances tab.

.. image:: /_static/images/openstack-instance0.png

Advanced Usage
--------------

Advanced users can add custom YAML data through the "Customization" tab. This configuration is used by cloud-init. For
more information on this, check out the `cloud-init documentation`_. Make sure to add ``#cloud-init`` at the top of the
section.

.. _cloud-init documentation: https://docs.cloud-init.io/en/latest/reference/examples.html

.. image:: /_static/images/openstack-instance4.png
