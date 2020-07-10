.. _openstack-openpower:

OpenStack on OpenPOWER
======================

These are notes on how the OSUOSL is setting up OpenStack on OpenPOWER (as of May 2020).

Summary
-------

We use Chef as our configuration management tool of choice and have created an environment using the `OpenStack Chef`_
Cookbooks. The compute nodes are running CentOS 7 and the controller node is an x86 virtual machine running CentOS 7.
All storage for the cluster is powered via a `Ceph`_ cluster backed by a 40Gb network.

We have created our own site specific wrapper `OpenStack cookbook`_ that also includes any changes needed to make
OpenStack run on the OpenPOWER platform on CentOS 7. It currently requires some private cookbooks to run however we are
working on removing those requirements.

.. _OpenStack Chef: https://docs.openstack.org/openstack-chef/latest/
.. _OpenStack cookbook: https://github.com/osuosl-cookbooks/osl-openstack
.. _Ceph: https://ceph.com/

Current Images
--------------

We are currently maintaining ppc64le Little endian (LE) and some ppc64 Big Endian (BE) images. Please keep in
mind that IBM is focusing their efforts primarily on LE so don't expect BE support to last for much longer on
various distributions.

The list of operating systems we currently support are (systems which support POWER9 are noted with **P9**):

- CentOS 7.6 BE
- CentOS 7.6 LE (P9)
- Debian 8.11 BE
- Debian 8.11 LE
- Debian 9.9 LE (P9)
- Debian 10.0 LE (P9)
- Fedora 29 LE (P9)
- Fedora 30 LE (P9)
- OpenSUSE 13.2 BE
- OpenSUSE 13.2 LE
- OpenSUSE Leap 15.0 LE (P9)
- OpenSUSE Leap 42.3 LE
- Ubuntu 14.04 BE
- Ubuntu 14.04 LE
- Ubuntu 16.04 BE
- Ubuntu 16.04 BE (32bits)
- Ubuntu 16.04 LE
- Ubuntu 18.04 LE (P9)

Hardware Stack
--------------

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

Software Stack
--------------

Here is the current deployment of OpenStack on OpenPOWER we're using:

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

Specific Changes
----------------

Here are a listing of specific changes we made to get this working on CentOS 7 on OpenPOWER.

Turn off SMT
~~~~~~~~~~~~

The SMT feature in the PPC64 cpu needs to be turned off via running ``/sbin/ppc64_cpu --smt=off``. Otherwise the Little
Endian guests will not run properly.

Loading kvm-hv module
~~~~~~~~~~~~~~~~~~~~~

The ``kvm-hv`` module will need to be loaded and the ``kvm-pr`` should not be loaded.
