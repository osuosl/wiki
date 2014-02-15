
.. _source/soc/ideas#google_summer_of_code_2008_ideas:

Google Summer of Code 2008 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code Ideas page.  

One of the things we learned in the past two Summer of Code programs is that the more time spent on collecting and refining the proposed project ideas, the better the summer goes.  So with that in mind ... ta-dah!  A new SoC ideas page.

.. _source/soc/ideas#student_and_prospective_applicant_information:

Student and Prospective Applicant Information
---------------------------------------------
Thank you for your interest in the Open Source Lab's Summer of Code proposals.  Here at the OSL we feel we have a two-part goal.  First, we are a strong supporter of the open source community and want to help as many projects as we can.  Second, we are an educational institution that tries to incorporate teaching and learning into as much of what we do as possible.  The Google Summer of Code helps us to do both.

.. _source/soc/ideas#project_proposals:

Project proposals
~~~~~~~~~~~~~~~~~
It is important to note that none of these projects are cast in stone.  We very much want to work with our students on developing and shaping the project.  Think of this page as a general outline of some of the things we want to do.  Don't be afraid to propose something that does not exactly match what we have below.  

If you have a great idea for a project that's not listed here, please feel free to submit it as well.  If it is a very well thought-out proposal with realistic goals, is in some way related to one of the `projects we work with <http://osuosl.org/hosting/clients>`_ and something one of our mentors would be interested in working on, we may accept it.

There's more to a good proposal than just a good project idea.  When we evaluate applications, we don't just look at the idea itself.  We also look at how much thought and effort has gone into the proposal.  Does it have a roadmap or a timeline with milestones?  Are the milestones reasonable?  Is there time built in for documentation and bug-squashing?  Has something like this been done before?  If so, how is this proposal different?

.. _source/soc/ideas#expectations:

Expectations
~~~~~~~~~~~~
It's important when starting a new relationship like this that both sides are aware of the expectations involved.  We're a pretty easygoing bunch here at the OSL - we're far more interested in building neat stuff than we are about rigidly following some policies and procedures manual.  However, we do have some pretty simple expectations:

  - *Good communication is vital.*  If we accept your proposal, we expect you to be talking to your mentor on at least a weekly basis.  The method of communication - phone, e-mail, :doc:`IRC, <irc///irc.freenode.net/%23osuosl>` `carrier pigeon <http://www.faqs.org/rfcs/rfc1149.html>`_ - is up to you and your mentor, but the weekly contact is absolutely mandatory.  Exceptions are possible, but only if pre-arranged.  If we haven't heard from you in a week, your mentor will attempt to contact you with a friendly reminder.  If we don't hear from you after the reminder, we'll send you a formal warning.  If you don't respond to the formal warning, it is likely we will be submitting a negative evaluation to Google recommending you be dropped from the program.  It sounds dire, but it's easy to avoid: just keep in touch.
  - *Commit early and commit often.*  As mentors, we need to see the code you're working on.  It's really difficult to help someone if we can't see what you're doing.  We won't require anything as rigid as scheduled code check-ins, but the more often you share what you're working on with the rest of us, the better things will go.  There is one caveat: we absolutely have to have **some** code from you before the mid-term evaluation.  We need something upon which to base our evaluation.
  - *You're part of the team.*  We're very egalitarian here at the OSL - see `The Rules <http://qooxdoo.org/the_rules>`_ for more on our internal philosophy.  We firmly believe that once someone is a member of the OSL you are always a member, regardless of whether you are with us as an SoC student, a community volunteer, or as an employee of the Lab.  Before, during, or after the Summer of Code.  Much of what we do is driven by consensus and we're not strong on hierarchy, so please don't hesitate to jump right in and express your opinions!

.. _source/soc/ideas#contact_us:

Contact Us
~~~~~~~~~~
Questions?  Concerns?  Want ask us if we'd be interested in an application?  Drop in and visit us in #osuosl on irc.freenode.net.  If you're not sure who to talk to ping gchaix in #osuosl or #gsoc. 

Hint: if we've already talked to you about your proposal, it helps your chances for acceptance.  We're happy to give feedback and suggestions on proposals, so it's a good idea talk to us before you submit it.  

.. _source/soc/ideas#drupal_-_moodle_integration:

Drupal - Moodle Integration
---------------------------

.. _source/soc/ideas#content_import/export:

Content Import/Export
~~~~~~~~~~~~~~~~~~~~~
For the first pass, it will probably be easiest to generate a file (a zip file of some other filetype?) that gets saved from one site, and then uploaded into the other.
  * Export a list of nodes as a Moodle course backup zip file

.. _source/soc/ideas#from_drupal:

From Drupal
^^^^^^^^^^^
  * A mechanism to select nodes for export as Moodle xml, possibly via a views include (like csv export, or rss)
   - Do we want to use a different mechanism than Moodle xml as the export format?
   - As we are preparing the nodes for export, should we specify what they will be imported as within Moodle (ie, a book page, an assignment, an activity, etc)? Or should this happen on the Moodle side. In thinking it over now, I think this choice should be made on export.

.. _source/soc/ideas#into_moodle:

Into Moodle
^^^^^^^^^^^
  * Use Moodle's course import functionality

.. _source/soc/ideas#from_moodle:

From Moodle
^^^^^^^^^^^
  * Use Moodle's course export functionality
   * what content type do we want to target for export?
    * teacher-created content
    * student-created content
     * for student-created content, how would we expose the export functionality to the students, given that they will not have the administrative rights to export courses?

.. _source/soc/ideas#into_drupal:

Into Drupal
^^^^^^^^^^^
  * At DrupalCon, I talked with the folks maintaining the FeedAPI, and they saw the future direction of the FeedAPI as morphing into a general import mechanism. When we talked this over earlier, we dismissed the FeedAPI as being used in this role, but, given the explicitly stated goal of the FeedAPI maintainers, I think we might be able to save time/lines of code by writing a custom parser for the FeedAPI that parsed Moodle xml. We had a reason why we dismissed this when we talked earlier; what was it?
  * Via web services (perhaps better as a second pass)

.. _source/soc/ideas#olpc_-_media_player_watch_&_listen:

OLPC - Media Player (Watch & Listen)
------------------------------------
Watch&Listen is a media player for the One Laptop Per Child (OLPC) aka the XO.  It uses the Helix media engine for playback.

  * Audio visualization(s)
  * Helix Auto-Update integration - automatic codecs downloads

.. _source/soc/ideas#helix_producer:

Helix Producer
--------------
Helix Producer is an encoding tool that is part of the Helix Media Engine.  It can read from some existing formats as well as capture audio/video from capture devices such as microphones, webcams, and TV cards.  Helix Producer is being used in several applications for the OLPC

.. _source/soc/ideas#h.323_videoconferencing_support:

H.323 (videoconferencing) Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Implementing any of the protocols required for standard videoconferencing:
  * Encoder for any of the following formats:
    * Video - H.261, H.263, H.264
    * Audio - G.711, G.729, G.729a, G.723.1, G.726
  * H.225 and or H.245 (connection management) support

.. _source/soc/ideas#image_support:

Image Support
~~~~~~~~~~~~~
 Output Plugin for any of the common image formats
    * BMP, JPG, PNG, GIF

.. _source/soc/ideas#aggregating_systems_reporting_tool:

Aggregating Systems Reporting Tool
----------------------------------

.. _source/soc/ideas#summary:

Summary
~~~~~~~

System administrators receive quite a bit of email from their systems hourly/daily/etc. Often times the emails are just informative and are often repetitive. There needs to be a way of sucking in the emails into an application which in turn, stores it in a sane manner, has an aggregate reporting mechanism, and an easy way to search the archives.

.. _source/soc/ideas#design:

Design
~~~~~~

 Implement an application that will use emails sent by systems that will import the data into a database. It will also offer the ability to easily define new data-sets and reports without needing to change the database schema. Basically, you define a template which this application uses to import the data. It would need to also have a "language" or a configuration file which dictates how it gathers the information. This might be similar to how `tenshi <http://www.gentoo.org/proj/en/infrastructure/tenshi/>`_ works for defining how to grab the information. 

An example of what we're wanting using a Mysql performance email.

  * Email gets sent out by each database server which has various information pertaining to the performance of that mysql instance
  * Application parses each email from each host and inputs the data into a database
  * Another script runs that will generate a daily/weekly report for the mysql performance and format the email in a specified way
  * The email gets sent to a list

Another feature that would be nice would be a webapp frontend. This frontend would be able to generate PDF or printable reports on the fly. It will also have a search function so we find various information easily without having to parse through emails. It could also display any trends that might be happening.

We have a working example written in python, but its written specifically for GLSA emails. Its current workflow is the following:

  * Encrypted GLSA emails get sent to a reporting email from every server
  * The python script accesses the imap box the email was delivered to
  * It decrypts the email
  * Generates the summary report, and sends it encrypted to an email address

The cron jobs are currently staggered an hour apart.

The current script is :doc:`here <soc:aggregate-security-reports.py>`, and an example of an :doc:`email report is here <soc:email-report1.txt>`. Also, here is an example of the :doc:`GLSA email <soc:email-glsa.txt>` that gets sent by every server.

.. _source/soc/ideas#unify_package_builder:

Unify Package Builder
---------------------

.. _source/soc/ideas#summary:

Summary
~~~~~~~

In the UNIX sysadmin world, there is no central ground for building packages that span distributions, and even operating systems. For the most part, each OS has their own set of tools to build packages. I'm (Lance) currently working on merging several tools into one tool called unify which will enable system administrators to use one spec file to build an RPM, deb, or solaris package. I'm using spec files primarily because there have been tools written for both debian and solaris which let you use spec files to build them. Unfortunately they both have slightly different ways of building packages. The goal of this project is to unify this into a simple command line driven system that works seamlessly. 

The current git repository is at `this link <http://git.osuosl.org/?p=unify.git;a=summary>`_.

.. _source/soc/ideas#gsoc_ideas:

GSoC ideas
~~~~~~~~~~

I'm still very much in the alpha stage of this project, but there's definitely potential for having a student work on a few parts of the project.

  * Implement creation of chroot environments
  * Implement building Solaris packages
  * Implement building Debian packages
  * Porting over a bunch of the standard packages in a shared repository

I'd prefer to use ebuilds rather than spec files, but unfortunately neither portage nor any of the alternatives that use ebuilds (pkgcore/paludis) don't have support for building binary packages yet. However, I am going to look into that.

.. _source/soc/ideas#maintain:

Maintain
--------

.. _source/soc/ideas#internationalization:

Internationalization
~~~~~~~~~~~~~~~~~~~~
Some of the parts are already in place, but more work needs to be done in order to fully support internationalization.
  * Make sure gettext functions are applied everywhere. Inline variables etc are not possible. Instead, the sprintf() function has to be used with %s, %d replacements etc.
  * Add per-user config options and global preferred language (mainly for the login screen and new users).
  * Translations of Maintain will be needed. A good idea might be to go to https://launchpad.net/rosetta the Ubuntu Rosetta project for that. This involves extracting the strings from Maintain and maybe writing some documentation on that.

.. _source/soc/ideas#supported_authentication_types:

Supported Authentication Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * Add ability for alternate authentication types including OpenID

.. _source/soc/ideas#drupal_as_an_openid_2.0_server:

Drupal as an OpenID 2.0 server
------------------------------
Build a Drupal module to allow Drupal to become a fully-featured OpenID server that supports the full OpenID 2.0 specification.

Desired features:
  * Provide OpenIDs for all local Drupal users
  * Support OpenID Attribute Exchange
    * Mapping profile and/or bio module fields to attributes
  * Whitelist and blacklist for OpenID servers and users

.. _source/soc/ideas#fossology:

FOSSology
---------

.. _source/soc/ideas#integration_with_other_data_sources:

Integration with other data sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The value of the public fossology repository would be enhanced considerably if it could refer other data sources, like Krugle, Ohloh, Swik, SourceForge, etc.  For example, FOSSology queries could use Ohloh tags, or report Ohloh development cost, or SourceForge rank.  These wouldn't replace those other repositories, but complement them and link to them for more indepth data that they provide.

.. _source/soc/ideas#code_dependency_analysis:

Code Dependency Analysis
~~~~~~~~~~~~~~~~~~~~~~~~
A big need we have is to figure out how to do a static dependency analysis.  For example, download a project from sourceforge and by analyzing the files, figure out what packages or libraries the code depends on.   The depfind project, http://depfind.sourceforge.net/, tries to do something similar for Java.  It would be great to have a dependency analyzer for C, C++, etc.

There are multiple uses for such an analysis.  For example, linux distributions could use it to make sure that their package dependencies are correct.  FOSSology, would use this for vulnerability tracking.  For example, if library A has a vulnerability and program B uses library C, but library C depends on A, then B depends on A and B may have the vulnerability.

.. _source/soc/ideas#internationalization_analysis:

Internationalization Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Take a project from sourceforge (or wherever) and looking at the project files, try and figure out the degree of internationalization.

.. _source/soc/ideas#code_vulnerabilities:

Code Vulnerabilities
~~~~~~~~~~~~~~~~~~~~
Relate vulnerabilities from the national vulnerability database (http://nvd.nist.gov/home.cfm) to files in the fossology repository.

.. _source/soc/ideas#cyber_alerts:

Cyber Alerts
~~~~~~~~~~~~
Relate cyber alerts (http://www.us-cert.gov/cas/techalerts/) to files in the fossology repository.