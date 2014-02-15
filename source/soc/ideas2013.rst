
.. _source/soc/ideas2013#google_summer_of_code_2013_ideas:

Google Summer of Code 2013 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code Ideas page.  

.. _source/soc/ideas2013#student_and_prospective_applicant_information:

Student and Prospective Applicant Information
---------------------------------------------

Thank you for your interest in the Open Source Lab's Summer of Code proposals.  Here at the OSL we feel we have a two-part goal.  First, we are a strong supporter of the open source community and want to help as many projects as we can.  Second, we are an educational institution that tries to incorporate teaching and learning into as much of what we do as possible.  The Google Summer of Code helps us to do both.

We ***highly recommend*** you read the `GSoC Student Guide <http://flossmanuals.net/GSoCStudentGuide/>`_ to ensure your success in writing your proposal and hopefully eventually being an accepted student in our organization. Specifically please check out the `writing a proposal <http://en.flossmanuals.net/GSoCStudentGuide/ch008_writing-a-proposal/>`_ guide and the `proposal <http://en.flossmanuals.net/GSoCStudentGuide/ch027_proposal-example-1/>`_ `examples <http://en.flossmanuals.net/GSoCStudentGuide/ch028_proposal-example-2/>`_ so that you get all of the information that we need.

.. _source/soc/ideas2013#project_proposals:

Project proposals
~~~~~~~~~~~~~~~~~

**Proposals that are written poorly or in an unprofessional manner, use improper grammar or spelling, or do not answer all the questions in our :doc:`application template <soc/template>` completely will be rejected.**

It is important to note that none of these projects are cast in stone.  We very much want to work with our students on developing and shaping the project.  Think of this page as a general outline of some of the things we want to do.  Don't be afraid to propose something that does not exactly match what we have below.  If you have a great idea for a project that's not listed here, please feel free to submit it.  If it is a very well thought-out proposal with realistic goals, is in some way related to one of the `projects we work with <http://osuosl.org/services/hosting/communities/>`_ and something one of our mentors would be interested in working on, we may consider accepting it.

There's more to a good proposal than just a good project idea.  When we evaluate proposals, we don't just look at the idea itself.  We also look at how much thought and effort has gone into the proposal.  Does it have a roadmap or a timeline with milestones?  Are the milestones reasonable?  Is there time built in for documentation and bug-squashing?  Has something like this been done before?  If so, how is this proposal different?

.. _source/soc/ideas2013#expectations:

Expectations
~~~~~~~~~~~~
It's important when starting a new relationship like this that both sides are aware of the expectations involved.  We're a pretty easygoing bunch here at the OSL - we're far more interested in building neat stuff than we are about rigidly following some policies and procedures manual.  However, we do have some pretty simple expectations:

  - *Good communication is vital.*  If we accept your proposal, we expect you to be talking to your mentor on at least a weekly basis.  The method of communication - phone, e-mail, :doc:`IRC, <irc///irc.freenode.net/%23osuosl>` `carrier pigeon <http://www.faqs.org/rfcs/rfc1149.html>`_ - is up to you and your mentor, but the weekly contact is absolutely mandatory.  Exceptions are possible, but only if pre-arranged.  If we haven't heard from you in a week, your mentor will attempt to contact you with a friendly reminder.  If we don't hear from you after the reminder, we'll send you a formal warning.  If you don't respond to the formal warning, it is likely we will be submitting a negative evaluation to Google recommending you be dropped from the program.  It sounds dire, but it's easy to avoid: just keep in touch.
  - *Commit early and commit often.*  As mentors, we need to see the code you're working on.  It's really difficult to help someone if we can't see what you're doing.  We won't require anything as rigid as scheduled code check-ins, but the more often you share what you're working on with the rest of us, the better things will go.  There is one caveat: we absolutely have to have **some** code from you before the mid-term evaluation.  We need something upon which to base our evaluation.
  - *You're part of the team.*  We're very egalitarian here at the OSL. We firmly believe that once someone is a member of the OSL you are always a member, regardless of whether you are with us as an SoC student, a community volunteer, or as an employee of the Lab.  Before, during, or after the Summer of Code.  Much of what we do is driven by consensus and we're not strong on hierarchy, so please don't hesitate to jump right in and express your opinions!

.. _source/soc/ideas2013#contact_us:

Contact Us
~~~~~~~~~~
Questions?  Concerns?  Want ask us if we'd be interested in an application?  

   * **IRC** - Drop in and visit us in **#osuosl** on **irc.freenode.net**.  If you're not sure who to talk to ping **Ramereth**, **kennric**, **pwnguin** or **basic`** in **#osuosl**. 
   * **Email** - gsoc@osuosl.org
**Hint**: if we've already talked to you about your proposal, it helps your chances for acceptance.  We're happy to give feedback and suggestions on proposals, so it's a good idea talk to us before you submit it.  

.. _source/soc/ideas2013#project_list:

Project List
************ 

.. _source/soc/ideas2013#ganeti_web_manager:

Ganeti Web Manager
------------------

`Ganeti Web Manager <http://code.osuosl.org/projects/ganeti-webmgr>`_ is a Django based web application that allows administrators and clients access to their `Ganeti virtualization clusters <http://code.google.com/p/ganeti/>`_.  Through Ganeti Web Manager users can deploy and manage virtual servers.  Ganeti Web Manager is being built by the Open Source Lab to support `Supercell <http://supercell.osuosl.org>`_, a testing cloud for open source projects.

If you would like to get started with playing with Ganeti, we recommend you checkout our :doc:`Ganeti Vagrant Development/Testing Environment <https///github.com/ramereth/vagrant-ganeti>` (look at the README for instructions). It uses VirtualBox to create a small Ganeti cluster on your own computer so you can understand the basics. Additionally we recommend you read the `Ganeti Walk-through documentation <http://docs.ganeti.org/ganeti/current/html/walkthrough.html>`_ to familiarize yourself with Ganeti. You can also checkout this `Ganeti Tutorial Guide <http://www.lancealbertson.com/wp-content/uploads/2012/06/GanetiTutorialPDFSheet.pdf>`_ to do some hands on command line familiarization. 

Visit our irc channel **#ganeti-webmgr** on freenode for help getting started. 

.. _source/soc/ideas2013#projects:

Projects
~~~~~~~~

These projects are only suggested by us. Please feel free to look at the :doc:`GWM Issue Tracker <https///code.osuosl.org/projects/ganeti-webmgr/issues>` for more ideas for projects. But please discuss any ideas with us first.

**`Bulk Operations <http://code.osuosl.org/issues/2745>`_**

*Please talk with us about this project before submitting your proposal.*

We have started working on some of the Bulk operation tasks but this project would likely be mostly focused on the :doc:`Bulk VM Creation <https///code.osuosl.org/issues/2751>` feature. This will require quite a bit of thought on how the UI works and how it will interact with the templating system we've implemented.

**`Add visualization of clusters, nodes, and or virtual machines <http://code.osuosl.org/issues/9537>`_**

This would be for visualizating how the cluster works and how the virtual machines and nodes interact. It does not use any real-time monitoring data other than what Ganeti provides itself. The goal is to help cluster admins see how their cluster is doing from a visual point of view.

**Implement a mobile site**

Currently GWM does not offer any mobile site solution. The goal of this project would be to create a mobile version of some of the basic features GWM provides. It wouldn't offer access to the console for example, but at least access to control the VM's power state, see cluster status, deploy a new VM, etc. 

.. _source/soc/ideas2013#vagrant:

Vagrant
-------

`Vagrant <http://www.vagrantup.com/>`_ is an open source tool that we use at the lab quite a bit. It currently supports :doc:`VirtualBox <https///www.virtualbox.org/>` and now more recently VMWare. Vagrant itself is still in a bit of flux over this so we may need to work with upstream on the viability of adding this feature.

.. _source/soc/ideas2013#projects:

Projects
~~~~~~~~

**Add Ganeti provider to Vagrant**

The project would be to create a `Ganeti <http://code.google.com/p/ganeti/>`_ provider for Vagrant which will allow users to power their virtual machines from a ganeti cluster instead of depending on their local workstation. This is ideal for use cases such as testing an environment with hundreds of VMs. Vagrant upstream recently made a change to their code to that `writing a provider would be possible <http://docs.vagrantup.com/v2/plugins/providers.html>`_. Ganeti provides an `Remote API (RAPI) <http://docs.ganeti.org/ganeti/current/html/rapi.html>`_ to manage a cluster from however it doesn't quite line up with a lot of other providers. 

The scope of the project would likely be:

  - Write a basic provider that connects to the RAPI and can deploy/connect to a virtual machine using the normal Ganeti deployment strategy.
  - Try to add other vagrant specific features if the RAPI supports it directly.
  - Attempt to implement importing of boxes into Ganeti (this may not be easily possible).

.. _source/soc/ideas2013#openconferenceware-android:

Openconferenceware-Android
--------------------------

:doc:`Openconferenceware-android <https///github.com/osuosl/ocw-android>` is an open source project we started three years ago to provide an android conference app for Open Source Bridge. Since then its unfortunately been neglected by us and has been mostly taken care of by Igal's :doc:`fork of OCW-Android <https///github.com/igal/opensourcebridge-android>`. It was also used at OSCON in 2010. Please also take a look at the :doc:`project page <https///code.osuosl.org/projects/ocw-android>` for background info and documentation.

We intend to re-launch the project and try to merge in the changes that Igal and others have done to try and unify the project.

.. _source/soc/ideas2013#projects:

Projects
~~~~~~~~

Some of these can be merged into one large task:

**Merge all forked code into a unified code-base**

Test all the code from various forks and try to merge any useful features or commits. Try to generalize any site specific code that might be included in the other projects. Update the documentation.

**Add new useful features**

We don't have any specific features we'd like to add but taking a look at the various issue trackers might be a good place to start.

**Make the app more flexible to other conference data formats**

Right now the application will only work with :doc:`Openconferenceware's <https///github.com/igal/openconferenceware>` data format which isn't very flexible. In the past we wrote a small Django application called :doc:`ocw-android-oscon-dataservice <https///github.com/osuosl/ocw-android-oscon-dataservice>` which screen scraped the OSCON site to generate a format that worked. Its not the most ideal solution but it worked at the time. It would be nice to have a more unified way to make this work whether you're using Drupal to run a conference or whatever else.

.. _source/soc/ideas2013#ganeti_instance_image:

Ganeti Instance Image
---------------------

:doc:`Ganeti Instance Image <https///code.osuosl.org/projects/ganeti-image>` is a guest OS definition for Ganeti that uses either filesystem dumps or tar ball images to deploy instances. The goal of this OS definition is to allow fast and flexible installation of instances without the need for external tools such as debootstrap. It was originally based on :doc:`ganeti-instance-debootstrap <https///code.google.com/p/ganeti/>`.

.. _source/soc/ideas2013#projects:

Projects
~~~~~~~~

**`Add support for OS Parameters <http://code.osuosl.org/issues/9549>`_**

**:doc:`Add support for shared file <https///code.osuosl.org/issues/12159>`**

.. _source/soc/ideas2013#ganeti:

Ganeti
------

`Ganeti <http://code.google.com/p/ganeti/>`_ is an open source project run by Google and used heavily at the lab. It provides a manangement layer on open of various open source hypervisors such as KVM and Xen to provider a stable virtualization platform.

.. _source/soc/ideas2013#projects:

Projects
~~~~~~~~

**Improve support for LXC hypervisor**

Currently Ganeti has limited support for `LXC <http://lxc.sourceforge.net/>`_ and has an open `feature bug <http://code.google.com/p/ganeti/issues/detail?id=249>`_ for improving the support. We'd like to work with the upstream project and have a GSoC student work on improving this feature. This would require quite a bit of knowledge of how LXC and Ganeti works so only advanced students need apply. They would likely need to know a fair bit about python as well and possibly a little bit of haskell.

.. _source/soc/ideas2013#other_osl_projects:

Other OSL Projects
------------------

We have other projects that you might be interested in however we don't have a specific idea in mind for GSoC. You might take a look at their issue trackers and see if any of them interest you. Some are old projects that we haven't touched in a while because of other priorities so please keep that in mind.

.. _source/soc/ideas2013#protein_geometry_database_pgd:

Protein Geometry Database (PGD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Protein Geometry Database <https///code.osuosl.org/projects/pgd>` is a specialized search engine for protein geometry. It allows you to explore either protein conformation or protein covalent geometry or
the correlations between protein conformation and bond angles and lengths. It is primarily a django project with a lot of javascript logic built into it. This project is a joint venture between the OSUOSL and the `Oregon State University Biochemistry department <http://biochem.science.oregonstate.edu/>`_ on campus.

Feel free to take a look at the :doc:`PGD Issue Tracker <https///code.osuosl.org/projects/pgd/issues>` for ideas but *please discuss any potential ideas with us first before pursuing them*.

.. _source/soc/ideas2013#touchscreen:

Touchscreen
~~~~~~~~~~~

:doc:`Touchscreen <https///code.osuosl.org/projects/touchscreen>` is a framework for developing interactive kiosk displays. Touchscreen powers the display screen used outside the Open Source Lab's server room. We use a 42" LCD flat screen, with a 17" touchscreen display to control it. Screens are built using HTML, CSS, and Javascript and the backend is powered via Django. Touchscreen was a :ref:`GSoC 2010 <https///wiki.osuosl.org/soc/ideas2010#touchscreen_20>` project and was very successful.

Unfortunately over time the project has been left unmaintained due to staff time and it horribly outdated (i.e. still uses a very old version of Django). We would like to revive the project with some renewed focus. Please take a look at the project and discuss with us any ideas you are interested in.

