Interacting with Volumes on OpenPOWER
=====================================

Each Operating System interacts with the volumes attached to it in various ways.  The most common ways to interact with
volumes are through packaged programs such as ``fdisk``, ``mount``/``umount``, and other LVM commands. Alongside these
packages, there are other packages that are necessary to view and allow the system to properly interact with the
volumes that the user is attempting to manipulate.

Volumes on ppc64 and ppc64le
----------------------------

One of the most crucial packages for actually being able to use volumes on POWER platform is ``ppc64-diag``. This
package is needed in order to properly add/remove volumes live on the VMs. For all images we've created and managed,
we've ensured this package is installed. However, if you use your own image, you will need to make sure this package is
installed.
