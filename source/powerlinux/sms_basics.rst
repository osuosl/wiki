IBM Power SMS Basics
====================

SMS (System Management Services) is the eqivalent to the "BIOS" of an IBM POWER
machine. For our use we primarily use it to change the boot order on the
machine.

Getting into SMS
----------------

When the machine first boots up, press "1" a few times till the main menu shows
up::

    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM
    IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM IBM

              1 = SMS Menu                          5 = Default Boot List
              8 = Open Firmware Prompt              6 = Stored Boot List

         Memory      Keyboard     Network     SCSI

Change One-time Boot Order
--------------------------

Quick Howto
~~~~~~~~~~~

**Press 5, 1, 7, 2 (or which ever is the CDROM), 2, 1**

Boot Options
~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Main Menu
     1.   Select Language
     2.   Setup Remote IPL (Initial Program Load)
     3.   Change SCSI Settings
     4.   Select Console
     5.   Select Boot Options

     -------------------------------------------------------------------------------
     Navigation Keys:

                                                 X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:5

Boot Device
~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Multiboot
     1.   Select Install/Boot Device
     2.   Configure Boot Device Order
     3.   Multiboot Startup <OFF>
     4.   SAN Zoning Support

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:1

List All
~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Select Device Type
     1.   Diskette
     2.   Tape
     3.   CD/DVD
     4.   IDE
     5.   Hard Drive
     6.   Network
     7.   List all Devices

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:7

Select CDROM
~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Select Device
     Device  Current  Device
     Number  Position  Name
     1.        2      PORT - 6 IBM Host Ethernet Adapter
            ( loc=U78AB.001.WZSGFG5-P1-C2-T2 )
     2.        1      SCSI CD-ROM
            ( loc=U8231.E2B.06DAFDP-V6-C2-T1-L8300000000000000 )

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:2

Normal Boot Mode
~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Select Task

    SCSI CD-ROM
        ( loc=U8231.E2B.06DAFDP-V6-C2-T1-L8300000000000000 )

     1.   Information
     2.   Normal Mode Boot
     3.   Service Mode Boot

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:2


Exit
~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Are you sure you want to exit System Management Services?
     1.   Yes
     2.   No

     -------------------------------------------------------------------------------
     Navigation Keys:

                                                 X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:2

Change Default Boot Order
-------------------------

Quick Howto
~~~~~~~~~~~

**5, 2, 1, 8, (choose device), 2, x, 1**

Boot Options
~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Main Menu
     1.   Select Language
     2.   Setup Remote IPL (Initial Program Load)
     3.   Change SCSI Settings
     4.   Select Console
     5.   Select Boot Options

     -------------------------------------------------------------------------------
     Navigation Keys:

                                                 X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:5

Boot Device Order
~~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Multiboot
     1.   Select Install/Boot Device
     2.   Configure Boot Device Order
     3.   Multiboot Startup <OFF>
     4.   SAN Zoning Support

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:2

Configure Boot Device Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Configure Boot Device Order
     1.   Select 1st Boot Device
     2.   Select 2nd Boot Device
     3.   Select 3rd Boot Device
     4.   Select 4th Boot Device
     5.   Select 5th Boot Device
     6.   Display Current Setting
     7.   Restore Default Setting

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:1

Select Device Type
~~~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Select Device Type
     1.   Diskette
     2.   Tape
     3.   CD/DVD
     4.   IDE
     5.   Hard Drive
     6.   Network
     7.   None
     8.   List All Devices

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:8

Select Device
~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Select Device
     Device  Current  Device
     Number  Position  Name
     1.        -      PORT - 4 IBM Host Ethernet Adapter
            ( loc=U78AB.001.WZSGKV7-P1-C2-T2 )
     2.        2      SCSI CD-ROM
            ( loc=U8231.E2B.06D6DDP-V4-C2-T1-L8500000000000000 )
     3.        1      SCSI 249 GB Harddisk
            ( loc=U8231.E2B.06D6DDP-V4-C2-T1-L8100000000000000 )
     4.    None

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:

Set Boot Sequence
~~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Select Task

    SCSI 249 GB Harddisk
        ( loc=U8231.E2B.06D6DDP-V4-C2-T1-L8100000000000000 )

     1.   Information
     2.   Set Boot Sequence: Configure as 1st Boot Device

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:2

Current Boot Sequence
~~~~~~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Current Boot Sequence
     1.  SCSI 249 GB Harddisk
        ( loc=U8231.E2B.06D6DDP-V4-C2-T1-L8100000000000000 )
     2.  SCSI CD-ROM
        ( loc=U8231.E2B.06D6DDP-V4-C2-T1-L8500000000000000 )
     3.    None
     4.    None
     5.    None

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:x

Exit SMS
~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Are you sure you want to exit System Management Services?
     1.   Yes
     2.   No

     -------------------------------------------------------------------------------
     Navigation Keys:

                                                 X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:1

Show MAC Address
----------------

If you want to find the MAC address for an LPAR prior to it booting, do the
following.

Select Remote IPL
~~~~~~~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     Main Menu
     1.   Select Language
     2.   Setup Remote IPL (Initial Program Load)
     3.   Change SCSI Settings
     4.   Select Console
     5.   Select Boot Options

     -------------------------------------------------------------------------------
     Navigation Keys:

                                                 X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:2

MAC Address
~~~~~~~~~~~

::

    PowerPC Firmware
     Version AL730_066
     SMS 1.7 (c) Copyright IBM Corp. 2000,2008 All rights reserved.
    -------------------------------------------------------------------------------
     NIC Adapters
          Device                          Location Code                 Hardware
                                                                        Address
     1.  PORT - 6 IBM Host Ethernet Ada  U78AB.001.WZSGFL9-P1-C2-T2  5cf3fc86eb65

     -------------------------------------------------------------------------------
     Navigation keys:
     M = return to Main Menu
     ESC key = return to previous screen         X = eXit System Management Services
     -------------------------------------------------------------------------------
     Type menu item number and press Enter or select Navigation key:

References
----------

- `IBM SMS Documentation
  <http://publib.boulder.ibm.com/infocenter/powersys/v3r1m5/index.jsp?topic=/iphb6_p5/sms.htm>`_
