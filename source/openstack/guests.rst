.. _openstack-guests:

Building OpenStack Guests
=========================

This documentation covers the steps needed to build OpenStack guests using a tool called
`packer`. In addition, we include documentation which covers how to build the images manually in case you run into
issues with packer.

Current Images
--------------

We are currently maintaining these images:

- CentOS 7
- CentOS 8
- Debian 10
- Fedora 31
- Ubuntu 18.04
- OpenSUSE Leap

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

.. note:: For AARCH64, Please run the following commands on one of the machines directly. Please make sure you have the
``AAVMF`` package installed which contains the UEFI firmware to boot the VMs properly.

1. Download the DVD or net install ISO for desired distribution.
2. Create a 3G qcow2 disk image:

.. code-block:: bash

    export DISTRO="debian-10"
    export DISTRO_ISO="debian.iso"
    qemu-img create -f qcow2 $DISTRO.qcow2 3G

3. Boot up the image using kvm manually:

.. code-block:: console

   $ /usr/libexec/qemu-kvm -m 2048M -boot strict=on -name $DISTRO -machine gic-version=3,accel=kvm \
     -cdrom $DISTRO_ISO -netdev user,id=user.0,hostfwd=tcp::2222-:22 \
     -cpu host -monitor none \
     -drive file=$DISTRO.qcow2,if=virtio,cache=writeback,discard=ignore,format=qcow2 \
     -bios /usr/share/AAVMF/AAVMF_CODE.fd
     -vnc 0.0.0.0:99

4. Connect via VNC to the VM and complete the installation

.. code-block:: console

  $ vncviewer $host:99

5. Wait for the VM to complete the install.

6. Compress and import image into OpenStack:

.. code-block:: console

      $ qemu-img convert -O qcow2 -c $DISTRO.qcow2 $DISTRO-compressed.qcow2
      $ source openrc
      $ glance image-create --name $DISTRO --disk-format=qcow2 \
        --container-format=bare < $DISTRO-compressed.qcow2
