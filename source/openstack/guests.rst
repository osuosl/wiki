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
   :widths: 40, 15, 15, 15, 15, 15
   :header-rows: 1

.. note:: We currently maintain only ppc64le little-endian (LE) images for POWER8/9/10. IBM is focusing on LE, so we
   provide limited support for a big-endian (BE) Debian Sid (unstable) image because other distributions have dropped
   BE.

.. note:: Windows images ship with an evaluation license only; you are responsible for obtaining valid licensing before
   production use.

If there are any other images you would like us to create, please let us know.

User-provided images
--------------------

If you want to upload an operating system we do not maintain, make sure the image meets these requirements:

- Install ``cloud-init`` and enable it to start on first boot so networking, SSH keys, and metadata are applied.
- Install and enable ``qemu-guest-agent`` to support clean shutdowns and IP reporting when the image property
  ``hw_qemu_guest_agent`` is set.
- Include virtio storage and network drivers and ensure the root disk can boot with ``virtio-scsi``, matching the
  ``hw_scsi_model``/``hw_disk_bus`` properties used here.
- Leave cloud-init datasources for EC2/ConfigDrive enabled and do not block 169.254.169.254 so metadata can reach the
  guest.
- Enable disk resize on first boot (cloud-init growpart/resizefs, GPT preferred, ``cloud-guest-utils`` or equivalent
  installed).
- Provide an SSH-able default user for key injection and avoid shipping hardcoded passwords; disable password auth if
  possible.

Building images with packer
---------------------------

We build all of our images using `packer`_ via our `packer-templates`_ github repo.

.. _packer: http://www.packer.io/
.. _packer-templates: https://github.com/osuosl/packer-templates

Manual Guest Installation
-------------------------

.. note:: This is only useful for manually testing some images and is no longer used for building images.

.. note:: For AARCH64, please run the following commands on one of the machines directly. Make sure you have the
  ``AAVMF`` package installed; it contains the UEFI firmware required to boot the VMs.

1. Download the DVD or net install ISO for your desired distribution. For this example we are using Debian 12:

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
     -bios /usr/share/AAVMF/AAVMF_CODE.fd \
     -vnc 0.0.0.0:99

4. Connect via VNC to the VM and complete the installation:

.. code-block:: console

  $ vncviewer $host:99

5. Wait for the VM to complete the install.

Uploading Images
----------------

.. note::

  We do not recommend uploading images using the web UI for any images larger than 1G because of Apache limits. Instead
  we recommend using the CLI tools, which communicate directly with the image service (glance).

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

Log in to the OpenStack web UI, click your username in the upper right, choose "OpenStack RC file" to download it, and
source it in your shell.

3. Import image into OpenStack:

Because our backend storage uses Ceph, we recommend uploading images in the raw disk format. This enables
copy-on-write features that speed up VM deployment. If you already have a qcow2 image, convert it with:

.. code-block:: console

  $ qemu-img convert -O raw -p $DISTRO.qcow2 $DISTRO.raw

Now upload the image:

.. code-block:: console

  $ source openrc
  $ openstack image create \
    --file $DISTRO.raw \
    --disk-format raw \
    --property hw_scsi_model=virtio-scsi \
    --property hw_disk_bus=scsi \
    --property hw_qemu_guest_agent=yes \
    --property os_require_quiesce=yes \
    $DISTRO

.. note::

  These properties are optional but match our backend defaults and usually deliver a better user experience.

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
