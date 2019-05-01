.. _openpower-openstack-guests:

Building Openstack OpenPOWER Guests
===================================

This documentation covers the steps needed to build an Openstack guests on OpenPOWER using a tool called `packer`. In
addition, we include documentation which covers how to build the images manually in case you run into issues with
packer.

Current Images
--------------

We are currently maintaining ppc64le Little endian (LE) and some ppc64 Big Endian (BE) images. Please keep in mind that
IBM is focusing their efforts primarily on LE so don't expect BE support to last for much longer on various
distributions.

The list of operating systems we currently support are (systems which support POWER9 are noted with **P9**):

- CentOS 7.5 BE
- CentOS 7.6 LE (P9)
- Debian 8.11 BE
- Debian 8.11 LE
- Debian 9.9 LE (P9)
- Fedora 28 BE
- Fedora 28 LE (P9)
- Fedora 29 LE (P9)
- Fedora 30 LE (P9)
- OpenSUSE 13.2 BE
- OpenSUSE 13.2 LE
- OpenSUSE Leap 15.0 LE (P9)
- OpenSUSE Leap 42.3 LE
- Ubuntu 14.04 BE
- Ubuntu 14.04 BE
- Ubuntu 16.04 BE
- Ubuntu 16.04 BE (32bits)
- Ubuntu 16.04 LE
- Ubuntu 18.04 LE (P9)

If there are any images you would like us to create, please let us know.

Building images with packer
---------------------------

We build all of our images using `packer`_ via our `packer-templates`_ github repo. Builds are triggered via opening a
pull request with the changes that are needed. Once an image has been built, `openstack_taster`_ will test to ensure
the images will work properly on our openstack cluster.

.. _packer: http://www.packer.io/
.. _packer-templates: https://github.com/osuosl/packer-templates
.. _openstack_taster: https://github.com/osuosl/openstack_taster

Manual Guest Installation
-------------------------

.. note:: This is only useful for manually testing some images and is no longer used for building images.

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
