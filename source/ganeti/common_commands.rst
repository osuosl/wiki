.. _ganeti-common-commands:

Common Ganeti Commands
======================

Here's a list of some common useful commands with Ganeti. If you want more
detailed information, be sure to read the related gnt-* man pages and the
`online documentation`_.

.. _online documentation: http://ganeti-doc.googlecode.com/svn/ganeti-2.1/html/index.html

Basics
------

Ganeti is a cluster virtualization environment and allows you to manage all VMs
from one single master host. You should always connect to the master DNS name
and never individual host. Lets use ganeti.osuosl.org as our master host for the
following commands.

All of Ganeti's commands have a ``gnt-`` prefix. The commands you'll use the
most are tied to the ``gnt-instance`` command which interacts with your VMs. You
can find simple help output by typing ``gnt-instance`` and find specific command
help by typing ``gnt-instance <command> --help``.

First, ssh to the master ganeti host for your cluster.

Commands
--------

- :ref:`instance-commands`
- :ref:`cluster-commands`
- :ref:`node-commands`
- :ref:`tips-and-tricks`

.. _instance-commands:

Instance Commands
-----------------

Here's a list of common instance, or virtual machine commands.

Starting an Instance
~~~~~~~~~~~~~~~~~~~~

::

    gnt-instance start <instance>

You can also do cool stuff like starting all the instances on a specific node::

    gnt-instance start --primary <nodename>

Stopping an Instance
~~~~~~~~~~~~~~~~~~~~

::

    gnt-instance shutdown <instance>

And to stop all nodes on a specific node::

    gnt-instance shutdown --primary <nodename>

If you want to quickly shutdown a VM (or otherwise known as destroy), use the
following command::

    gnt-instance shutdown --timeout=0 <instance>

Connecting to the Console
~~~~~~~~~~~~~~~~~~~~~~~~~

All of our VMs have a serial console enabled::

    gnt-instance console <instance>

To escape out of the console type ``ctrl+]``.

If you want to start and connect to the console immediately after, you can run
the following command. Unfortunately, there is no way currently to do this in a
single command in ganeti.

::

    gnt-instance start <hostname> && gnt-instance console <hostname>

Migrating an Instance
~~~~~~~~~~~~~~~~~~~~~

If you'd like to do a live migration of an instance to its secondary host, run
the following command::

    gnt-instance migrate <instance>

Failing over an Instance
~~~~~~~~~~~~~~~~~~~~~~~~

Failing over an instance its just like migrating except its done with the
instance offline so its not live::

    gnt-instance failover <instance>

Adding a new Instance
~~~~~~~~~~~~~~~~~~~~~

Adding a new instance is generally easy however there are a lot of things to
consider in your situation::

    gnt-instance add -t drbd -s 10G -o image+debian \
      --net 0:link=br100 -B memory=512M \
      -H kvm:kernel_path="/boot/guest/vmlinuz-x86_64" \
      --no-start -I hail <instance>.osuosl.org

This will do the following:

=================================================== =========================================================
``add``                                             start an add action
``-t drbd``                                         use the DRBD disk template
``-s 10G``                                          set the OS disk size to 10G
``-o image+debian``                                 Use the ``image`` instance with the ``debian`` OS Variant
``--net 0:link=br100``                              Set the network bridge to br100 (VLAN 100 in our case)
``-B memory=512M``                                  Set the VM memory to 512M
``-H kvm:kernel_path="/boot/guest/vmlinuz-x86_64"`` Set the kernel_path to a specific kernel we want
``--no-start``                                      Don't start the VM after it finishes building
``-I hail``                                         Use the hail iallocator for automatic allocation
``<instance>.osuosl.org``                           FDQN of the node we're adding 
=================================================== =========================================================

You also may have a cluster-wide default set of settings for instances. To see
what those settings are, run::

    gnt-cluster info

So unless you need to change from the default, you can just type the following
instead::

    gnt-instance add -t drbd -s 10G -o image+debian \
      --no-start -I hail <instance>.osuosl.org

Multi-VG Support
~~~~~~~~~~~~~~~~

Ganeti also supports multiple VG's which are nice if you have a set of SSD's and
regular disks and want them on different VGs. This feature isn't documented
nearly as well so we're doing it here. Assume doing the same instance add from
above, but instead you want to put it on the ``ganeti-ssd`` VG::

    gnt-instance add -t drbd --disk 0:vg=ganeti-ssd,size=10G -o image+debian \
      --no-start -I hail <instance>.osuosl.org

Booting from a CD ISO
~~~~~~~~~~~~~~~~~~~~~

Sometimes you want to install an OS manually from an ISO, here's how you do it.
The first step is to create a VM using the ``--no-install`` option which creates
a VM with just storage setup, no OS installed:

.. code-block:: bash

    # disable serial console
    gnt-instance modify -H serial_console=false <instance>

    # disable kernel
    gnt-instance modify -H kernel_path="" <instance>

    # boot with iso
    gnt-instance start -H \
      boot_order=cdrom,cdrom_image_path=/path/to/debian-504-amd64-netinst.iso <instance>

Now you'll need to connect to the VNC port for the instance and do the install
via that. You can find that information out by doing and "info" on the instance.

Changing Secondary disks
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to change where the secondary storage for a instance to a different
node, the following command will do that::

    gnt-instance replace-disks -n <new node> <instance>

This can be done live while the instance is still running.

Switching disk templates
~~~~~~~~~~~~~~~~~~~~~~~~

If you need to change an instance from using a plain LVM disk template to DRBD,
issue the following command.

.. code-block:: bash

    # make sure the instance is down
    gnt-instance shutdown <instance>

    # change to drbd adding the new node as the secondary
    gnt-instance modify -t drbd -n <secondary node> <instance>

    # start instance
    gnt-instance start <instance>

If you need to switch from the DRBD disk template to plain, replace the drbd
command with the following below. Whichever node is listed as the secondary at
the time will have its volumes removed.

.. code-block:: bash

    # switch back to plain
    gnt-instance modify -t plain <instance>

Moving an instance to another node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Say you have an instance that isn't using DRBD but you want to move it to
another node in the cluster::

    gnt-instance move -n <primary node> <instance>

Migrate existing LVM volume
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use an LVM volume that already has a guest OS installed on it,
you can use Ganeti to put it into its control. This currently only works with
the plain disk template and if the volume is in the same volume group that
ganeti is using::

    gnt-instance add -t plain -o <os-type> \
      --disk 0:adopt=<lvname> -n <node> <instance>

For example, if the device is ``/dev/ganeti/instance1``, you would use
"``adopt=instance1``". This will **not** run any OS installation scripts.

Adding network interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~

Say you need to add another network interface for an instance::

    gnt-instance modify --net add:link=<bridge interface> <instance>
    gnt-instance reboot <instance>

For example, if you want an instance to have eth1 on the backend network, you'd
use ``add:link=br42``.

Adding disks
~~~~~~~~~~~~

Say you need to add another disk to an instance::

    gnt-instance modify --disk add:size=<disk size> <instance>
    gnt-instance reboot <instance>

For example, if you want a new 20G disk to an instance, you'd use
``add:size=20G``.

.. _cluster-commands:

Cluster Commands
----------------

Creating a new Cluster
~~~~~~~~~~~~~~~~~~~~~~

Say you want to create a new cluster that:

- uses br42 as the primary interface for Ganeti communication
- node uses 10.1.11.200 as the DRBD ip
- enable KVM
- set the default bridged interface for instances to br113
- set the default KVM settings to 2 vpus & 512M RAM
- set the default kernel path to ``/boot/guest/vmlinuz-x86_64``
- the master DNS name is ganeti-cluster.osuosl.org

::

    gnt-cluster init --master-netdev=br42 \
      --vg-name ganeti \
      -s 10.1.11.200 \
      --enabled-hypervisors=kvm \
      -N link=br113 \
      -B vcpus=2,memory=512M \
      -H kvm:kernel_path=/boot/guest/vmlinuz-x86_64 \
      ganeti-cluster.osuosl.org

Verifying Cluster Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify general cluster integrity, run::

    gnt-cluster verify

If you encounter any issues, check out `Common Cluster Problems`_ in their
documentation.

.. _Common Cluster Problems: http://docs.ganeti.org/ganeti/current/html/walkthrough.html#common-cluster-problems

You can also check the integrity of just disks::

    gnt-cluster verify-disks

Becoming a Master Node
~~~~~~~~~~~~~~~~~~~~~~

If you'd like to change which node is master, ssh to the node you want to become
master and type the following::

    gnt-cluster masterfailover

Modifying Cluster Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you'd like to modify some of the cluster settings, you can do the following.

.. code-block:: bash

    # change default vcpus, and memory settings for instances
    gnt-cluster modify -B vcpus=2,memory=512M

    # change default kernel
    gnt-cluster modify -H kvm:kernel_path=/boot/guest/vmlinuz-x86_64

    # change default instance bridge interface
    gnt-cluster modify -N link=br113

Viewing Cluster Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see the cluster information::

    gnt-cluster info

.. _node-commands:

Node Commands
-------------

Adding a New Node
~~~~~~~~~~~~~~~~~

You've installed a new Ganeti server and want to add it to the cluster::

    gnt-node add -s <drbd_ip> <hostname>

If this node was previously in the cluster, you should add ``**--readd**``.

List all Nodes
~~~~~~~~~~~~~~

::

    gnt-node list

Mark node offline
~~~~~~~~~~~~~~~~~

If you need to do maintenance on node, you should mark it offline in ganeti so
that it doesn't try to communicate with it. But before you do that, you need to
migrate all the instances off of it.

.. code-block:: bash

    # migrate instances to secondary nodes
    gnt-node migrate <node>

    # if the node is offline, use this
    gnt-node failover <node>

    # now mark it offline
    gnt-node modify -C no -O yes <node>

Evacuate all storage on a Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to remove all the instances from a node, you need to do this in
several steps. First you need to migrate all the primary instances on the node
to their secondary. Next you need to evacuate all instances that have secondary
storage on the node to new nodes.

.. code-block:: bash

    # Migrate all the primary instances
    gnt-node migrate <node>

    # Evacuate the node
    gnt-node evacuate -I hail <node>

Remove a node from the Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to remove a node completely from the cluster, you can use the
following command. You must **remove or migrate all instances** on the node
**before** you can run this command!!

::

    gnt-node remove <node>

.. _tips-and-tricks:

Tips and Tricks
---------------

Handy Bash Aliases
~~~~~~~~~~~~~~~~~~

There's a few commands that we run quite often and getting annoying typing out
completely, so here's a few handy bash aliases we've created to help out. You
can put these in your .bashrc files to use them.

Connecting to console on start
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You want to start and immediately connect to the console.

.. code-block:: bash

    # .bashrc
    gnt-consolestart () { gnt-instance start $1 && gnt-instance console $1; }

    # usage
    gnt-consolestart <hostname>

Destroy running Instance
^^^^^^^^^^^^^^^^^^^^^^^^

Say you need to stop or "destroy" a running instance immediately.

.. code-block:: bash

    # .bashrc
    gnt-destroy () { gnt-instance shutdown --timeout=0 $1 ; }

    # usage
    gnt-destroy <hostname>
