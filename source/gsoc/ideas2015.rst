Google Summer of Code 2015 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code
2015 idea page! Before applying please read over our :ref:`application guide
<gsoc-app-info>` for details specific to our organization.

Ideas
-----
- :ref:`gsoc2015-data-center-tools`
- :ref:`gsoc2015-whats-fresh`
- :ref:`gsoc2015-other-projects`

.. _gsoc2015-data-center-tools:

Data Center Tools
~~~~~~~~~~~~~~~~~

Project: Infrastructure-wide IPMI/SNMP Management Console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explanation:**

We host a variety of systems in our data center which include a wide array of
vendors (i.e. Dell, HP, Sun, etc). Each of these machines utilize some type of
out-of-band (OOB) technology such as iLO or iDrac which allows direct access to
the machine power, console and other features. Unfortunately each OOB tool is
different between the command line access and the console access. 

However server machines support the IPMI standard which basically does the same,
and PDUs (Power Distribution Units) use another common standard, SNMP.

There are several FOSS tools out there already that utilize IPMI and SNMP in some
fashion, but none create a complete tool that stores a whole infrastructure into
an interface. We have begun work on an IPMI management tool, and would like to 
integrate SNMP functionality with this to create a unified OOB management tool.

**Expected Results**

Either a command line driven or web app driven interface that allows for
viewing and addition of machines and PDUs, access to power, serial and vga console,
authentication of users and authorization by user and group. Optionally show event 
logs, time-based metrics, and any sensor data.

**Knowledge Prerequisite:**

Basic understanding of production-grade datacenter hardware, ability to program in
Python, and a good grasp of API driven interfaces.

**Mentor:** Lance (Ramereth)

------

.. _gsoc2015-whats-fresh:

What's Fresh
~~~~~~~~~~~~

Project: What's Fresh version 2.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What's Fresh is an open source project originally funded by the `Oregon Sea Grant`_
to create a mobile app for locating fresh local seafood on the Oregon coast. 
Version 1.0 was created by a collaboration between OSU's `Business Solutions Group`_
and the OSL under the umbrella of OSU's `Center for Applied Systems and Software`_ (CASS). It
consists of a `Django driven API`_ and a multi-platform (iOS and Android) `mobile app`_ 
created with the Sencha tool kit. It was designed to be easily adapted to any
community that sells any kind of local produce and provides an easy way for people 
to find markets, products, vendors, and detailed information about what they are buying.

**Expected Results**

Improvements to the Django data entry system to allow map-based location data entry
and in general a smoother and simpler data entry process, a theming and customization
system for the mobile and API apps to allow users to easily adapt them to other
communities, and an automated build process for the mobile application.


**Knowledge Prerequisite:**

Basic understanding of the Django application framework, ability to program in
Python, and familiarity with mobile applications, PhoneGap or related tools, and 
REST APIs.

**Mentor:** Ken (kennric)

.. _Oregon Sea Grant: http://seagrant.oregonstate.edu/
.. _Business Solutions Group: http://bsg.oregonstate.edu/
.. _Center for Applied Systems and Software: http://cass.oregonstate.edu/
.. _Django driven API: https://github.com/osu-cass/whats-fresh-api
.. _mobile app: https://github.com/osu-cass/whats-fresh-mobile

------

.. _gsoc2015-other-projects:

Other OSL Projects
~~~~~~~~~~~~~~~~~~

These are projects we don't have specific project proposals for, but you are
free to take a look at and discuss with us any you might be interested in doing.


Protein Geometry Database (PGD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Protein Geometry Database`_ is a specialized search engine for protein
geometry.  It allows you to explore either protein conformation or protein
covalent geometry or the correlations between protein conformation and bond
angles and lengths. It is primarily a Django project with a lot of javascript
logic built into it. This project is a joint venture between the OSUOSL and the
Oregon State University Biochemistry department on campus.

.. _Protein Geometry Database: https://code.osuosl.org/projects/pgd

This project has seen significant development in the last year, and several 
important features are still on the horizon, such as support for newer protein
file formats and support for very large proteins. 

This is an excellent project for anyone with an interest in bioinformatics or open source science.

One specific area of the PGD that needs improvement is the user
management system.  Users should be able to store and manipulate their
searches, including comparing historical results to current results.
There is some additional functionality planned for admin users with
regard to database management as well.

*Please talk to kennric in #osuosl-gsoc on Freenode if you want to propose an
idea for this project.*

----

Template
--------

::

    Primary Project Name
    ~~~~~~~~~~~~~~~~~~~~

    Project: GSoC Idea
    ^^^^^^^^^^^^^^^^^^

    **Brief Explanation:**

    **Expected Results**

    **Knowledge Prerequisite:**

    Mentor:
