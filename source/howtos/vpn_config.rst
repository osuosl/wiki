OpenVPN Client Settings
=======================

What you need:
--------------

- OpenVPN
- client certificate  **<username>.crt**
- client private key: **<username>.key**
- server certificate: **ca.crt**


Settings:
---------

- server: **vpn.osuosl.org:1194**
- type: **Certificate (TLS)**
- protocol: **UDP**
- compression: **None** (Note this changed on 08/18/10 - previously LZO was used)
- device type: **TUN**


Network Manager (Linux)
-----------------------

Packages:
~~~~~~~~~

- Debian/Ubuntu: **sudo aptitude install openvpn network-manager-openvpn**

Procedure:
~~~~~~~~~~
- Copy your key, certificate, and server certificate to a secure location of
  your choice such as ~/openvpn/.  Set paranoid permissions (-r-x------ or
  similar).
- Install Network Manager (installed by default in many Linux distributions)
- Install the Network Manager OpenVPN package
- Open Network Manager
- Add a new VPN connection:

  - Connection name:  **<witty name>** 
  - Gateway: **vpn.osuosl.org**
  - Type: **Certificates (TLS)**
  - User Certificate: **<username>.crt**
  - CA Certificate:  **ca.crt**
  - Private Key: **<username>.key**
  - Private Key Password: **<password>** (if applicable)
  - Advanced->Make sure 'Use LZO data compression' is **unchecked**
  - IPv4 Settings->Routes...->Use this connection only for resources on its
    network: **✔** (if unchecked, all network traffic is routed through the VPN)
- Apply
- Click on the Network Manager status bar icon and select **VPN
  Connections-><witty name>**
- Wait until connection is established
- Check connection:

  - **ifconfig -a**: IP address should be in the 10.2.*.* range.
  - **ping 10.2.0.1**: The router should respond


Trouble shooting
~~~~~~~~~~~~~~~~

Shotgun style - try again, reboot, disable network devices, do the chicken
dance. If all else fails, try the command line version. If that works, try this
again, maybe it just didn't like you the first time.

OpenVPN command-line client
---------------------------

Packages:
~~~~~~~~~

- Debian/Ubuntu: **sudo aptitude install openvpn**
- Gentoo: **sudo emerge openvpn**.  For detailed instructions, including kernel
  configuration see http://en.gentoo-wiki.com/wiki/OpenVPN.

Procedure:
~~~~~~~~~~

- Copy your key, certificate, and server certificate to a secure location of
  your choice such as /etc/openvpn/.  Set paranoid permissions (-r-x------ or
  similar).
- Create a configuration file in a location of your choice such as
  /etc/openvpn/openvpn.conf.  Here is an example configuration file:

.. code-block:: bash

    client                         # Client mode
    dev tun                        # Create a TUN device (not TAP)
    proto udp                      # Use UDP (not TCP)
    #comp-lzo                      # Don't enable LZO compression

    remote vpn.osuosl.org 1194  # Server settings
    remote-cert-tls server         # Use TLS to check server identity

    ca /etc/openvpn/ca.crt                      # Server certificate
    cert /etc/openvpn/<username>.crt            # Client certificate
    key /etc/openvpn/<username>.key             # Client private key

    resolv-retry infinite          # Never give up trying to connect to the
                                   # server (useful for unreliable internet
                                   # connections and laptops)
    nobind                         # Don't bind a local port

    # Drop privileges after initialization (not applicable to Windows)
    user nobody
    group nobody

    # Preserve state across restarts.
    persist-key
    persist-tun

    mute-replay-warnings           # Do not complain about duplicate packets
                                   # (common on wireless networks)

    # Verify server certificate by checking that the certicate has the
    # nsCertType field set to 'server'. See:
    # http://openvpn.net/index.php/open-source/documentation/howto.html#mitm 
    ns-cert-type server

    verb 4                         # Set log file verbosity
    script-security 3 system       # Enable dns-pushing

    # For Ubuntu:
    up /etc/openvpn/update-resolv-conf
    down /etc/openvpn/update-resolv-conf

    # For Gentoo: 
    up /etc/openvpn/up.sh
    down /etc/openvpn/down.sh

    # For Fedora:
    up /usr/share/doc/openvpn-2.1.1/contrib/pull-resolv-conf/client.up
    down /usr/share/doc/openvpn-2.1.1/contrib/pull-resolv-conf/client.down

- Run OpenVPN: **openvpn /etc/openvpn/openvpn.conf**
- Check connection:

  - **ifconfig -a**: IP address should be in the 10.*.*.* range.
  - **ping 10.0.0.1**: The router should respond
