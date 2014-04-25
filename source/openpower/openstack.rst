.. _openpower-openstack:

Openstack on OpenPOWER
======================

These are notes on how the OSUOSL is setting up Openstack on OpenPOWER.

.. note::

  These steps are still a work in a progress and may change at anytime.

Summary
-------

For now we are using Fedora 20 as our platform for deploying Openstack on
OpenPOWER. We're using `Packstack`_ as a way to deploy Openstack in an easy
fashion. We are also researching using other methods to manage and deploy
Openstack. This guide currently only shows how to deploy Openstack in a
standalone setting, but we plan to shift that do a cluster-wide configuration.

.. _Packstack: https://wiki.openstack.org/wiki/Packstack

Installation
------------

Install Packstack
~~~~~~~~~~~~~~~~~

Since this is Fedora 20, packstack should be available in the default repos::

  yum install openstack-packstack

Configure Packstack
~~~~~~~~~~~~~~~~~~~

Have packstack create an answers file::

  packstack --allinone --os-neutron-install=n

It should then be prompting you for the system password. Press ``ctrl+c`` to
close it and begin editing the answers file. First thing to do is disable
``ceilometer`` because it requires ``mongodb`` which is not available on PPC64
yet.

The relevant changes are listed here:

.. code-block:: bash

  CONFIG_CEILOMETER_INSTALL=n
  CONFIG_NOVA_COMPUTE_PRIVIF=lo
  CONFIG_NOVA_NETWORK_PUBIF=enP7p1s0f3
  CONFIG_NOVA_NETWORK_PRIVIF=lo
  CONFIG_NOVA_NETWORK_FLOATRANGE=10.1.100.0/24

.. note:: 

  ``CONFIG_NOVA_NETWORK_PUBIF`` and ``CONFIG_NOVA_NETWORK_FLOATRANGE`` are
  variables set for our internal infrastructure.  Also, packstack is not for
  **production** use as it is no longer being developed.

Turn Off SELinux
~~~~~~~~~~~~~~~~

There will be issues if SELinux is set to ``Enforce``. Change it to
``Permissive``

.. note::

  We plan to work on fixing this so that we can run it with SELinux.

Fixing MariaDB
~~~~~~~~~~~~~~

As noted in `RDO`_ workarounds, the mariadb package has an issue on a new
install that causes it not to be able to start up properly.(Please refer to this
link before running the following commands). To fix it::

  yum install -y mariadb-server
  systemctl enable mysqld.service
  rm /usr/lib/systemd/system/mysqld.service
  cp /usr/lib/systemd/system/mariadb.service /usr/lib/systemd/system/mysqld.service
  touch /var/log/mysqld.log
  chown mysql:mysql /var/log/mysqld.log

.. _RDO: http://openstack.redhat.com/Workarounds_2014_01#Failed_to_start_mysqld_.28Fedora_20.29

Installing libguestfs
~~~~~~~~~~~~~~~~~~~~~

``libguestfs`` and ``python-libguestfs`` are currently broken in the Fedora 20
mirrors, and a fix is being worked on. For the moment, you have to compile these
packages from source::

  yum groupinstall "Development Tools"
  wget http://ppc.koji.fedoraproject.org/kojifiles/packages/libguestfs/1.24.81.fc20/src/libguestfs-1.24.8-1.fc20.src.rpm
  yum-builddep libguestfs-1.24.8-1.fc20.src.rpm
  yum install hfsplus-tools
  rpmbuild --rebuild libguestfs-1.24.8-1.fc20.src.rpm --nocheck
  yum localinstall ~/rpmbuild/RPMS/ppc64/libguestfs-1.24.8-1.fc20.ppc64.rpm \ 
    ~/rpmbuild/RPMS/ppc64/python-libguestfs-1.24.8-1.fc20.ppc64.rpm

Install Openstack
~~~~~~~~~~~~~~~~~

Run the packstack setup:

.. code-block:: bash

  # $answers is the answers.txt file that was generated at the beginning.
  packstack --answer-file=$answers

KVM
~~~

Make sure all the kvm modules are loaded::

  modprobe kvm_pr
  systemclt openstack-nova-compute restart

.. note::

  To work around the ``ceilometer`` issue, one option is maybe using an x86_64
  host as a controller.

Fixing Firewalld After Reboot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Right now if you reboot any of the powerkvm boxes, the firewalld settings are not saved properly.

To fix this just re-run the packstack script:

.. code-block:: bash

  # $answers is the answers.txt file that was generated at the beginning.
    packstack --answer-file=$answers
