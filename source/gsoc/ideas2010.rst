Google Summer of Code 2010 Ideas
================================

.. note::

  This page is kept for historical purposes. Please check the latest year's
  ideas page for the most up to date information.

Welcome to the Oregon State University Open Source Lab Google Summer of Code
Ideas page.  

Pydra
-----

Pydra is an open source parallel and clustered computing solution written in
python using Twisted.Python and Django.  Pydra is a new project that is working
towards it's first public release.

`Read more about pydra <http://pydra-project.osuosl.org>`_

Project Ideas
~~~~~~~~~~~~~

Contribute to Pydra
^^^^^^^^^^^^^^^^^^^

There are a lot of features on the wishlist for pydra.  Choose from these ideas,
or check out the `task tracker`__:

.. __: http://pydra-project.osuosl.org/report/2

- `Statistical Analysis of Task Runtimes`_ - predict future runtimes and
  resource requirements.
- `Cloud Support`_ - on demand provisioning and deployment to cloud based
  resources such as Amazon EC2.
- `Function Wrapper`_ - Programmatically distributing work to the pydra cluster.
- `Executable Tasks`_ - Tasks should be executable outside the cluster to allow
  easier development and debugging.

.. _Statistical Analysis of Task Runtimes: http://pydra-project.osuosl.org/ticket/171
.. _Cloud Support: http://pydra-project.osuosl.org/ticket/172
.. _Function Wrapper: http://pydra-project.osuosl.org/ticket/20
.. _Executable Tasks: http://pydra-project.osuosl.org/ticket/147

Write Applications Using Pydra
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Develop an application that uses Pydra to reduce its run time.  Here are some
suggestions, feel free to come up with your own ideas.

- Web Crawler
- Document Indexer

.. _gsoc2010-touchscreen20:

Touchscreen 2.0
---------------

Touchscreen is software for running interactive slideshows/demos.  Touchscreen
allows standalone slideshows or interactive displays using controls such as a
touchscreen interface.  It is primarily used at the OSL on the large
flatscreen+touchscreen directly outside our server room.  It displays various
statistics and realtime data about the lab.

We are in the process of rewriting touchscreen to use Django, Jquery,
javascript, HTML, and CSS.

`Learn more about Touchscreen <http://trac.osuosl.org/touchscreen>`_

Project Ideas
~~~~~~~~~~~~~

Write a Screen Plugin(s)
^^^^^^^^^^^^^^^^^^^^^^^^

Write new plugin(s) that showcases things happening at the osl.  We'll supply
the data, you supply an exciting representation of it.  

Here are some screens we have already produced:

- `Plotting Locations of Our FTP Users on a World Map in Realtime`__
- `OSL Bandwidth Usage`_
- `FTP Bandwidth map`_
- `Campus Webcams`_

.. __: https://trac.osuosl.org/touchscreen/ticket/19
.. _OSL Bandwidth Usage: https://trac.osuosl.org/touchscreen/ticket/16
.. _FTP Bandwidth map: https://trac.osuosl.org/touchscreen/ticket/20
.. _Campus Webcams: https://trac.osuosl.org/touchscreen/ticket/11

Suggestions for new screens:

- rewrite ftp user's map using google maps or `raphaeljs`_
- twitter feed - display feed of specific user(s), and or hashtag(s)
- trac project feed - project lists and recent commits
- RT ticket feed - dashboard of in progress and waiting tickets

.. _raphaeljs: http://raphaeljs.com

Work on Touchscreen Core
^^^^^^^^^^^^^^^^^^^^^^^^

Here are some suggestions of things to be worked on, or take a look at the `task
tracker`__.

.. __: http://trac.osuosl.org/touchscreen/report/1

- `Menuing configuration`_ - an interface for configuring a menuing system
- `Menu Generation`_ - display for the menu.

.. _Menuing configuration: https://trac.osuosl.org/touchscreen/ticket/12
.. _Menu Generation: https://trac.osuosl.org/touchscreen/ticket/13
