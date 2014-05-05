.. _openpower-openstack-guests:

Openstack OpenPOWER Guests
==========================

This documentation covers the steps needed to build an Openstack guests on
OpenPOWER KVM.

Unfortunately we can't use `packer`_ yet for building images so for now we'll need
to build them manually on the OpenPOWER boxes. For now we should **only** be
building images on the hardware itself and not use QEMU emulation on x86. While
it may work, we have this method as a confirmed way to build the images.

.. _packer: http://www.packer.io/

.. note::

    All guests will have their output directed to the serial console by default.

Guest Installation
------------------

This method should work for other distributions (in theory) but for now Fedora
and Debian is only supported currently. Please run the following commands on one
of the OpenPOWER machines directly.

1. Download the DVD or net install ISO for desired distribution.
2. Create a 2G qcow2 disk image::

    qemu-img create -f qcow2 fedora-20.qcow2 2G

3. Boot up the image using kvm manually::

    qemu-system-ppc64 --enable-kvm -M pseries -cpu POWER7+_v2.1 -smp 2 -m 1G \
      -nodefaults -nographic -monitor stdio -serial pty -netdev user,id=user.0 \
      -device virtio-net-pci,netdev=user.0 -cdrom Fedora-20-ppc64-DVD.iso \
      -drive file=fedora-20.qcow2,if=virtio -boot order=d

4. Note the serial device qemu created::

    (qemu) char device redirected to /dev/pts/2 (label serial0)

5. Quickly connect to the serial console using ``socat``. To escape, use
   ``ctrl+]``::

    socat STDIO,raw,echo=0,escape=0x1d /dev/pts/2

6a. **Fedora:**

   When the grub menu comes up, press ``e`` to edit. Find the line that says::

    linux /ppc/ppc${2}/vmlinuz  ro

   And then add the following to the end (NOTE: this is just a short URL to the
   `github file`__) ::

    ks=http://osl.io/ksfedora20

6b. **Debian:**

   When the yaboot prompt comes up, copy and paste the following in (NOTE: this
   is a short URL to the `github file`__)::

    install url=http://osl.io/preseeddebian debian-installer/locale=en_US console-keymaps-at/keymap=us keyboard-configuration/xkb-keymap=us netcfg/get_hostname=unassigned-hostname netcfg/get_domain=unassigned-domain

.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/http/ks-fedora-qemu-20-ppc64.cfg
.. __: http://ftp.osuosl.org/pub/osl/packer-templates/http/preseed-debian-ppc64.cfg

7. Wait for the VM to complete the install automatically and shutdown.
8. Boot the image up using the newly installed system. Change ``-boot order=d``
   to ``-boot order=c`` for the kvm command. Quickly connect to the serial
   console.
9. Login as root (password is ``osuadmin``).

10a. **Fedora:**

    Run the following command (NOTE: this is just a short URL to the `github
    file`__)::

      wget -O - http://osl.io/postinstyum | bash

10b. **Debian:**

    Run the following command (NOTE: this is just a short URL to the `github
    file`__)::

      wget -O - http://osl.io/postinstdebian | bash

.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/openpower/postinstall-openstack-yum.sh
.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/openpower/postinstall-openstack-debian.sh

11. Compress and import image into Openstack::

      qemu-img convert -O qcow2 -c fedora-20.qcow2 fedora-20-compressed.qcow2
      source keystonerc_admin
      glance image-create --name fedora20 --disk-format=qcow2 \
        --container-format=bare < fedora-20-compressed.qcow2

Known Issues
------------

Fedora
~~~~~~

cloud-init dmidecode dependency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently cloud-init depends on dmidecode which is an x86 specific package and
not included in ppc64. There's an open bug (`#1025071`_) that can be used to
track the progress of the upstream fix.

As a workaround, we have rebuilt the latest version of the package and edited
the spec file to just comment out the dmidecode dependency. Thus far this seems
to be the best short-term solution.

.. _#1025071: https://bugzilla.redhat.com/show_bug.cgi?id=1025071
