
.. _source/soc/ideas2012#google_summer_of_code_2012_ideas:

Google Summer of Code 2012 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code Ideas page.  

.. _source/soc/ideas2012#student_and_prospective_applicant_information:

Student and Prospective Applicant Information
---------------------------------------------

Thank you for your interest in the Open Source Lab's Summer of Code proposals.  Here at the OSL we feel we have a two-part goal.  First, we are a strong supporter of the open source community and want to help as many projects as we can.  Second, we are an educational institution that tries to incorporate teaching and learning into as much of what we do as possible.  The Google Summer of Code helps us to do both.

.. _source/soc/ideas2012#project_proposals:

Project proposals
~~~~~~~~~~~~~~~~~

**Proposals that are written poorly or in an unprofessional manner, use improper grammar or spelling, or do not answer all the questions in our :doc:`application template <soc/template>` completely will be rejected.**

It is important to note that none of these projects are cast in stone.  We very much want to work with our students on developing and shaping the project.  Think of this page as a general outline of some of the things we want to do.  Don't be afraid to propose something that does not exactly match what we have below.  If you have a great idea for a project that's not listed here, please feel free to submit it.  If it is a very well thought-out proposal with realistic goals, is in some way related to one of the `projects we work with <http://osuosl.org/services/hosting/communities/>`_ and something one of our mentors would be interested in working on, we may consider accepting it.

There's more to a good proposal than just a good project idea.  When we evaluate proposals, we don't just look at the idea itself.  We also look at how much thought and effort has gone into the proposal.  Does it have a roadmap or a timeline with milestones?  Are the milestones reasonable?  Is there time built in for documentation and bug-squashing?  Has something like this been done before?  If so, how is this proposal different?

.. _source/soc/ideas2012#expectations:

Expectations
~~~~~~~~~~~~
It's important when starting a new relationship like this that both sides are aware of the expectations involved.  We're a pretty easygoing bunch here at the OSL - we're far more interested in building neat stuff than we are about rigidly following some policies and procedures manual.  However, we do have some pretty simple expectations:

  - *Good communication is vital.*  If we accept your proposal, we expect you to be talking to your mentor on at least a weekly basis.  The method of communication - phone, e-mail, :doc:`IRC, <irc://irc.freenode.net/%23osuosl>` `carrier pigeon <http://www.faqs.org/rfcs/rfc1149.html>`_ - is up to you and your mentor, but the weekly contact is absolutely mandatory.  Exceptions are possible, but only if pre-arranged.  If we haven't heard from you in a week, your mentor will attempt to contact you with a friendly reminder.  If we don't hear from you after the reminder, we'll send you a formal warning.  If you don't respond to the formal warning, it is likely we will be submitting a negative evaluation to Google recommending you be dropped from the program.  It sounds dire, but it's easy to avoid: just keep in touch.
  - *Commit early and commit often.*  As mentors, we need to see the code you're working on.  It's really difficult to help someone if we can't see what you're doing.  We won't require anything as rigid as scheduled code check-ins, but the more often you share what you're working on with the rest of us, the better things will go.  There is one caveat: we absolutely have to have **some** code from you before the mid-term evaluation.  We need something upon which to base our evaluation.
  - *You're part of the team.*  We're very egalitarian here at the OSL - see `The Rules <http://qooxdoo.org/the_rules>`_ for more on our internal philosophy.  We firmly believe that once someone is a member of the OSL you are always a member, regardless of whether you are with us as an SoC student, a community volunteer, or as an employee of the Lab.  Before, during, or after the Summer of Code.  Much of what we do is driven by consensus and we're not strong on hierarchy, so please don't hesitate to jump right in and express your opinions!

.. _source/soc/ideas2012#contact_us:

Contact Us
~~~~~~~~~~
Questions?  Concerns?  Want ask us if we'd be interested in an application?  

   * **IRC** - Drop in and visit us in **#osuosl** on **irc.freenode.net**.  If you're not sure who to talk to ping **gchaix** or **Ramereth** in **#osuosl** or **#gsoc**. 
   * **Email** - gsoc@osuosl.org
**Hint**: if we've already talked to you about your proposal, it helps your chances for acceptance.  We're happy to give feedback and suggestions on proposals, so it's a good idea talk to us before you submit it.  

.. _source/soc/ideas2012#project_list:

Project List
************ 

.. _source/soc/ideas2012#ganeti_web_manager:

Ganeti Web Manager
------------------

`Ganeti Web Manager <http://code.osuosl.org/projects/ganeti-webmgr>`_ is a Django based web application that allows administrators and clients access to their `Ganeti virtualization clusters <http://code.google.com/p/ganeti/>`_.  Through Ganeti Web Manager users can deploy and manage virtual servers.  Ganeti Web Manager is being built by the Open Source Lab to support `Supercell <http://supercell.osuosl.org>`_, a testing cloud for open source projects.

Visit our irc channel #ganeti-webmgr on freenode for help getting started.

.. _source/soc/ideas2012#projects:

Projects
~~~~~~~~

  * `Realtime Metrics for virtual machines. <http://code.osuosl.org/issues/3615>`_
  * `Basic Puppet Integration - configuration management <http://code.osuosl.org/issues/3609>`_
  * `Implement Node Groups <http://code.osuosl.org/issues/6795>`_
  * `Bulk Operations <http://code.osuosl.org/issues/2745>`_
  * `Add visualization of clusters, nodes, and or virtual machines <http://code.osuosl.org/issues/9537>`_

.. _source/soc/ideas2012#ganeti_instance_image:

Ganeti Instance Image
---------------------

:doc:`Ganeti Instance Image <https://code.osuosl.org/projects/ganeti-image>` is a guest OS definition for Ganeti that uses either filesystem dumps or tar ball images to deploy instances. The goal of this OS definition is to allow fast and flexible installation of instances without the need for external tools such as debootstrap. It was originally based on ganeti-instance-debootstrap.

.. _source/soc/ideas2012#projects:

Projects
~~~~~~~~

  * Complete `version 0.6 release <http://code.osuosl.org/projects/ganeti-image/versions/339>`_ tasks
  * `Add support for OS Parameters <http://code.osuosl.org/issues/9549>`_
  * `FreeBSD OS support <http://code.osuosl.org/issues/225>`_
  * `Add support for AMI images <http://code.osuosl.org/issues/9555>`_
  * :doc:`Add support for OpenStack Images <htts///code.osuosl.org/issues/9561>`

.. _source/soc/ideas2012#osl_systems:

OSL Systems
-----------

OSL Systems are projects assist in the hosting infrastructure of the OSL.

.. _source/soc/ideas2012#projects:

Projects
~~~~~~~~

  * `check_hwraid LSI/MegaRAID/HP RAID Nagios Plugin <http://code.osuosl.org/issues/8715>`_
  * `Infrastructure-wide IPMI Management Console <http://code.osuosl.org/issues/9543>`_
  * `Create & Implement status.osuosl.org <http://code.osuosl.org/issues/6765>`_