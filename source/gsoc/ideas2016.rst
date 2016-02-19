Google Summer of Code 2016 Ideas
================================

Welcome to the Oregon State University Open Source Lab Google Summer of Code
2016 idea page! Before applying please read over our :ref:`application guide
<gsoc-app-info>` for details specific to our organization.

Note: Our timezone is UTC -7, the best times to find us on IRC are between 16:00 
and 23:00 UTC. We will usually see your comments outside of those times, but 
might not be able to reply immediately. 

Ideas
-----

- :ref:`gsoc2016-timesync-clients`


.. _gsoc2016-timesync-clients:

TimeSync Client Projects
~~~~~~~~~~~~~~~~~~~~~~~~

The TimeSync API allows clients to store and retreive time entries for multiple
projects, regardless of the workflow or tools used to manage that project. Clients
for TimeSync will connect to the API and provide time tracking and reporting
functionality ont he command line, a web interface, GitHub, RT, and others.


Project: Ruby port of Pymesync
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Brief Explanation:**

Pymesync is an existing Python module providing connectivity to the TimeSync API. This 
project is aimed at creating a Ruby Gem with equivalent functionality for use in Ruby
applications, and a preliminary Ruby application that uses the new gem to provide 
basic visualization of TimeSync data.

**Expected Results**

A Ruby Gem equivalent in functionality to Pymesync (https://github.com/osuosl/pymesync)
and a basic Ruby application (using Sinatra or similar basic framework) that provides
simple data graphing of times logged byt project, user and activity.

**Knowledge Prerequisite:**

Ability to program in Ruby, with basic knowledge of Ruby Gem design. Familiarity with 
Python. Basic application design using a Ruby framework, and some understanding of
data visualization/graphing.

**Mentor:** Ken Lett (kennric)


------


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
