
.. _source/soc/ideas2010#google_summer_of_code_2010_ideas:

Google Summer of Code 2010 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code Ideas page.  

.. _source/soc/ideas2010#student_and_prospective_applicant_information:

Student and Prospective Applicant Information
---------------------------------------------
Thank you for your interest in the Open Source Lab's Summer of Code proposals.  Here at the OSL we feel we have a two-part goal.  First, we are a strong supporter of the open source community and want to help as many projects as we can.  Second, we are an educational institution that tries to incorporate teaching and learning into as much of what we do as possible.  The Google Summer of Code helps us to do both.

.. _source/soc/ideas2010#project_proposals:

Project proposals
~~~~~~~~~~~~~~~~~

**Proposals that are written poorly or in an unprofessional manner, use improper grammar or spelling, or do not answer all the questions in our :doc:`application template <soc/template>` completely will be rejected.**

It is important to note that none of these projects are cast in stone.  We very much want to work with our students on developing and shaping the project.  Think of this page as a general outline of some of the things we want to do.  Don't be afraid to propose something that does not exactly match what we have below.  If you have a great idea for a project that's not listed here, please feel free to submit it.  If it is a very well thought-out proposal with realistic goals, is in some way related to one of the `projects we work with <http://osuosl.org/services/hosting/communities/>`_ and something one of our mentors would be interested in working on, we may consider accepting it.

There's more to a good proposal than just a good project idea.  When we evaluate proposals, we don't just look at the idea itself.  We also look at how much thought and effort has gone into the proposal.  Does it have a roadmap or a timeline with milestones?  Are the milestones reasonable?  Is there time built in for documentation and bug-squashing?  Has something like this been done before?  If so, how is this proposal different?

.. _source/soc/ideas2010#expectations:

Expectations
~~~~~~~~~~~~
It's important when starting a new relationship like this that both sides are aware of the expectations involved.  We're a pretty easygoing bunch here at the OSL - we're far more interested in building neat stuff than we are about rigidly following some policies and procedures manual.  However, we do have some pretty simple expectations:

  - *Good communication is vital.*  If we accept your proposal, we expect you to be talking to your mentor on at least a weekly basis.  The method of communication - phone, e-mail, :doc:`IRC, <irc///irc.freenode.net/%23osuosl>` `carrier pigeon <http://www.faqs.org/rfcs/rfc1149.html>`_ - is up to you and your mentor, but the weekly contact is absolutely mandatory.  Exceptions are possible, but only if pre-arranged.  If we haven't heard from you in a week, your mentor will attempt to contact you with a friendly reminder.  If we don't hear from you after the reminder, we'll send you a formal warning.  If you don't respond to the formal warning, it is likely we will be submitting a negative evaluation to Google recommending you be dropped from the program.  It sounds dire, but it's easy to avoid: just keep in touch.
  - *Commit early and commit often.*  As mentors, we need to see the code you're working on.  It's really difficult to help someone if we can't see what you're doing.  We won't require anything as rigid as scheduled code check-ins, but the more often you share what you're working on with the rest of us, the better things will go.  There is one caveat: we absolutely have to have **some** code from you before the mid-term evaluation.  We need something upon which to base our evaluation.
  - *You're part of the team.*  We're very egalitarian here at the OSL - see `The Rules <http://qooxdoo.org/the_rules>`_ for more on our internal philosophy.  We firmly believe that once someone is a member of the OSL you are always a member, regardless of whether you are with us as an SoC student, a community volunteer, or as an employee of the Lab.  Before, during, or after the Summer of Code.  Much of what we do is driven by consensus and we're not strong on hierarchy, so please don't hesitate to jump right in and express your opinions!

.. _source/soc/ideas2010#contact_us:

Contact Us
~~~~~~~~~~
Questions?  Concerns?  Want ask us if we'd be interested in an application?  

   * **IRC** - Drop in and visit us in **#osuosl** on **irc.freenode.net**.  If you're not sure who to talk to ping **gchaix** or **kreneskyp** in **#osuosl** or **#gsoc**. 
   * **Email** - gsoc@osuosl.org
**Hint**: if we've already talked to you about your proposal, it helps your chances for acceptance.  We're happy to give feedback and suggestions on proposals, so it's a good idea talk to us before you submit it.  

.. _source/soc/ideas2010#project_list:

Project List
************ 

.. _source/soc/ideas2010#pydra:

Pydra
-----
Pydra is an open source parallel and clustered computing solution written in python using Twisted.Python and Django.  Pydra is a new project that is working towards it's first public release.

`Read more about pydra <http://pydra-project.osuosl.org>`_

.. _source/soc/ideas2010#project_ideas:

Project Ideas
~~~~~~~~~~~~~

.. _source/soc/ideas2010#contribute_to_pydra:

Contribute to Pydra
^^^^^^^^^^^^^^^^^^^
There are a lot of features on the wishlist for pydra.  Choose from these ideas, or check out the `task tracker <http://pydra-project.osuosl.org/report/2>`_:

  * `Statistical Analysis of Task Runtimes <http://pydra-project.osuosl.org/ticket/171>`_ - predict future runtimes and resource requirements.
  * `Cloud Support <http://pydra-project.osuosl.org/ticket/172>`_ - on demand provisioning and deployment to cloud based resources such as Amazon EC2.
  * `Function Wrapper <http://pydra-project.osuosl.org/ticket/20>`_ - Programmatically distributing work to the pydra cluster.
  * `Executable Tasks <http://pydra-project.osuosl.org/ticket/147>`_ - Tasks should be executable outside the cluster to allow easier development and debugging.

.. _source/soc/ideas2010#write_applications_using_pydra:

Write Applications Using Pydra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Develop an application that uses Pydra to reduce its run time.  Here are some suggestions, feel free to come up with your own ideas.
  * Web Crawler
  * Document Indexer

.. _source/soc/ideas2010#touchscreen_2.0:

Touchscreen 2.0
---------------
Touchscreen is software for running interactive slideshows/demos.  Touchscreen allows standalone slideshows or interactive displays using controls such as a touchscreen interface.  It is primarily used at the OSL on the large flatscreen+touchscreen directly outside our server room.  It displays various statistics and realtime data about the lab.

We are in the process of rewriting touchscreen to use Django, Jquery, javascript, HTML, and CSS.

`Learn more about Touchscreen <http://trac.osuosl.org/touchscreen>`_

.. _source/soc/ideas2010#project_ideas:

Project Ideas
~~~~~~~~~~~~~

.. _source/soc/ideas2010#write_a_screen_plugins:

Write a Screen Plugin(s)
^^^^^^^^^^^^^^^^^^^^^^^^
Write new plugin(s) that showcases things happening at the osl.  We'll supply the data, you supply an exciting representation of it.  

Here are some screens we have already produced:
  * :doc:`Plotting Locations of Our FTP Users on a World Map in Realtime <https///trac.osuosl.org/touchscreen/ticket/19>`
  * :doc:`OSL Bandwidth Usage <https///trac.osuosl.org/touchscreen/ticket/16>`
  * :doc:`FTP Bandwidth map <https///trac.osuosl.org/touchscreen/ticket/20>`
  * :doc:`Campus Webcams <https///trac.osuosl.org/touchscreen/ticket/11>`

Suggestions for new screens:
  * rewrite ftp user's map using google maps or `raphaeljs <http://raphaeljs.com>`_
  * twitter feed - display feed of specific user(s), and or hashtag(s)
  * trac project feed - project lists and recent commits
  * RT ticket feed - dashboard of in progress and waiting tickets

.. _source/soc/ideas2010#work_on_touchscreen_core:

Work on Touchscreen Core
^^^^^^^^^^^^^^^^^^^^^^^^
Here are some suggestions of things to be worked on, or take a look at the `task tracker <http://trac.osuosl.org/touchscreen/report/1>`_

  * :doc:`Menuing configuration <https///trac.osuosl.org/touchscreen/ticket/12>` - an interface for configuring a menuing system
  * :doc:`Menu Generation <https///trac.osuosl.org/touchscreen/ticket/13>` - display for the menu.