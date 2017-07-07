Packages Required for Different OS Families
===========================================

Each Operating System interacts with the volumes attached to it in various ways.
The most common ways to interact with volumes are through packaged programs such
as ``fdisk``, ``mount``/``umount``, and other LVM commands. Alongside these packages,
there are other packages that are necessary to view and allow the system to properly
interact with the volumes that the user is attempting to manipulate.

Volumes on ppc64
--------------------

One of the most crucial packages for proper POWER volume management is ``ppc64-diag``.

The following is a table showing which images on openpower-controller.osuosl.org have
this package pre-installed:

.. csv-table:: Pre-Installed Images
  :header: "OS", "``ppc64-diag``"
  :widths: 12, 15

  "Debian", "no"
  "CentOS", "yes"
  "Ubuntu", "no"
  "Fedora", "yes"
  "OpenSUSE", "no"
    
For some distributions, ``ppc64-diag`` is not available in the stable repository. In example:
for Debian, ``ppc64-diag`` only exists in the *"stretch"* packages, and for OpenSUSE,
``ppc64-diag`` is only available in the *"Tumbleweed"* packages. So if you are running an
older version of Debian or OpenSUSE such as *"jessie"* or *"Leap"*, you will need to install
``ppc64-diag`` from another, potentially unstable version.
