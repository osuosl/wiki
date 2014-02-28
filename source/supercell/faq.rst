FAQ
===

Some common questions/answers about Supercell and Ganeti Web Manager:

Can I store data long-term on Supercell?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Storing important data on Supercell is probably not a good idea. Data on
Supercell is not replicated or backed-up anywhere, so there is a chance you
could lose it should something happen to the cluster.

Is there central storage that I could access from multiple VMs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have an NFS node in place which will be able to provide centralized storage
for Supercell, however we don't yet have it setup in an automated way. If you
really need storage before we are able to add this functionality, please
contact us in #supercell on freenode to discuss.

How can I access a web application hosted on my Supercell VM?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the documentation on Connecting to your VMs via SSH. Once you ssh to
the jumphost, you will be able to setup a proxy in your browser pointing to
localhost:8080 which will get forwarded to the Supercell cluster. Use your VM's
IP address to bring it up in your browser. We have plans to implement a VPN, but
this is not yet complete.
