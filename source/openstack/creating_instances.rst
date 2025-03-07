.. _creating-instances:

Creating Instances on OpenStack
===============================

This is a walk through for people using our clusters for virtual machines.

Groups and Users
----------------

You need to first have a group which your user can live in. This group will have a quota for resources, image and
flavor settings along with security settings.

Once we have made your group and user you will be sent a password that you should change. Then you can login and
proceed to the **Instances** section on the left side and hit the 'Launch Instance' button.

.. image:: /_static/images/openstack-instance0.png

Launching a new instance
------------------------

After selecting the 'Launch Instance' button you will see this popup.  Here you will enter in the name for the vm, in
this case 'my-instance' afterwards, click "Next".

.. image:: /_static/images/openstack-instance1.png

Select image
~~~~~~~~~~~~

The next page selects which image you want to use. By default the GUI shows you the wrong way to deploy an instance
with our setup. We unfortunately cannot change this until the Pike release. To fix this, select "Image" under the
"Select Boot Source" drop-down and also change "Create New Volume" to "No".

.. image:: /_static/images/openstack-instance1-source1.png

Your screen should now look like what we have below which lists the images you're able to use. Select one of the
images you'd like to use. Scroll down and click "Next" or click "Flavor" on the left side for the next section.

.. image:: /_static/images/openstack-instance1-source2.png

Select flavor
~~~~~~~~~~~~~

The next page selects the "Flavor" of the system which dictates how much CPU, RAM and Disk the instance will be
deployed with. Now click "Next" or "Networks" on the left side.

.. image:: /_static/images/openstack-instance1-flavor.png

Select the network
~~~~~~~~~~~~~~~~~~

This page configures how your instance connects to the network. We currently have one public network that you can use:
"general_servers1". Now click "Security Groups".

.. image:: /_static/images/openstack-instance1-networks.png

Select security group
~~~~~~~~~~~~~~~~~~~~~

Next we need to configure what security groups we want to use. You can think of security groups as firewall rules for
the virtual machine. Generally the default security group should be all you need but you can stack other security
groups on as needed. You can also check what rules are set by clicking on the ">" icon next to the group. Now click
"Next" or "Key Pair".

.. important:: The default security group allows no traffic in. If you want to access your instance from the outside,
               you will need to add rules to allow traffic.

.. image:: /_static/images/openstack-instance1-security-groups.png

Select key pair
~~~~~~~~~~~~~~~

Now we need to select an ssh key pair to use for the VM. If you already have a key added, select it. If not click
"Import Key Pair" to import a public key that you've already created.

.. image:: /_static/images/openstack-instance2.png

Enter a name for the key and paste the **public** key in that you've generated. After you import it, you can select it
and move onto the next screen. After this, you can just click "Launch" which should be blue now.

.. image:: /_static/images/openstack-instance3.png

Advanced usage
~~~~~~~~~~~~~~

For advanced users, you can add custom user data in. For more information on this, checkout the `Cloud-init
documentation`_. Make sure you add ``#cloud-init`` at the top of the section and any other cloud-init configuration
after that in Yaml format.

.. _Cloud-init documentation: https://cloudinit.readthedocs.io/en/latest/topics/examples.html

.. image:: /_static/images/openstack-instance4.png
