.. _vpn-config:

OpenVPN Client Settings
=======================

.. contents::

Supported Client Platforms
--------------------------

.. note::

  As of December 2022 our current VPN server is still running on a legacy system and has difficulty working on newer
  platforms. We are in the process of getting this service migrated to a newer system by sometime in 2023.

  We understand the security implications of continuing to run a legacy server such as this and are working as
  diligently as we can to have this service upgraded ASAP.

The following platforms have been tested to work with our server:

- RHEL 7 & 8
- Debian 10, 11
- Ubuntu 18.04, 20.04
- Mac OS

The following platforms are unsupported per the note above (basically, anything that uses OpenSSL 3):

- RHEL 9
- Fedora
- Ubuntu 22.04

What you need
-------------

- OpenVPN
- client certificate  **<username>.crt**
- client private key: **<username>.key**
- server certificate: :download:`ca.crt </_static/files/ca.crt>`

Settings
--------

- server: **vpn.osuosl.org:1194**
- type: **Certificate (TLS)**
- protocol: **UDP**
- device type: **TUN**

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
- Copy your key, certificate, and server certificate to ``~/.openvpn`` and then run ``chmod 600 ~/.openvpn*``
- Open Network Manager
- Add VPN -> OpenVPN:

  - Identity

    - Name:  **OSUOSL VPN**
    - Gateway: **vpn.osuosl.org**
    - Type: **Certificates (TLS)**
    - User Certificate: **<username>.crt**
    - CA Certificate:  **ca.crt**
    - Private Key: **<username>.key**
    - Advanced:

      - General -> Set virtual device type: **TUN**
      - Security ->  Cipher: **BF-CBC**
      - TLS Authentication -> TLS min version: **1.0**
  - IPv4

    - Routes -> Use this connection only for resources on its network: **✔** (if unchecked, all network traffic is
      routed through the VPN)
  - IPv6

    - IPv6 Method -> Disable: **✔**
- Add
- Click on the Network Manager status bar icon and select **VPN Off -> Connect**
- Wait until connection is established
- Check connection:

  - ``ip a`` -- An IP address should be in the ``10.*.*.*`` range via a ``tun0`` interface.
  - ``ping -c 1 10.0.0.1`` -- You should be able to ping this IP address

Trouble shooting
~~~~~~~~~~~~~~~~

Shotgun style - try again, reboot, disable network devices, do the chicken dance. If all else fails, try the command
line version. If that works, try this again, maybe it just didn't like you the first time.

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
- Copy your key, certificate, and server certificate to ``/etc/openvpn/client/`` and then run ``chmod 600
  /etc/openvpn/client/*``
- Download the following config file and update the key names to match what you have:

  - Ubuntu :download:`osuosl.conf </_static/files/osuosl-ubuntu.conf>`
  - Debian :download:`osuosl.conf </_static/files/osuosl-debian.conf>`
  - RHEL :download:`osuosl.conf </_static/files/osuosl-rhel.conf>`

.. code-block::

  wget -O /etc/openvpn/client/osuosl.conf # <url from above>

- Enable and start the OpenVPN client service:

.. code-block:: bash

  systemctl enable openvpn-client@osuosl.service
  systemctl start openvpn-client@osuosl.service

- Check connection:

  - ``ip a`` -- An IP address should be in the ``10.*.*.*`` range via a ``tun0`` interface.
  - ``ping -c 1 10.0.0.1`` -- You should be able to ping this IP address

Troubleshooting
~~~~~~~~~~~~~~~

Check the log out from the service by doing the following:

.. code-block:: bash

  journalctl -u openvpn-client@osuosl.service

Tunnelblick (OS X)
------------------

Tunnelblick is a free, open source gui for OpenVPN on OS X that allows for easy control of the OpenVPN client.

Troubleshooting
~~~~~~~~~~~~~~~

The version of OpenVPN we are running is incompatible with OpenVPN client v2.4+ on OS X.  If you are running OS X,
please use OpenVPN v2.3 to connect to the VPN.

Disabling LZO compression may help on older OpenVPN instances.

In addition, the version of OpenVPN we are running is incompatible with TLSv1.2, so if you are running into issues
(such as on Debian 10), please do the following in ``/etc/ssl/openssl.cnf``::

  #MinProtocol = TLSv1.2
  MinProtocol = TLSv1

We plan to resolve this issue soon.

Installation
~~~~~~~~~~~~
Download and install Tunnelblick from the project's downloads_ page.

Alternatively install the package using the Homebrew:

.. code-block:: bash

    brew cask install tunnelblick

Configuration
~~~~~~~~~~~~~
#.  Download this :download:`Tunnelblick profile</_static/files/osuosl.tblk.zip>`.

#.  Replace the contents of ``osuosl.tblk/USER.crt`` and ``osuosl.tblk/USER.key`` with your personal ``crt`` and
    ``key``.

#.  Double click the ``osuosl.tblk`` file to install the profile in Tunnelblick.

#.  Connect to the ``osuosl`` profile in Tunnelblick.

.. note::

    You may need to check ``Tunnel all IPv4`` under the advanced settings for
    the ``osuosl`` profile.

.. _downloads: https://tunnelblick.net/downloads.html
