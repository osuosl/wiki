.. _keys:

SSH Key Behavior and Management on OpenPOWER
============================================

These are findings of how SSH Keys behave in various conditions on OSL's POWERDev OpenStack cluster,
and how to manage these keys.

.. note::

  For beginners: a good tutorial on SSH keys and SSH in general `here`__.

  And a quicker, more advanced and jargon-full tutorial `here`__.

  *Probably best to read both, even if you're advanced. There are some extremely helpful tips and tricks in both of these.*

.. __: https://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch01_01.htm

.. __: https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process

Accessing an Instance Using an SSH Key
--------------------------------------

On a simple level, instances can be accessed using ``ssh``::

  $ ssh <image_name>@<instance_IP_address>

*Example:* ``$ ssh ubuntu@140.211.123.456``

.. note::

  .. csv-table:: Login Names
    :header: "OS", "Username"
    :widths: 12, 15

    "Debian", "``debian``"
    "CentOS", "``centos``"
    "Ubuntu", "``ubuntu``"
    "Fedora", "``fedora``"
    "OpenSUSE", "``opensuse``"

Doing so will prompt the server and client to establish a secure connection, then the server authenticates
the requesting client. If you have the correct credentials (the desired SSH private key), then you will be
granted access to the server.

.. note::

  This description is very brief and not detailed enough to fully explain how SSH keys and the Diffie-Hellman exchange works.
  A more descriptive overview is linked in the section `above.`__

.. __: keys.html#ssh-key-behavior-and-management-on-openpower

*However*, a common issue occurs **after rebuilding an instance**, regarding your local ``known_hosts`` file,
which stores a list of IP addresses and their corresponding DSA, RSA, or ECDSA host keys.

If you are recieving something similar to the error::

  ECDSA host key for 140.211.123.456 has changed and you have requested strict checking.
  Host key verification failed.

then a simple command should fix the error::

  $ ssh-keygen -f "<path/to>/.ssh/known_hosts" -R <instance_IP_address>

*Example:* ``$ ssh-keygen -f "/home/scobeavs/.ssh/known_hosts" -R 140.211.123.456``

This issue occurs because the client (the machine you're attempting to log on to the server through),
is also attempting to authenticate the server, to keep the user (you) from connecting to a potentially
dangerous imposter. This command removes the server from your ``known_hosts`` file,
allowing you to connect to the server as if it were brand new to you.

Changing a Key From Inside an Instance
--------------------------------------

To create an OpenPOWER OpenStack instance, we must first set up a Key Pair to associate with that machine.

.. note::

  For the purposes of this documentation, this key pair will be known as the **Original Key Pair**.

To allow for multiple SSH Keys to access this instance:
  We need to add the contents of ``<our_key>.pub`` to ``~/.ssh/authorized_keys`` from the machine
  with the corresponding keyfile.

  To do so, we need to be certain we can ``ssh`` into our instance with::

      $ ssh <image_name>@<instance_IP_address>

  After we have tested that, we can ``Ctrl+D`` or ``logout`` out of the instance, and use ``ssh-copy-id``
  to transfer ``<our_key>.pub`` to ``authorized_keys``, allowing multiple key pairs.

  - To **add** a key pair, retaining the original(s)::

      $ ssh-copy-id <path/to/our_key>.pub <image_name>@<instance_IP_address>

    *Example:* ``$ ssh-copy-id ~/.ssh/id_rsa.pub ubuntu@140.311.133.05``

  - To **change** the key pair, removing all others::

      $ cat <path/to/our_key>.pub | ssh <image_name>@<instance_IP_address> "mkdir -p ~/.ssh && cat > ~/.ssh/authorized_keys"

    *Example:* ``$ cat ~/.ssh/id_rsa.pub | ssh debian@140.244.313.10 "mkdir...``

Changing a Key From OpenStack Web GUI
-------------------------------------

There is currently no known way to edit the **Original Key Pair** designated to the instance.

Once an instance is created, the original keypair with the original
name and fingerprint will always be attached to that machine.

The instance will *still* not change even if an administrator deletes the **Original Key Pair** and creates a
new key pair with the same name as the **Original**, and rebuilds the machine.

Our best guess to the reason why is because when the instance is created, the **Original Key Pair** and its
fingerprint are entered into the ``nova`` database, and there remain, uneditable, until its destruction.

Note that we can use this knowledge to our advantage, however, as there is a fail-proof way to return the
``authorized_keys`` file to its original state by simply rebuilding the instance.

Accessing an Instance After a Rebuild
-------------------------------------

As explained above, using SSH Key Pairs to access an instance after a rebuild will *only* work with the
**Original Key Pair**. This remains true through operating systems. *However*, an error may occur like
the one noted in `the first section`__. To rid of this error, follow the steps given there.

.. __: keys.html#accessing-an-instance-using-an-ssh-key

So... What do you do if you lost the original key?

Accessing an Instance After a Rebuild ... *Without the Original Key*
--------------------------------------------------------------------

As of right now, there is no simple way to fix this issue. Send in a support ticket request here to have the OSU Open Source Lab work with you to remedy this issue.

support@osuosl.org
