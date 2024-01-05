.. _openstack-guests:

OpenStack Guest Images
======================

This documentation covers the steps needed to build OpenStack guests using a tool called `packer`. In addition,
we include documentation which covers how to build the images manually in case you run into issues with packer.

Current Images
--------------

We are currently maintaining these images:

.. csv-table::
   :file: ./csv/images.csv
   :widths: 40, 15, 15, 15, 15
   :header-rows: 1

We are currently only maintaining ppc64le Little endian (LE) images for POWER8/9. IBM is focusing their efforts
primarily on LE, so Big endian (BE) support is limited to only Debian Sid (unstable) As all other distributions have
removed support for BE.

If there are any other images you would like us to create, please let us know.

Building images with packer
---------------------------

We build all of our images using `packer`_ via our `packer-templates`_ github repo.

.. _packer: http://www.packer.io/
.. _packer-templates: https://github.com/osuosl/packer-templates

Manual Guest Installation
-------------------------

.. note:: This is only useful for manually testing some images and is no longer used for building images.

.. note:: For AARCH64, Please run the following commands on one of the machines directly. Also, make sure you have the ``AAVMF`` package installed which contains the UEFI firmware to boot the VMs properly.

1. Download the DVD or net install ISO for desired distribution. For this example we are using Debian 10:

.. code-block:: bash

    export DISTRO="debian-12"
    export DISTRO_ISO="debian.iso"

2. Create a 3G qcow2 disk image:

.. code-block:: bash

    qemu-img create -f qcow2 $DISTRO.qcow2 3G

3. Boot up the image using kvm manually:

x86 / POWER:

.. code-block:: console

   $ /usr/libexec/qemu-kvm -m 2048M -boot strict=on -name $DISTRO -machine type=pseries,accel=kvm \
     -cdrom $DISTRO_ISO -netdev user,id=user.0,hostfwd=tcp::2222-:22 \
     -device virtio-net,netdev=user.0 \
     -drive file=$DISTRO.qcow2,if=virtio,cache=writeback,discard=ignore,format=qcow2 \
     -vnc 0.0.0.0:99

AARCH64:

.. code-block:: console

   $ /usr/libexec/qemu-kvm -m 2048M -boot strict=on -name $DISTRO -machine gic-version=3,accel=kvm \
     -cdrom $DISTRO_ISO -netdev user,id=user.0,hostfwd=tcp::2222-:22 \
     -cpu host -monitor none \
     -drive file=$DISTRO.qcow2,if=virtio,cache=writeback,discard=ignore,format=qcow2 \
     -bios /usr/share/AAVMF/AAVMF_CODE.fd
     -vnc 0.0.0.0:99

4. Connect via VNC to the VM and complete the installation:

.. code-block:: console

  $ vncviewer $host:99

5. Wait for the VM to complete the install.

Uploading Images
----------------

.. note::

  We do not recommend uploading images using the GUI interface for any images larger than 1G in size due to limits we
  have set with Apache. Instead we recommend you install using the CLI tools which will communication directly to the
  image service (glance).

1. Install OpenStack CLI packages:

.. code-block:: console

  # Debian/Ubuntu
  $ apt install python3-openstackclient

  # Fedora
  $ dnf install python3-openstackclient

  # MacOS (Brew)
  $ brew install openstackclient

.. note::

  RHEL requires installing the RDO repository to install the ``python3-openstackclient`` package. Run ``dnf search
  openstack``, select the latest release to install and then install the ``python3-openstackclient`` package.

  This can also be installed using ``pip`` by installing the ``openstackclient`` meta package.

2. Download and source openrc file

Login to the OpenStack GUI interface and then on your user on the upper right corner and pressing "OpenStack RC file".
That will download a file which you will then source using your shell environment.

3. Import image into OpenStack:

Due to our backend storage uses Ceph, we recommend to upload images using the raw disk format. This allows for
Copy-on-Write features being used which speeds up VM deployment. If you already have something in qcow2 format, you can
easily convert it by doing the following:

.. code-block:: console

  $ qemu-img convert -O raw -p $DISTRO.qcow2 $DISTRO.raw

Now upload the image:

.. code-block:: console

  $ source openrc
  $ openstack image create \
    --file $DISTRO-compressed.raw \
    --disk-format raw \
    --property hw_scsi_model=virtio-scsi \
    --property hw_disk_bus=scsi \
    --property hw_qemu_guest_agent=yes \
    --property os_require_quiesce=yes \
    $DISTRO

.. note::

  The extra properties are optional but do align best with how our backend systems are configured. It will allow for a
  better user experience if you include those.

However, if you still prefer to use qcow2, make sure you compress it first:

.. code-block:: console

  $ qemu-img convert -O qcow2 -cp $DISTRO.qcow2 $DISTRO-compressed.qcow2
  $ source openrc
  $ openstack image create \
    --file $DISTRO-compressed.qcow2 \
    --disk-format qcow2 \
    --property hw_scsi_model=virtio-scsi \
    --property hw_disk_bus=scsi \
    --property hw_qemu_guest_agent=yes \
    --property os_require_quiesce=yes \
    $DISTRO
