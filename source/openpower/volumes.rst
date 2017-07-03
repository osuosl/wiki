Packages Required for Different OS Families
===========================================

Each Operating System interacts with the volumes attached to it in various ways.
The most common ways to interact with volumes are through packaged programs such
as ``fdisk``, ``mount``/``umount``, and other LVM commands. Alongside these packages,
there are other packages that are necessary to view and allow the system to properly
interact with the volumes that the user is attempting to manipulate.

One of the most crucial packages for proper POWER volume management is ``ppc64-diag``.

The following is a table showing which images on openpower-controller.osuosl.org have
this package pre-installed:

.. csv-table::
  :header: "OS", "``ppc64-diag``"
  :widths: 12, 4

  "Debian", "no"
  "CentOS", "yes"
  "Fedora", "no"
  "Ubuntu", "no"
  "OpenSUSE", "no"
