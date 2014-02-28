Connecting to Your Virtual Machines via SSH
===========================================

.. warning::
  This Method is depricated. Please request an OpenVPN account at
  support@osuosl.org if you do not have one

All the virtual machines reside on a private NAT network. In order to connect to
the VMs we have setup an ssh proxy account on a jumphost which you can use to
connect to hosts on the inside. In order to use the proxy with ssh, you will
need to install connect-proxy.

We hope to eventually offer connections via OpenVPN, but for now this offers
users with a simple approach to access.

Installing connect-proxy
------------------------

For Ubuntu or Debian:

::

    apt-get install connect-proxy

For Fedora/RH:

::

    yum install connect-proxy

For OSX: You have two options:

- Download the source code and compile it
- Download a pre-built binary by us. Put this somewhere in your shell $PATH

For Windows:

- Use the standard Cygwin installer (setup.exe) to add the connect-proxy
  package.
- Every other step is the same as on Linux. This cygwin quickstart document
  should help you get started with Cygwin on Windows.

Configuring SSH
---------------

Next, we need to edit your ``~/.ssh/config`` so that connecting works as
expected and easily. Copy the following into your ``~/ssh/config``:

::

    Host *.osuosl.test 10.20.*
    ProxyCommand connect-proxy -R both -5 -S localhost:8080 %h %p

Adding SSH Keys
---------------

Now you need to add your ssh key to Ganeti Web Manager.

- Login into the `Supercell Ganeti Web Manager`_ site.
- Click on your username in the upper right hand corner
- Click on "Add SSH key" and copy/paste your public key

.. _Supercell Ganeti Web Manager: https://ganeti-supercell.osuosl.org

We have a cronjob that runs every five minutes which updates the keys on the
jumphost so you'll need to wait on that.

Create SOCKS Proxy connection
-----------------------------

Now we need to connect to the proxy user and setup a proxy port using the ssh
client. To do that, use the following::

    ssh -N -D 8080 proxy@jumphost.supercell.osuosl.org

If it works, you should see a login banner. You only need one instance of this
ssh connection to connect to multiple hosts. Always remember to start this up
before connecting.

.. note::
  **TODO:** add .ssh/config to simplify this and explain backgrounding the
  connection

Connect to your virtual machine
-------------------------------

Since we have our ssh config in place, all we need to do now is try connecting
to the host like any other host::

    ssh root@myhostname.osuosl.test

If all goes well, it should work! If not check the steps above and ensure you
have a proper ssh key deployed on your VM and in Ganeti Web Manager.

Issues connecting
-----------------

If you're having issues connecting and see an error like this::

    ssh_exchange_identification: Connection closed by remote host

It's likely because you had too many incorrect connection attempts and was added
to the ``/etc/hosts.deny`` file via denyhosts. You will need to either contact
us via IRC in #supercell or send an email to support@osuosl.org to resolve the
issue. Please include your IP address so we can quickly unban you.

