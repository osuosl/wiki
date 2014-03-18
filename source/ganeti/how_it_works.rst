.. _ganeti-how-it-works:

How Ganeti works - The Basics
=============================

This document is to help give you a basic understanding of how Ganeti works. If
you'd like to see more detailed information, please visit their `upstream docs`_
site.

.. _upstream docs: http://docs.ganeti.org/ganeti/current/html/

Ganeti is written primarily in python. Each node runs several daemons which take
care of various tasks for Ganeti such as config syncing, instance creation, lvm,
etc. Every Ganeti cluster must have **one** node act as a master. This master is
the only node allowed to run cluster-wide commands such as adding new instances.
Each node can be a master (if setup as a master candidate) and can become a
master.

Communication between the nodes happens via an encrypted connection using a
restful API. It currently only supports Xen, KVM for HVM backends and some
limited support for LXC. The most common setup using using LVM with DRBD to have
a cluster failover solution. It also has support for plain LVM, and file-based
although is less tested. Ganeti handles all of the storage backend setup for LVM
and DRBD so you don't need to worry about that.

All of the remote commands are executed via ssh and require the same ssh key on
every node.

Managing the Cluster
--------------------

Managing all aspects of the cluster is done via ``gnt-`` prefixed commands on
the master node. The ssh host key is copied between all the nodes so that there
should be no warning when you ssh to the host. Here's a list of commands you can
use to manage the cluster:

==============  ==============================================
 command         use                                            
==============  ==============================================
 gnt-cluster     managing cluster-wide actions                  
 gnt-node        manage node-level actions                      
 gnt-instance    manage instance (VM) level actions             
 gnt-backup      manage import/export actions for instances     
 gnt-os          list all operating system types and variants   
 gnt-job         show and manage ganeti jobs                    
==============  ==============================================

All commands are well documented in both man pages and command line based help. You can get help on every command by doing::

    gnt-$command $action --help

When you call a command, Ganeti will communicate to the other nodes it needs to
via the daemons, gather up information about the node, verify several factors,
and then create a job to complete the task. Logs can be found in
``/var/log/ganeti/``. You should look on the master node for more logs however
you may need to look at node specific logs during instance creation, etc. 

Some useful common commands are :doc:`documented here <common_commands>` in more detail.

Instance (VMs) Management
-------------------------

Ganeti uses an OS instance definition to create new VMs. The most common
instance definition is `instance-debootstrap`__ which uses debootstrap to create
a debian-based install. We have written an image based instance definition
called `ganeti-instance-image`__ which lets you use either a tarball, filesystem
dump, or qemu-img file for OS deployments. This allows us to deploy a diverse
environment using upstream installation methods. You need to install the same
instance definition on **ALL** nodes otherwise Ganeti will complain. 

.. __: http://git.ganeti.org/?p=instance-debootstrap.git;a=summary
.. __: http://code.osuosl.org/projects/ganeti-image

The instance definitions almost all use bash, but they could be written in any
language. They have **four** actions:

- create -- create a new instance
- rename -- rename an instance
- export -- export an instance
- import -- import an instance

You can add simple post-install scripts so that you can do things like setup
cfengine.

Exporting/Importing the instances is primarily used when you want to move
between clusters. Most are just tarball filesystem dumps with meta information
about the VM. 
