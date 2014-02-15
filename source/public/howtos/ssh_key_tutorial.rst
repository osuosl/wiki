
.. _generating_an_ssh_key_pair:

Generating an SSH Key Pair
==========================

Why?
----
SSH keys have numerous advantages over passwords
  - Increased security: they are nearly impossible to brute force or guess
  - Ease of management: Need access to a friend's computer? Just send them your public key. No more creating and changing random passwords.
  - Type less passwords: You can use ssh-agent to cache your key, so you can use ssh without typing your password every time
  - Automated scripts: Because you don't need to type your password every time, its easier to automate tasks that require ssh

How?
----

Linux/OS X (Short Version)
~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Run this command: 
::

    ssh-keygen -t rsa 

  - Accept the default location, and enter a secure passphrase that you (and only you) will remember.
  - Email us the contents of ~/.ssh/id_rsa.pub

Linux/OS X (Detailed)
~~~~~~~~~~~~~~~~~~~~~
  - Use the ``ssh-keygen`` utility to create your key. For a 2048 bit RSA key do:
::

    $ ssh-keygen -t rsa
For increased security you can make an even larger key with the -b option. For example, for 4096 bits do:
::

    $ ssh-keygen -t rsa -b 4096
The OSL recommends using RSA over DSA because DSA keys are required to be only 1024 bits.
  - When prompted, you can press Enter to use the default location (/home/your_username/.ssh/id_rsa on Linux, or /Users/your_username/.ssh/id_rsa on Mac) if you don't already have a key installed, or specify a custom location if you are creating a second key (or just want to for whatever reason).
  - Enter a passphrase at the prompt.**All people connecting to OSL servers must use a passphrase**. This is just a password used to unlock your key. If someone else gets a copy of your private key they will be able to log in as you on any account that uses that key, unless you specify a passphrase. If you specify a passphrase they would need to know both your private key **and** your passphrase to log in as you.
  - After you re-enter your passphrase, ssh-keygen may print a little picture representing your key ((you don't need to worry about this now, but it is meant as an easily recognizeable fingerprint of your key, so you could know if it is changed without your knowledge - but it doesn't seem to be widely used)) then exit.
  - Your private key should now be in the location you specified, and your public key will be at that same location but with '.pub' tacked onto the filename. 
  - If you are creating this key for use with an OSL SSH account, copy and paste the public key into your ticket. If we didn't ask you for a public key but you want one added to your account email it to support@osuosl.org, being sure to specify who you are and what project(s) you are associated with.
  - Or, to use the public key on a computer under your control, add it to ~/.ssh/authorized_keys (you can specify multiple public keys, one per line).
  - Never share your private key file, only the public key file.

Windows (using putty)
---------------------
`Great guide on setting up Filezilla with ssh keys <http://albertsk.files.wordpress.com/2012/12/putty-filezilla.pdf>`_
 `Download <http://the.earth.li/~sgtatham/putty/latest/x86/puttygen.exe>`_ and start the puttygen.exe generator.
  - In the "Key" section choose SSH-2 RSA and press Generate.
  - Move your mouse randomly in the small screen in order to generate the key pairs.
  - Enter a key comment, which will identify the key (useful when you use several SSH keys).
  - Type in the passphrase and confirm it. The passphrase is used to protect your key. You will be asked for it when you connect via SSH.
  - Click "Save private key" to save your private key.
  - Click "Save public key" to save your public key.
  - Email your public key to support@osuosl.org
  - keep your private key in a safe place  
  - when using putty go to connection->SSH->Auth and Browse to your private key
