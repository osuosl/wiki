.. _openpower-openstack:

Openstack on OpenPOWER
======================

These are notes on how the OSUOSL is setting up Openstack on OpenPOWER.

.. note::

  These steps are still a work in a progress and may change at anytime.

Summary
-------

We use Chef as our configuration management tool of choice and have created an
environment using the `StackForge`_ Chef Cookbooks. The compute nodes are
running Fedora 20 and the controller node is an x86 virtual machine running
CentOS 6.6.

We have created our own site specific `Openstack cookbook`_ that also includes any
changes needed to make Openstack run on the OpenPOWER platform on Fedora 20. It
currently requires some private cookbooks to run (namely the firewall), and
lacks some documentation.

.. _StackForge: https://github.com/stackforge
.. _Openstack cookbook: https://github.com/osuosl-cookbooks/osl-openstack

Software Stack
--------------

Here is the current deployment of OpenStack on OpenPOWER we're using:

- Host Operating Systems

  - CentOS 6.6 x86_64 VM (keystone/glance/horizon)
  - Fedora 20 ppc64 (nova/cinder)

- OpenStack

  - OpenStack Icehouse
  - Packages from `RDO`_

.. _RDO: https://www.rdoproject.org

Reasons for using Fedora
------------------------

Fedora wasn't our first choice for the OS running on the compute nodes because
of its fast pace nature, however the IBM engineers recommended we use that for
now because it was easier to get newer bug fixes included. Our goal is to
eventually use CentOS 7 on the compute nodes once support has been completed.

Specific Changes
----------------

Here are a listing of specific changes we made to get this working on Fedora 20
on OpenPOWER.

Turn Off SELinux
~~~~~~~~~~~~~~~~

There will be issues if SELinux is set to ``Enforce``. Change it to
``Permissive``. We haven't had time to figure out the exact problem with the
SELinx permissions.

Install newer versions of packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some packages need to be newer than what comes from Fedora 20 and so we created
a new `repository`_ with the packages we needed. All of these packages have been
compiled from the Fedora rawhide repository. The list of packages that needed to
be upgraded are:

- kernel
- libvirt
- libvirt-python
- qemu
- seabios
- SLOF

.. _repository: http://ftp.osuosl.org/pub/osl/repos/yum/openpower/f20/ppc64/

Turn off SMT
~~~~~~~~~~~~

The SMT feature in the PPC64 cpu needs to be turned off via running
``/sbin/ppc64_cpu --smt=off``. Otherwise the Little Endian guests will not run
properly.

Loading kvm-hv module
~~~~~~~~~~~~~~~~~~~~~

The ``kvm-hv`` module will need to be loaded and the ``kvm-pr`` should not be
loaded.

Chef specific changes
~~~~~~~~~~~~~~~~~~~~~

Much of the Fedora support in the Openstack cookbooks has been removed, however
most of the changes were done in the attributes. We have included some changes
in our ``osl-openstack`` cookbook to fix those. The majority of the changes are:

- Setting correct package names for Fedora on a few attributes
- Setting the correct yum repository for Fedora and adding it
