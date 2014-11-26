.. _openpower-openstack_instances:

Instances for OpenStack
=======================

This is a walk through for people using our clusters for OpenPower virtual
machines.

Groups and Users
----------------
You need to first have a group which your user can live in.  If your
organization doesn't already have group in OpenStack (on the cluster you
desire, either x86 or OpenPower).  This group will have a quota for resources,
image and flavor settings along with security settings.

Once we have made your group and user you will be sent a password that you
should change.  Then you can login and proceed to the Instances section on the
left side and hit the '+ Launch Instance' button.

.. image:: /_static/images/openstack-instance0.png

Launching a new instance
------------------------
After selecting the '+ Launch Instance' button you will see this popup.
Here you will select either Power7+ or Power8 in the Availability Zone.
Flavor refers to the specs of the VM, you can request custom ones.
You will want to Boot from image and then select the OS of your choice
.. image:: /_static/images/openstack-instance1.png


Your Key Pair can be saved to your user account or you can add another:

.. image:: /_static/images/openstack-instance2.png


Use a passphrased ssh-key

.. image:: /_static/images/openstack-instance3.png


For advanced users

.. image:: /_static/images/openstack-instance4.png


Again this is probably not needed

.. image:: /_static/images/openstack-instance5.png


**Hit Launch**
