.. _vpn-config:

OpenVPN Client Settings
=======================

.. contents::

Supported Client Platforms
--------------------------

The following platforms have been tested to work with our server:

- RHEL 7, 8, 9
- Debian 10, 11, 12
- Ubuntu 18.04, 20.04, 22.04
- Mac OS
- Fedora
- Windows 10, 11

What you need
-------------

- OpenVPN
- OVPN config file containing our default config and all certificates

CA Certificate
--------------

We renewed our CA certificate in September 2021. You can download it here: :download:`ca.crt </_static/files/ca.crt>`

Settings
--------

In general, the OVPN file we provide you should have all of the information you need to connect, however below are the
basic settings you have:

- server: **vpn.osuosl.org**
- type: **Certificate (TLS)**
- Advanced:

  - General -> Set virtual device type: **TUN**
  - Security ->  Cipher: **AES-256-GCM**
  - TLS Authentication -> Verify peer (server) certificate usage signature: **✓**

Network Manager (Linux)
-----------------------

Packages
~~~~~~~~

.. code-block:: bash

  # Debian/Ubuntu:
  $ apt install network-manager-openvpn-gnome

  # RHEL
  $ yum install epel-release
  $ yum install NetworkManager-openvpn-gnome

Procedure
~~~~~~~~~
- Install the packages mentioned above
- Open Network Manager
- Click the **+** to create a new VPN connection
- Click on **Import from file..**
- Use the ``.ovpn`` file we gave you
- There are some additional settings we recommend you change that we're not able to do via the ``.ovpn`` file.

  - IPv4 -> DNS: **140.211.166.130, 140.211.166.131**
  - IPv4 -> and select: **Use this connection only for resources on its network**
  - IPv6 -> IPv6 Method: **Disable**
- Click on the Network Manager status bar icon and select: **VPN Off -> Connect**
- Wait until connection is established
- Check connection:

  - ``ip a`` -- An IP address should be in the ``10.2.*.*`` range via a ``tun0`` interface.
  - ``ping -c 1 10.0.0.1`` -- You should be able to ping this IP address

Trouble shooting
~~~~~~~~~~~~~~~~

Check the system logs by doing the following:

.. code-block:: console

  journalctl -t nm-openvpn

Systemd service (Linux)
-----------------------

Packages
~~~~~~~~

.. code-block:: bash

  # Debian/Ubuntu:
  $ apt update
  $ apt install openvpn resolvconf-admin

  # RHEL
  $ yum install epel-release
  $ yum install openvpn


Procedure
~~~~~~~~~

- Install the packages mentioned above
- Copy the ``.ovpn`` file we gave you as ``/etc/openvpn/client/osuosl.conf``

.. note::

  For Debian/Ubuntu users: You will need to change the ``group`` from ``nobody`` to ``nogroup``

- Change permissions: ``chmod 0600 /etc/openvpn/client/osuosl.conf``
- Enable and start the OpenVPN client service:

.. code-block:: bash

  systemctl enable openvpn-client@osuosl.service
  systemctl start openvpn-client@osuosl.service

- Check connection:

  - ``ip a`` -- An IP address should be in the ``10.*.*.*`` range via a ``tun0`` interface.
  - ``ping -c 1 10.0.0.1`` -- You should be able to ping this IP address

Troubleshooting
~~~~~~~~~~~~~~~

Check the system logs from the service by doing the following:

.. code-block:: bash

  journalctl -u openvpn-client@osuosl.service

Unable to connect
-----------------

Our certificates were originally signed using the sha1 algorithm which is no longer supported on newer operating
systems (Fedora, RHEL >= 9, Ubuntu >= 22.04, etc). To fix this, we need to renew your certificate which will be signed
using sha256.

Please send an email to support@osuosl.org with the subject line: ``OpenVPN Certificate renewal: <Name>``. We will send
you an updated certificate which should fix the issue.

Tunnelblick (OS X)
------------------

Tunnelblick is a free, open source gui for OpenVPN on OS X that allows for easy control of the OpenVPN client.

Installation
~~~~~~~~~~~~
Download and install Tunnelblick from the project's downloads_ page.

Alternatively install the package using the Homebrew:

.. code-block:: bash

    brew cask install tunnelblick

Configuration
~~~~~~~~~~~~~
Tunnelblick uses a ``.ovpn`` file with your certificate and key to install a profile. If you would like to set up
OpenVPN using Tunnelblick, please send an email to support@osuosl.org with the subject line:
``OpenVPN .ovpn file: <Name>``. We will send you the file that you can easily use:
 
#.  Double click  the ``USER.ovpn`` file we provided to install the profile in Tunnelblick.

#.  Open Tunnelblick and connect to the ``USER`` profile.

.. note::

    You may need to check ``Tunnel all IPv4`` under the advanced settings for the ``USER`` profile.

.. _downloads: https://tunnelblick.net/downloads.html

OpenVPN (Windows)
------------------

OpenVPN community edition for windows uses the ``.ovpn`` file we provided.

#. Download window openvpn client from openvpn_community_downloads_ page. and install. Versions 2.5 and higher should work fine. Earlier versions may also work.
#. Create a folder in C:\\Program Files\\OpenVPN\\config called **osuosl** and copy the .ovpn, .crt, and .key files provided into the folder
#. Edit the .ovpn file sections ca, cert, key 
   Should have full path e.g. replacing **yourname** with the filename part of your crt and key files

.. code-block::

 ca "C:\\Program Files\\OpenVPN\\config\\osuosl\\ca.crt"      # Server certificate
 cert "C:\\Program Files\\OpenVPN\\config\\osuosl\\yourname.crt"  # Client certificate
 key "C:\\Program Files\\OpenVPN\\config\\osuosl\\yourname.key"   # Client private key

Once done with configs launch the C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe, this should create an icon on your task bar you can right click and see OSUOSL option for connection

.. _openvpn_community_downloads: https://openvpn.net/community-downloads/
