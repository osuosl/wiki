Ganeti OSL Infrastructure
=========================

Ganeti is a cluster virtual machine management framework written primarily by
Google. It offers us quite a bit of flexibility in scaling, deploying, and
managing virtual machines. Instead of using ISCSI with a single point of failure
like we currently use, Ganeti will utilize `DRBD`_ which is basically like
having RAID1 (mirroring) over the network.

.. _DRBD: http://www.drbd.org/

From a storage point of view, all the instances (virtual machines) will be using
local storage on the server with a secondary node having its block device synced
via DRBD over a private network. We should be able to handle N+1 failure with
Ganeti (i.e. we can lose at least one node). There is currently no automatic way
of failing instances over if a node goes down.

Instead of using Xen for virtualization, we'll be using `KVM`_, which will
enable us to be 100% free and opensource with this environment. A major plus in
our minds!

.. _KVM: http://www.linux-kvm.org/

Reasons for choosing Ganeti
---------------------------

Our Xen cluster has been a great system overall the last several years, but
lacks many important features:

- Non-redundant storage backend
- Lack of inexpensive scalability (requires expensive storage solutions for
  expansion)
- Hardware doesn't support VT/AMD-V so Xen is our only option
- Xen Dom0 support is not included in the mainline kernel (hard to maintain)
- Aging hardware
- No cluster-wide management
- No automated deployments

The recent outages with our backend iSCSI storage has pushed us to look at other
options. Initially we were looking at using some type of libvirt based solution,
however we discovered Ganeti and decided to give it a look. This was around the
time that ganeti 2.0 was released and offered a large slate of changes and
improvements including support for KVM. Here's a list of the the important
features and reasons we chose Ganeti.

- Ease of node (Dom0) deployment and cluster expansion
- Automated redundant storage (via DRBD)
- Support for KVM (making it much easier to use newer kernels)
- Cluster-wide management of VMs
- Easy to use and unified tools
- Deployment automation
- Reporting and management tools
- Useful API for writing automation scripts
- Responsiveness of the Ganeti Community

With Ganeti, we can write better tools for adding new VMs, and balance loads on
the nodes. It also gives us a cluster-wide view of our virtualization
infrastructure and no longer need to log into each node to interact with the
VMs. Since iSCSI is out of the picture, disk I/O should be much faster with the
use of local disks. We can still run into the risk of I/O starvation but we
should be able to limit it to one or two nodes. Additionally, it allows us to
write tools that will enable our projects more direct access to the VMs for
things like power cycling, console access, etc.

Check out the :doc:`basics of how Ganeti works <how_it_works>` wiki page to have
a better overall understanding of its framework.

Why not use Libvirt?
--------------------

So why not use some type of libvirt based solution? Well there are several
reasons, but the primary one being that its not a cluster-aware application.
Each libvirt node works as a single host. While there are probably some projects
out there that offer the cluster-wise solution, Ganeti is so much easier to
manage with. Using ganeti does mean that we won't be able to use already made
tools such as virt-manager, however it will not take much time to build
something that offers the same features. Ganeti replaces many of the things that
libvirt does and puts it in a cluster mindset instead of a host-by-host mindset.

Infrastructure Overview
-----------------------

Here's an overview of what our Xen and Ganeti infrastructures look like. We
currently host around 60 virtual machines for various projects.

Xen Cluster Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware Summary
^^^^^^^^^^^^^^^^

- 3 Disk nodes (iSCSI) servers
- 14 Xen nodes (Dom0)

Disk Node (Storage)
^^^^^^^^^^^^^^^^^^^

We use three servers running Gentoo Linux with the iSCSI ietd daemon. This is
currently the single point of failure in our system and the cause of many of our
recent problems with VM outages. They suffer from I/O starvation often if a VM
ends up using a lot of disk I/O.

Xen nodes
^^^^^^^^^

We have 14 IBM HS20 blade servers with 4G of RAM that are getting close to 4-5
years old and run as the Dom0 for Xen. Each node has access to all of the iSCSI
luns so that we can do live migrations. Doing migrations is done manually and is
prone to errors sometimes.

Ganeti Infrastructure
~~~~~~~~~~~~~~~~~~~~~

Summary
^^^^^^^

- 4 Ganeti Nodes (Dom0)

Instead of centralized storage accessed over iSCSI, each node (Dom0) in the
cluster uses LVM on top of a redundant RAID configuration for instance storage.
For further redundancy each instances disks are synced across two nodes. In case
of a planned or emergency downtime we can simply move each instance to it's
secondary node where it can resume normal operation. This configuration gives us
an easily managed and highly redundant storage environment while giving the
projects we host faster and more reliable disks than were available on our Xen
cluster.

Nodes
^^^^^

We have 4 HP DL360's with 24G of RAM and 730G of RAID5 storage available on each
node and running Gentoo Linux. Each of these nodes have qemu-kvm installed and
KVM enabled in the hardware and kernel. If we lose one node, we can still keep
all of the VMs online after failing them over.

Once we run out of space in the current cluster, we can simply add another node
and balance out the nodes with some tools. The node does not need to be exactly
the same in specs, which gives us a lot of flexibility if we get hardware
donated to us.
