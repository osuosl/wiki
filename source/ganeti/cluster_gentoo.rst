.. _ganeti-cluster-gentoo:

Building a Ganeti Cluster on Gentoo
===================================

Configuring DNS
---------------

Ganeti requires the following names to resolve

- A name for the cluster as a whole, this IP must be available
  (cluster.example.org)
- A name for each node (node1.example.org)
- A name for each instance (instance1.example.org)

Building a Node
---------------

You'll probably want to configure at least two nodes as follows. Ganeti makes it
easy to add or remove nodes later. Ganeti can work in a standalone mode for LVM
only (no DRBD) disk storage.

DRBD Kernel
~~~~~~~~~~~

DRBD requires you to set one kernel option::

    Device Drivers --->
        <*> Connector - unified userspace <-> kernelspace linker

DRBD is included in the mainline kernel in version 2.6.33 and later. You can
enable it here::

    Device Drivers  --->
    [*] Block devices  --->
    <*>   DRBD Distributed Replicated Block Device support

Go ahead and set this, recompile and reboot if necessary. If not, you still need
to make sure you have the ``/usr/src/linux`` symlink updated for the kernel you
are running, and (I think) run ``make modules_prepare``.

For a normal installation with drbd compiled in::

    emerge drbd

If you want to use the upstream drbd kernel modules, do the following::

    emerge drbd drbd-kernel

This will pull in ``sys-cluster/drbd-kernel`` which will compile the DRBD kernel
module for the kernel at ``/usr/src/linux``. Whenever you upgrade your kernel
you'll need to update the symlink and reemerge ``drbd-kernel``. \ Now go ahead
and load the drbd module::

    modprobe drbd minor_count=255 

If you're using DRBD 8.2.x or newer you need to use the following options::

    modprobe drbd minor_count=255 usermode_helper=/bin/true

.. code-block:: bash

    echo "drbd minor_count=255 usermode_helper=/bin/true" >> \
      /etc/modules.autoload.d/kernel-2.6

If you have DRBD compiled as a built-in module, add the following to your kernel
argument line in grub.conf::

    drbd.minor_count=255 drbd.usermode_helper=/bin/true

And make sure it will be automatically loaded at boot in the future

Install Ganeti
~~~~~~~~~~~~~~

Set the appropriate USE flags. In this case we will be using ``kvm``. If you
want an actual cluster you'll need ``drbd`` as well.

.. code-block:: bash

    echo "app-emulation/ganeti kvm drbd" >> /etc/portage/package.use

Now go ahead and install ganeti::

    emerge -av app-emulation/ganeti

Configure Networking
~~~~~~~~~~~~~~~~~~~~

Ideally you should have a 'public' network that will be used for communicating
with the nodes and instances from the outside, and a 'backend' network that will
be used by ganeti for DRBD, migrations, etc. Assuming your 'public' IP (which
node1.example.org should resolve to) is ``10.1.0.11`` and your 'backend' IP is
``192.168.1.11``, you should edit ``/etc/conf.d/net`` to look something like
this:

.. code-block:: bash

    bridge_br0="eth0"
    config_eth0=( "null" )

    config_br0=( "10.1.0.11 netmask 255.255.254.0" )
    routes_br0=( "default gw 10.1.0.1" )

    # make sure eth0 is up before configuring br0
    depend_br0() {
            need net.eth0
    }

    config_eth1=( "192.168.1.11 netmask 255.255.255.0" )

Set the Hostname
~~~~~~~~~~~~~~~~

Ganeti is picky about hostnames, and requires that the output of ``hostname`` be
fully qualified. So make sure ``/etc/conf.d/hostname`` looks like this

.. code-block:: bash

    HOSTNAME="node1.example.org"

**NOT** like this

.. code-block:: bash

    HOSTNAME="node1"

Configure LVM and DRBD
~~~~~~~~~~~~~~~~~~~~~~

"Configuring" DRBD is easy, since ganeti will do all the real work. All we need
is for the service to start successfully, so just do::

    touch /etc/drbd.conf

It is recommended that you edit this line in ``/etc/lvm/lvm.conf``::

    filter = [ "r|/dev/nbd.*|", "a/.*/", "r|/dev/drbd[0-9]+|" ]

The important part is the "r|/dev/drbd[0-9]+|" entry, which will prevent LVM
from scanning drbd devices.

.. note::

    If you are using HP hardware raid you will also need to set
    ``preferred_names = [ "^/dev/cciss/" ]``

Now, go ahead and create an LVM volume group with the disks you plan to use for
instance storage. The default name that Ganeti prefers is ``xenvg`` but we
recommend you choose something more useful for your infrastructure.

.. code-block:: bash

    pvcreate /dev/cciss/c0d0p4   # Thats HP hardware raid
    lvcreate xenvg /dev/cciss/c0d0p4

Building the Cluster
--------------------

Initialize the Cluster
~~~~~~~~~~~~~~~~~~~~~~

On the first node go ahead and run::

    gnt-cluster init -b br0 --master-netdev br0 -s [secondary-ip] \
      --enabled-hypervisors=kvm -t kvm \
      --hypervisor-parameters kvm:kernel_path:[path-to-kvm-kernel] \
      -g xenvg \
      [clustername]

[path-to-kvm-kernel]
  can be left blank if you want to supply kernels from within the guests. This
  can be changed later or on a per-instance basis.

[clustername]
  must resolve to an available IP address (but does not need to be a FQDN: for
  example ``ganeti`` where ``ganeti.example.org`` is the FQDN.). Ganeti will
  bring this IP address up on the master node, so you can always ssh to it.

[secondary-ip]
  this is 'private' IP mentioned previously

Adding a Node
~~~~~~~~~~~~~

Now you can add a second node to your cluster with::

    gnt-node add -s [secondary-ip] [nodename]

[secondary-ip]
  is the IP of the new node

[nodename]
  must resolve, but need not be fully qualified. For example ``node2`` where
  ``node2.example.org`` is the FQDN.

