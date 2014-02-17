
.. _source/public/ganeti/iso_os_install#installing_an_os_with_an_iso_using_ganeti:

Installing an OS with an ISO using Ganeti
=========================================

Here's a quick guide on how to do a manual OS install using an ISO image.

This is a work in progress...

.. _source/public/ganeti/iso_os_install#disable_kvm_clock:

Disable kvm_clock
-----------------

There's currently a bug in KVM to where migrations lock up the guest if it is using the kvm_clock. To work around this issue, you need to tell the kernel to use a different clock at boot time. You can also change this at runtime but this will ensure its a permanent change.

.. _source/public/ganeti/iso_os_install#debian:

Debian
~~~~~~

On debian, open up /boot/grub/menu.lst and edit the following line while the guest is running.

::

    kargs root=/dev/vda2 ro clocksource=tsc

Now update the grub config by running ``update-grub``.