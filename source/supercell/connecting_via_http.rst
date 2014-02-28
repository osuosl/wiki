Connecting to a VM via HTTP
===========================

We are working on setting up a VPN which would simplify this process, but for
now if you want to connect to HTTP services on your Supercell VM, you will need
to connect using an ssh proxy. Before following the directions below, be sure
you have ssh setup properly - see Connecting via SSH for more info.

Once you have connected to the Supercell jumphost
(jumphost.supercell.osuosl.org) using SSH, you will be able to setup a SOCKS
proxy in your browser connected to localhost port 8080. This is the '-D 8080'
portion of the ssh command given on the Connecting via SSH documentation.

Firefox
-------

In Firefox, this is done under Preferences -> Advanced -> Network -> Settings.
Once in that settings window, select 'Manual Proxy Configuration', and then
under 'Socks Host', enter 127.0.0.1, port 8080, then select Socks v5 and click
OK. This will allow you to connect to a website on your VM by entering the IP
address into your browser (of the form 10.20.x.x). If you want to use the local
DNS name (``*.osuosl.test``), there is a setting in about:config which will
forward DNS requests through the SOCKS proxy. To enable this, go to
'about:config', and then change the setting network.proxy.socks_remote_dns to
true.

Chromium
--------

In Chromium, go to Preferences -> Under The Hood -> Network -> Change Proxy
Settings. Note that Chromium will update your system proxy settings and not just
internal Chromium settings. Set the Socks Host to 127.0.0.1, port 8080. Chromium
will automatically use the socks proxy for DNS, so you should now be able to
connect to your VM using either the DNS name (``*.osuosl.test``), or via the IP
address (10.20.x.x). Note that now all your browsing traffic is going through
the jumphost, so please disable this proxy setting once you are done connecting
to your VM.
