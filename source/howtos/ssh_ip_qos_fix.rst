Fixing Slow SSH Speeds With IPQoS
=================================

Why?
----

The Differentiated Services Code Point (DSCP_) field in an IP header is for classifying network data and providing
Quality of Service (QoS). `The default SSH DSCP setting for non-interactive sessions`__ is ``CS1``. Within the OSL
network, ``CS1`` packets might be dropped very frequently, thus resulting in poor performance when SCPing.

How?
----

The poor performance when using SCP or rsync over secure shell can be remedied by adding ``-o IPQoS=throughput`` to your
scp or rsync command. Another more permanent fix would be to add this to your ssh config::

    Host *
      IPQoS=throughput

.. _DSCP: https://en.wikipedia.org/wiki/Differentiated_services
.. __:    https://man7.org/linux/man-pages/man5/ssh_config.5.html
