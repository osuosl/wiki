.. _openpower-openstack-guests:

Building Openstack OpenPOWER Guests
===================================

This documentation covers the steps needed to build an Openstack guests on
OpenPOWER KVM using both `packer` and also manually.

Unfortunately we can't use `packer`_ yet for building images so for now we'll need
to build them manually on the OpenPOWER boxes. For now we should **only** be
building images on the hardware itself and not use QEMU emulation on x86. While
it may work, we have this method as a confirmed way to build the images. All of
the configuration and scripts used for building the images are included in our
`packer-templates`_ github repo.

.. _packer: http://www.packer.io/
.. _packer-templates: https://github.com/osuosl/packer-templates

.. note::

    All guests will have their output directed to the serial console by default.

Current Images
--------------

We are maintaining ppc64 Big Endian (BE) and ppc64le Little Endian (LE) images
on our FTP mirrors. The list of operating systems we currently support are:

- Fedora 22 Alpha LE/BE
- Fedora 21 LE/BE
- Fedora 20 BE
- Ubuntu 15.04 LE
- Ubuntu 14.04 LE/BE
- Debian 8 LE/BE
- Debian 7 BE
- OpenSUSE 13.2 LE/BE

If there are any images you would like us to create, please let us know.

.. _FTP mirrors: http://ftp.osuosl.org/pub/osl/openpower/openstack/

Manual Guest Installation
-------------------------

Please run the following commands on one of the OpenPOWER machines directly.

1. Download the DVD or net install ISO for desired distribution.
2. Create a 3G qcow2 disk image:

.. code-block:: bash

    export DISTRO="debian-9"
    export DISTRO_ISO="debian-9.5.0-ppc64el-netinst.iso"
    qemu-img create -f qcow2 $DISTRO.qcow2 3G

3. Boot up the image using kvm manually:

.. code-block:: console

   $ /usr/libexec/qemu-kvm -m 2048M -boot strict=on -name $DISTRO -machine type=pseries,accel=kvm \
     -cdrom $DISTRO_ISO -netdev user,id=user.0,hostfwd=tcp::2222-:22 \
     -device virtio-net,netdev=user.0 \
     -drive file=$DISTRO.qcow2,if=virtio,cache=writeback,discard=ignore,format=qcow2 \
     -vnc 0.0.0.0:99

4. Connect via VNC to the VM and complete the installation

.. code-block:: console

  $ vncviewer $host:99

5. Wait for the VM to complete the install.

6. Compress and import image into Openstack:

.. code-block:: console

      $ qemu-img convert -O qcow2 -c $DISTRO.qcow2 $DISTRO-compressed.qcow2
      $ source openrc
      $ glance image-create --name $DISTRO --disk-format=qcow2 \
        --container-format=bare < $DISTRO-compressed.qcow2
