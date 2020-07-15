.. _openstack-details:

OpenStack Details
=================

These are notes on how the OSUOSL is setting up OpenStack (as of July 2020).

Summary
-------

We use Chef as our configuration management tool of choice and have created an environment using the `OpenStack Chef`_
Cookbooks. The compute nodes are running CentOS 7 and the controller node is an x86 virtual machine running CentOS 7.
All storage for the cluster is powered via a `Ceph`_ cluster backed by a 10Gb network on x86 and AARCH and a 40Gb 
network on POWER.

We have created our own site specific wrapper `OpenStack cookbook`_ that also includes any changes needed to make
OpenStack run on the varying architectures. It currently requires some private cookbooks to run, however we are
working on removing those requirements.

.. _OpenStack Chef: https://docs.openstack.org/openstack-chef/latest/
.. _OpenStack cookbook: https://github.com/osuosl-cookbooks/osl-openstack
.. _Ceph: https://ceph.com/

Hardware Stack (x86)
--------------------

- Controller (1)

  - One (1) x86_64 Virtual Machine running on Ganeti with KVM
  - 8g RAM / 10g disk / 8 vCPU

- Compute (8)

  - Eight (8) servers, each with:

    - 2 x Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz
    - 128G RAM
    - 10Gb NIC

- Storage (8) - (shared between x86 and AARCH clusters)

  - Eight (8) Dell PowerEdge R710
  - 64g RAM
  - 6 x 4TB SATA / 1 x 800GB NVMe

Hardware Stack (POWER)
----------------------

- Controller (1)

  - One (1) x86_64 Virtual Machine running on Ganeti with KVM
  - 24g RAM / 20g disk / 8 vCPU

- Compute (9)

  - Five (5) 8247-22L POWER8 systems w/ 512g RAM
  - Four (5) 9006-12P POWER9 systems w/ 512g RAM

- Storage (5)

  - Five (5) 8001-22C POWER8 systems
  - 256g RAM
  - 8 x 8TB SATA / 4 x 240GB SSD

POWER-Specific Changes
^^^^^^^^^^^^^^^^^^^^^^

Turn off SMT
""""""""""""

The SMT feature in the PPC64 cpu needs to be turned off via running ``/sbin/ppc64_cpu --smt=off``. Otherwise the Little
Endian guests will not run properly.

Loading kvm-hv module
"""""""""""""""""""""

The ``kvm-hv`` module needs to be loaded and the ``kvm-pr`` should not be loaded.

Hardware Stack (AARCH64)
------------------------

- Controller (1)

  - One (1) x86_64 Virtual Machine running on Ganeti with KVM
  - 24g RAM / 20g disk / 8 vCPU

- Compute (12)

  - Twelve (12) Ampere Computing eMAG (HR350A) aarch64 systems w/ 128g RAM

- Storage (8) - (shared between x86 and AARCH clusters)

  - Eight (8) Dell PowerEdge R710
  - 64g RAM
  - 6 x 4TB SATA / 1 x 800GB NVMe

Software Stack
--------------

Here is the current deployment of OpenStack we are using on all architectures:

- Host Operating System

  - CentOS 7
  - Compute nodes running a mainline 5.4.x kernel

- OpenStack

  - `OpenStack Rocky Release`_
  - Packages from `RDO`_

- Ceph

  - `Ceph Mimic Release`_

.. _OpenStack Rocky Release: https://releases.openstack.org/rocky/highlights.html
.. _RDO: https://www.rdoproject.org
.. _Ceph Mimic Release: https://ceph.com/releases/v13-2-0-mimic-released/
