.. _openstack-details:

OpenStack Details
=================

These are notes on how the OSUOSL is setting up OpenStack (as of August 2026).

Summary
-------

We use Chef as our configuration management tool of choice and have created an environment using the `osl-openstack`_
cookbook. All nodes are running AlmaLinux 9, except the POWER nodes which are still on AlmaLinux 8. All storage for
the cluster is powered via a `Ceph`_ cluster backed by a 10Gb network on x86 and AARCH64 and a 40Gb network on POWER.

.. _osl-openstack: https://github.com/osuosl-cookbooks/osl-openstack
.. _Ceph: https://ceph.com/

Hardware Stack (x86)
--------------------

- Controller (2)

  - One (1) Dell PowerEdge R620 w/ 192g RAM / 24 cores
  - One (1) Intel S2600KP w/ 128g RAM / 12 cores

- Compute (10)

  - Eight (8) Inspur NE5260M5 systems w/ 768g RAM / 56 cores
  - One (1) GIGABYTE R181-2A0-ZB system w/ 256g RAM / 48 cores
  - One (1) Dell PowerEdge R640 system w/ 384g RAM / 32 cores

- Storage (20) - (shared between x86 and AARCH64 clusters)

  - Monitors (3)

    - Three (3) Dell PowerEdge R430 systems w/ 128g RAM / 16 cores

  - OSD nodes (17)

    - Eleven (11) HDD nodes w/ 128g RAM, eight (8) drives each, mixture of 4TB, 8TB and 10TB SATA
    - Six (6) SSD nodes w/ 128-256g RAM, eight (8) 1.92TB SSDs each
    - NVMe (800GB and 2TB) for journals on the HDD nodes

Hardware Stack (POWER)
----------------------

- Controller (2)

  - One (1) Dell PowerEdge R620 w/ 128g RAM / 24 cores
  - One (1) Intel S2600KP w/ 128g RAM / 12 cores

- Compute (6)

  - Four (4) 9006-12P POWER9 systems w/ 512g RAM
  - One (1) 9043-MRX POWER10 system w/ 2T RAM
  - One (1) 9105-42A POWER10 system w/ 2T RAM

- Storage (5)

  - Five (5) 8001-22C POWER8 systems
  - 256g RAM / 16 cores
  - 7 x 8TB SATA / 3 x 240GB SSD / 2 x 2TB SSD / 1 x 2TB NVMe

Hardware Stack (AARCH64)
------------------------

- Controller (2)

  - One (1) Intel S2600KP w/ 128g RAM / 12 cores
  - One (1) Dell PowerEdge R620 w/ 48g RAM / 12 cores

- Compute (10)

  - Five (5) FOXCONN Mt. Collins (Ampere Altra) systems w/ 256g RAM / 160 cores
  - Five (5) Lenovo HR350A (Ampere eMAG) systems w/ 128g RAM / 32 cores

- Storage

  - Shared with the x86 cluster; see `Hardware Stack (x86)`_

Software Stack
--------------

Here is the current deployment of OpenStack we are using on all architectures:

- Host Operating System

  - AlmaLinux 9
  - The POWER nodes are still on AlmaLinux 8 and will be upgraded to 9 soon

- OpenStack

  - `OpenStack Yoga Release`_
  - Packages from `RDO`_

- Ceph

  - `Ceph Reef Release`_

.. _OpenStack Yoga Release: https://releases.openstack.org/yoga/index.html
.. _RDO: https://www.rdoproject.org
.. _Ceph Reef Release: https://docs.ceph.com/en/latest/releases/reef/
