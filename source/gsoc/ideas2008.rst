Google Summer of Code 2008 Ideas
================================

.. note::

  This page is kept for historical purposes. Please check the latest year's
  ideas page for the most up to date information.

Welcome to the Oregon State University Open Source Lab Google Summer of Code
Ideas page.  

One of the things we learned in the past two Summer of Code programs is that the
more time spent on collecting and refining the proposed project ideas, the
better the summer goes.  So with that in mind ... ta-dah!  A new SoC ideas page.

Drupal - Moodle Integration
---------------------------

Content Import/Export
~~~~~~~~~~~~~~~~~~~~~

For the first pass, it will probably be easiest to generate a file (a zip file
of some other filetype?) that gets saved from one site, and then uploaded into
the other.

- Export a list of nodes as a Moodle course backup zip file

From Drupal
^^^^^^^^^^^

- A mechanism to select nodes for export as Moodle xml, possibly via a views
  include (like csv export, or rss)

  - Do we want to use a different mechanism than Moodle xml as the export
    format?
  - As we are preparing the nodes for export, should we specify what they will
    be imported as within Moodle (ie, a book page, an assignment, an activity,
    etc)? Or should this happen on the Moodle side. In thinking it over now, I
    think this choice should be made on export.

Into Moodle
^^^^^^^^^^^

- Use Moodle's course import functionality

From Moodle
^^^^^^^^^^^

- Use Moodle's course export functionality

 - what content type do we want to target for export?

  - teacher-created content
  - student-created content

   - for student-created content, how would we expose the export functionality
     to the students, given that they will not have the administrative rights to
     export courses?

Into Drupal
^^^^^^^^^^^

- At DrupalCon, I talked with the folks maintaining the FeedAPI, and they saw
  the future direction of the FeedAPI as morphing into a general import
  mechanism. When we talked this over earlier, we dismissed the FeedAPI as being
  used in this role, but, given the explicitly stated goal of the FeedAPI
  maintainers, I think we might be able to save time/lines of code by writing a
  custom parser for the FeedAPI that parsed Moodle xml. We had a reason why we
  dismissed this when we talked earlier; what was it?
- Via web services (perhaps better as a second pass)

OLPC - Media Player (Watch & Listen)
------------------------------------
Watch&Listen is a media player for the One Laptop Per Child (OLPC) aka the XO.
It uses the Helix media engine for playback.

- Audio visualization(s)
- Helix Auto-Update integration - automatic codecs downloads

Helix Producer
--------------

Helix Producer is an encoding tool that is part of the Helix Media Engine.  It
can read from some existing formats as well as capture audio/video from capture
devices such as microphones, webcams, and TV cards.  Helix Producer is being
used in several applications for the OLPC

H.323 (videoconferencing) Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementing any of the protocols required for standard videoconferencing:

- Encoder for any of the following formats:

  - Video - H.261, H.263, H.264
  - Audio - G.711, G.729, G.729a, G.723.1, G.726
- H.225 and or H.245 (connection management) support

Image Support
~~~~~~~~~~~~~

Output Plugin for any of the common image formats

- BMP, JPG, PNG, GIF

Aggregating Systems Reporting Tool
----------------------------------

Summary
~~~~~~~

System administrators receive quite a bit of email from their systems
hourly/daily/etc. Often times the emails are just informative and are often
repetitive. There needs to be a way of sucking in the emails into an application
which in turn, stores it in a sane manner, has an aggregate reporting mechanism,
and an easy way to search the archives.

Design
~~~~~~

Implement an application that will use emails sent by systems that will import
the data into a database. It will also offer the ability to easily define new
data-sets and reports without needing to change the database schema. Basically,
you define a template which this application uses to import the data. It would
need to also have a "language" or a configuration file which dictates how it
gathers the information. This might be similar to how `tenshi`_ works for
defining how to grab the information. 

.. _tenshi: http://www.gentoo.org/proj/en/infrastructure/tenshi/

An example of what we're wanting using a Mysql performance email.

- Email gets sent out by each database server which has various information
  pertaining to the performance of that mysql instance
- Application parses each email from each host and inputs the data into a
  database
- Another script runs that will generate a daily/weekly report for the mysql
  performance and format the email in a specified way
- The email gets sent to a list

Another feature that would be nice would be a webapp frontend. This frontend
would be able to generate PDF or printable reports on the fly. It will also have
a search function so we find various information easily without having to parse
through emails. It could also display any trends that might be happening.

We have a working example written in python, but its written specifically for
GLSA emails. Its current workflow is the following:

- Encrypted GLSA emails get sent to a reporting email from every server
- The python script accesses the imap box the email was delivered to
- It decrypts the email
- Generates the summary report, and sends it encrypted to an email address

The cron jobs are currently staggered an hour apart.

The current script is :doc:`here <soc:aggregate-security-reports.py>`, and an
example of an :doc:`email report is here <soc:email-report1.txt>`. Also, here is
an example of the :doc:`GLSA email <soc:email-glsa.txt>` that gets sent by every
server.

Unify Package Builder
---------------------

Summary
~~~~~~~

In the UNIX sysadmin world, there is no central ground for building packages
that span distributions, and even operating systems. For the most part, each OS
has their own set of tools to build packages. I'm (Lance) currently working on
merging several tools into one tool called unify which will enable system
administrators to use one spec file to build an RPM, deb, or solaris package.
I'm using spec files primarily because there have been tools written for both
debian and solaris which let you use spec files to build them. Unfortunately
they both have slightly different ways of building packages. The goal of this
project is to unify this into a simple command line driven system that works
seamlessly. 

The current git repository is at `this link`_.

.. _this link: http://git.osuosl.org/?p=unify.git;a=summary

GSoC ideas
~~~~~~~~~~

I'm still very much in the alpha stage of this project, but there's definitely
potential for having a student work on a few parts of the project.

- Implement creation of chroot environments
- Implement building Solaris packages
- Implement building Debian packages
- Porting over a bunch of the standard packages in a shared repository

I'd prefer to use ebuilds rather than spec files, but unfortunately neither
portage nor any of the alternatives that use ebuilds (pkgcore/paludis) don't
have support for building binary packages yet. However, I am going to look into
that.

Maintain
--------

Internationalization
~~~~~~~~~~~~~~~~~~~~
Some of the parts are already in place, but more work needs to be done in order
to fully support internationalization.

- Make sure gettext functions are applied everywhere. Inline variables etc are
  not possible. Instead, the sprintf() function has to be used with %s, %d
  replacements etc.

  - Add per-user config options and global preferred language (mainly for the
    login screen and new users).
  - Translations of Maintain will be needed. A good idea might be to go to
    https://launchpad.net/rosetta the Ubuntu Rosetta project for that. This
    involves extracting the strings from Maintain and maybe writing some
    documentation on that.

Supported Authentication Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Add ability for alternate authentication types including OpenID

Drupal as an OpenID 2.0 server
------------------------------

Build a Drupal module to allow Drupal to become a fully-featured OpenID server
that supports the full OpenID 2.0 specification.

Desired features:
- Provide OpenIDs for all local Drupal users
- Support OpenID Attribute Exchange

  - Mapping profile and/or bio module fields to attributes

- Whitelist and blacklist for OpenID servers and users

FOSSology
---------

Integration with other data sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The value of the public fossology repository would be enhanced considerably if
it could refer other data sources, like Krugle, Ohloh, Swik, SourceForge, etc.
For example, FOSSology queries could use Ohloh tags, or report Ohloh development
cost, or SourceForge rank.  These wouldn't replace those other repositories, but
complement them and link to them for more indepth data that they provide.

Code Dependency Analysis
~~~~~~~~~~~~~~~~~~~~~~~~

A big need we have is to figure out how to do a static dependency analysis.  For
example, download a project from sourceforge and by analyzing the files, figure
out what packages or libraries the code depends on.   The depfind project,
http://depfind.sourceforge.net/, tries to do something similar for Java.  It
would be great to have a dependency analyzer for C, C++, etc.

There are multiple uses for such an analysis.  For example, linux distributions
could use it to make sure that their package dependencies are correct.
FOSSology, would use this for vulnerability tracking.  For example, if library A
has a vulnerability and program B uses library C, but library C depends on A,
then B depends on A and B may have the vulnerability.

Internationalization Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Take a project from sourceforge (or wherever) and looking at the project files,
try and figure out the degree of internationalization.

Code Vulnerabilities
~~~~~~~~~~~~~~~~~~~~

Relate vulnerabilities from the national vulnerability database
(http://nvd.nist.gov/home.cfm) to files in the fossology repository.

Cyber Alerts
~~~~~~~~~~~~

Relate cyber alerts (http://www.us-cert.gov/cas/techalerts/) to files in the
fossology repository.
