
.. _source/public/ibmpower/hmc_basics#hmc_basics:

HMC Basics
==========

Connecting to an LPAR is always done via the HMC (Hardware Management Console). You can think of the HMC as a control console for creating, modifying, and accessing all the resources on all the machines connected to it. It has a web interface and an ssh shell.

The hostname for the OSL HMC is **oslhmc.osuosl.bak (10.1.0.50)** and requires access via our VPN.

.. _source/public/ibmpower/hmc_basics#command_line:

Command line
------------

.. _source/public/ibmpower/hmc_basics#starting_an_lpar:

Starting an LPAR
~~~~~~~~~~~~~~~~

::

    chsysstate -r lpar -o on -b norm -f Default -m powerdev1 -n chinook.fedora

Some notable options (these carry on to other commands with chsysstate):

  * "``-f Default``" -- name of the profile to use, typically named **``Default``**.
  * "``-m powerdev1``" -- name of the machine the LPAR is on
  * "``-n chinook.fedora``" -- name of the LPAR

.. _source/public/ibmpower/hmc_basics#shutdown/restart_an_lpar:

Shutdown/Restart an LPAR
~~~~~~~~~~~~~~~~~~~~~~~~

::

    # Graceful shutdown
    chsysstate -o shutdown --immed -r lpar -m powerdev1 -n chinook.fedora

    # Immediate shutdown (no waiting from OS)
    chsysstate -o shutdown --immed -r lpar -m powerdev1 -n chinook.fedora

    # Restart
    chsysstate -o shutdown -r lpar --immed -m powerdev1 -n chinook.fedora

    # Immediate restart (no waiting from OS)
    chsysstate -o shutdown -r lpar --immed --restart -m powerdev1 -n chinook.fedora

.. _source/public/ibmpower/hmc_basics#console:

Console
~~~~~~~

::

    # connect to console
    mkvterm -m powerdev1 -p chinook.fedora

    # close an open console session
    rmvterm -m powerdev1 -p chinook.fedora

The escape code is unfortunately **``~.``** although you can escape it and not kill you connection by doing **``~~.``**

.. _source/public/ibmpower/hmc_basics#adding_ssh_key:

Adding SSH Key
~~~~~~~~~~~~~~

::

    $ ssh username@oslhmc.osuosl.bak
    $ mkauthkeys --add "key string"

To add it to a specific user:

::

    $ ssh osuadmin@oslhmc.osuosl.bak
    $ mkauthkeys -u userid --add "key string"

.. _source/public/ibmpower/hmc_basics#other_hmc_commands:

Other HMC Commands
------------------

Here are some other HMC related commands you may or may not have access to.

::

    asmmenu bkconsdata bkprofdata chaccfg chhwres chsysstate chcod chled chusrtca
    chcuod chlparutil chvet chhmc chsacfg chsyscfg chhmcusr chsvcevent chsyspwd
    deploysysplan hmcshutdown hmcwin installios osinstall lscuod lshwinfo
    lslparutil lssvcevents lsvet lsdump lshwres lsmediadev lssyscfg lshmc lsled
    lspartition lssysconn lsaccfg lshmcusr lslic lsrefcode lssysplan lscod lshsc
    lslock lssacfg lsusrtca lpar_netboot migrcfg mkaccfg mkhmcusr mksysconn mkvterm
    mkauthkeys mksyscfg mksysplan rmaccfg rmlparutil rmsysplan rstprofdata rmhmcusr
    rmsyscfg rmvterm runlpcmd rmlock rmsysconn rsthwres viosvrcmd

.. _source/public/ibmpower/hmc_basics#references:

References
----------

  * `IBM DeveloperWorks HMC Command Line <http://www.ibm.com/developerworks/wikis/display/LinuxP/HMC+command+line>`_