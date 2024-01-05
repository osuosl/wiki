.. _openstack-details:

OpenStack Details
=================

These are notes on how the OSUOSL is setting up OpenStack (as of January 2024).

Summary
-------

We use Chef as our configuration management tool of choice and have created an environment using the `osl-openstack`_
cookbook. All nodes are running AlmaLinux 8.  All storage for the cluster is powered via a `Ceph`_ cluster backed by a
10Gb network on x86 and AARCH64 and a 40Gb network on POWER.

.. _osl-openstack: https://github.com/osuosl-cookbooks/osl-openstack
.. _Ceph: https://ceph.com/

Hardware Stack (x86)
--------------------

- Controller (1)

  - Physical machine with 10G NICs
  - 96g RAM / 500g disk / 24 CPU

- Compute (18)

  - Eighteen (18) servers, each with:

    - 128G RAM
    - 10Gb NIC

- Storage (12) - (shared between x86 and AARCH64 clusters)

  - 96g RAM
  - Mixture of 4TB, 10TB SATA
  - Various sizes of SSD & NVMe

Hardware Stack (POWER)
----------------------

- Controller (1)

  - Physical machine with 10G NICs
  - 96g RAM / 500g disk / 24 CPU

- Compute (9)

  - Five (5) 8247-22L POWER8 systems w/ 512g RAM
  - Four (5) 9006-12P POWER9 systems w/ 512g RAM

- Storage (5)

  - Five (5) 8001-22C POWER8 systems
  - 256g RAM
  - 7 x 8TB SATA / 4 x 240GB SSD / 1 x 2T NVMe

Hardware Stack (AARCH64)
------------------------

- Controller (1)

  - Physical machine with 10G NICs
  - 96g RAM / 500g disk / 24 CPU

- Compute (12)

  - Twelve (12) Ampere Computing eMAG (HR350A) aarch64 systems w/ 128g RAM

- Storage (12) - (shared between x86 and AARCH64 clusters)

  - 96g RAM
  - Mixture of 4TB, 10TB SATA
  - Various sizes of SSD & NVMe

Software Stack
--------------

Here is the current deployment of OpenStack we are using on all architectures:

- Host Operating System

  - AlmaLinux 8

- OpenStack

  - `OpenStack Train Release`_
  - Packages from `RDO`_

- Ceph

  - `Ceph Nautilus Release`_

.. _OpenStack Train Release: https://releases.openstack.org/train/index.html
.. _RDO: https://www.rdoproject.org
.. _Ceph Nautilus Release: https://docs.ceph.com/en/latest/releases/nautilus/
