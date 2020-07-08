.. _openstack-x86:

Openstack on x86_64
===================

These are notes on how the OSUOSL is setting up Openstack on x86_64 (as of May 2020).

Summary
-------

We use Chef as our configuration management tool of choice and have created an environment using the `OpenStack Chef`_
Cookbooks. The compute nodes are running CentOS 7 and the controller node is an x86 virtual machine running CentOS 7.
All storage for the cluster is powered via a `Ceph`_ cluster backed by a 10Gb network.

We have created our own site specific wrapper `Openstack cookbook`_ that also includes any changes needed to make
Openstack run on the x86 platform on CentOS 7. It currently requires some private cookbooks to run however
we are working on removing those requirements.

.. _OpenStack Chef: https://docs.openstack.org/openstack-chef/latest/
.. _Openstack cookbook: https://github.com/osuosl-cookbooks/osl-openstack
.. _Ceph: https://ceph.com/

Hardware Stack
--------------

- Controller (1)

  - One (1) x86_64 Virtual Machine running on Ganeti with KVM
  - 8g RAM / 10g disk / 8 vCPU

- Compute (8)

  - Eight (8) servers, each with:
    - 2 x Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz
    - 128G RAM
    - 10Gb NIC

- Storage (8)

  - Eight (8) Dell PowerEdge R710
  - 64g RAM
  - 6 x 4TB SATA / 1 x 800GB NVMe

Software Stack
--------------

Here is the current deployment of OpenStack on x86 we're using:

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
