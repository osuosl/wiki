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

Current Images
--------------

We are maintaining PPC64 and PPC64LE images on our FTP mirrors. The list of
operating systems we currently support are:

- Debian 7
- Fedora 20
- Ubuntu 14.04
- Ubuntu 14.04 Little Endian

.. _FTP mirrors: http://ftp.osuosl.org/pub/osl/openpower/openstack/

Guest Installation
------------------

Please run the following commands on one of the OpenPOWER machines directly.

1. Download the DVD or net install ISO for desired distribution.
2. Create a 2G qcow2 disk image::

    export DISTRO="fedora-20"
    export DISTRO_ISO="Fedora-20-ppc64-DVD.iso"
    qemu-img create -f qcow2 $DISTRO.qcow2 2G

3a. Boot up the image using kvm manually (For Big Endian)::

    qemu-system-ppc64 --enable-kvm -M pseries -cpu POWER7+_v2.1 -smp 2 -m 1G \
      -nodefaults -nographic -monitor stdio -serial pty -netdev user,id=user.0 \
      -device virtio-net-pci,netdev=user.0 -cdrom $DISTRO_ISO -drive \
      file=$DISTRO.qcow2,if=virtio -boot order=d

3b. Boot up the image using kvm manually (For Little Endian)::

    qemu-system-ppc64 --enable-kvm -M pseries -cpu POWER7+_v2.1 -smp 2 -m 1G \
      -nodefaults -nographic -monitor stdio -serial pty -netdev user,id=user.0 \
      -device spapr-vlan,netdev=user.0 -cdrom $DISTRO_ISO -device spapr-vscsi \
      -drive file=$DISTRO.qcow2 -boot order=d

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

6c. **Ubuntu:**

   When the yaboot prompt comes up, copy and paste the following in (NOTE: this
   is a short URL to the `github file`__)::

    install-powerpc64 url=http://osl.io/preseedubuntu debian-installer/locale=en_US console-keymaps-at/keymap=us keyboard-configuration/xkb-keymap=us netcfg/get_hostname=unassigned-hostname netcfg/get_domain=unassigned-domain

6d. **Ubuntu 14.04 (Little Endian):**

   When the grub menu comes up, press ``e`` to edit. Find the line that starts
   with::

    linux        /install/vmlinux

   And then add the following to the end (NOTE: this is just a short URL to the
   `github file`__) ::

    url=http://osl.io/preseedubuntule debian-installer/locale=en_US console-keymaps-at/keymap=us keyboard-configuration/xkb-keymap=us netcfg/get_hostname=unassigned-hostname netcfg/get_domain=unassigned-domain

.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/http/ks-fedora-qemu-20-ppc64.cfg
.. __: http://ftp.osuosl.org/pub/osl/packer-templates/http/preseed-debian-ppc64.cfg
.. __: http://ftp.osuosl.org/pub/osl/packer-templates/http/preseed-ubuntu-ppc64.cfg
.. __: http://ftp.osuosl.org/pub/osl/packer-templates/http/preseed-ubuntu-ppc64le.cfg

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

10c. **Ubuntu:**

    Run the following command (NOTE: this is just a short URL to the `github
    file`__)::

      wget -O - http://osl.io/postinstubuntu | bash

.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/openpower/postinstall-openstack-yum.sh
.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/openpower/postinstall-openstack-debian.sh
.. __: https://raw.githubusercontent.com/osuosl/packer-templates/master/openpower/postinstall-openstack-ubuntu.sh

11. Compress and import image into Openstack::

      qemu-img convert -O qcow2 -c $DISTRO.qcow2 $DISTRO-compressed.qcow2
      source keystonerc_admin
      glance image-create --name $DISTRO --disk-format=qcow2 \
        --container-format=bare < $DISTRO-compressed.qcow2
