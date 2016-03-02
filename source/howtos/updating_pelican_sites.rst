CASS Website Workflow
=====================

This documentation applies to both the CASS main website, the OSL website
and any other sites using the Pelican static site generator.


What is Pelican
---------------


What is Git
-----------


Git via GitHub
~~~~~~~~~~~~~~


Git on the Mac
~~~~~~~~~~~~~~


Git on Windows
~~~~~~~~~~~~~~


The Workflow
------------


**Summary**

#.	Check out the Git repository and create a new branch
#.	Add/edit content
#.	Push your branch up to Github
#.	Solicit reviews of your changes
#.	Review changes on the staging website
#.	Merge staging with production


Checking out the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The content for Pelican sites will be in a repository on Github named
for the site it contains:

OSL website: https://github.com/osuosl/osuosl-pelican
CASS website: https://github.com/osuosl/cass-pelican
Beaver Barcamp: https://github.com/osuosl/beaver-barcamp-pelican

You can view and even edit the contents of the repository directly on its 
Github page, but it is usually better to 'clone' the repository to your
local machine. How you do this depends on the operating system and git 
client you use. For examples in this document, I'll use the git 
command-line client, which can be used on all platforms. 

.. code-block::bash

	git clone https://github.com/osuosl/cass-pelican

Now you have a local copy of the website in the cass-pelican directory. 
Move into that directory for the following steps.

First, we have to check out the staging branch. If this is the first time
you have cloned the repository, this command will check out staging and 
make sure your local copy tracks the changes on Github.

.. code-block::bash

	git checkout -tb staging origin/staging

If you already have the staging branch checked out from before, you can 
just switch to it:

.. code-block::bash

	git checkout staging

and pull in any changes that have happened since the last time you worked
on the site:

.. code-block::bash

	git pull


Now you are in an up-to-date staging branch. Next, create a new branch to
hold your changes

.. code-block::bash

	git checkout -b your_name/a_descriptive_branch_name


The string "your_name/a_descriptive_branch_name" is the full name of the 
branch, you can call it whatever you like, but it is easier to manage if you 
prefix them with your own username, followed by a descriptive name that 
explains what you are doing. 

For example, if I were updating the staff list, I would probably make a 
branch like this:


.. code-block::bash

	git checkout -b kennric/update_staff_list


Now you can begin making changes or adding content.


Editing Content
~~~~~~~~~~~~~~~

All of the content for the site lives in the 'content' directory. Content 
is organized into directories; in the CASS site, for instance, there are 
'blog', 'pages', and 'images' directories. You should become familiar with 
the location of the content you will be working with.

Content is written in plain text with easy to read markup, the format is 
called ReStructuredText, a.k.a. RST. The files have the extension .rst.
Pelican makes use of some RST declarations to add metadata to a page or
blog post, such as author and date.


`A guide on writing RST for Pelican sites <http://docs.getpelican.com/en/3.6.3/content.html>`_


Blog Posts
++++++++++

Blog posts are added to ``content/blog/posts/``. They should include the
following metadata:

.. code-block:: none

  :date:      # Date the post was written (format: yyyy/mm/dd)
  :author:    # The name of the person who wrote the post, not the submitter
  :slug:      # Link to the page when the site is generated


Regular Pages
+++++++++++++

Regular pages are added in ``content/`` under the relative directory. If the
page doesn't make sense in any of the current folders, create a new one.

All regular pages require a ``:slug:`` metadata. If the page will be included in
the menu, it also requires ``:menu:`` as described below.


Navigation Menu
+++++++++++++++

Our Pelican theme creates a main menu in the following format:

.. code-block:: none

  thing1              thing2              thing3      thing4
     |                   |                   |           |
  child1              child1 -- gchild1   child1      child1
     |                   |         |         |           |
  child2 -- gchild1   child2    gchild2   child2      child2
     |         |                   |                     |
  child3    gchild2             gchild3               child3
     |                                                   |
  child4                                              child4 -- gchild1
                                                                   |
                                                                gchild2


This requires a menu metadata field to be added to the page:

* ``:menu: <parent_name>, <page_name>, <menu_weight>; <parent2>, <name2>, <weight2>; ...``

  This metadata is required for pages to be included in the menu. Each menu
  location is delimited by a semicolon (';'). Menu items can have one or
  multiple locations in the menu.

  - ``<parent_name`` is the name of the menu item above the current item
  - ``<page_name>`` is the name of the current item that will be displayed in the
    menu
  - ``<menu_weight>`` is the weight of the menu item. Items with higher weights
    appear lower on the menu.

* ``:slug: path/to/rendered/file``

  - This is used as the link in the ``<a href=''>`` tag.

Example
+++++++

Example page headers and resultant menu structure:

about.rst:

.. code-block:: none

  About
  =====
  :slug: about
  :menu: top, About, 0; About, Summary, 10


organization.rst:

.. code-block:: none

  Organization
  ============
  :slug: org
  :menu: top, Organization, 5; Organization, Structure, 0


staff.rst:

.. code-block:: none

  Staff
  =====
  :slug: org/staff
  :menu: Organization, Staff, 5


This results in this menu structure:

.. code-block:: none

  Home    About      Organization
             |               |
             |               |
          Summary       Structure
                             |
                             |
                          Staff

Forms
~~~~~

Forms should be added under ``content/forms`` and should follow the form
specifications outlined in the `Formsender docs`_. The OSL website already has
`examples of forms`_ that can be looked at as well.

.. _Formsender docs: http://formsender.readthedocs.org/en/latest/
.. _examples of forms: https://github.com/osuosl/osuosl-pelican/tree/master/content/forms


Pushing Your Changes
--------------------

Now that you have new or edited content, you'll need to push it up to Github
so that it can be approved and pushed onto the staging site.

First, we need to add the changes to your copy of the repository. Git will
see the files you have added or changed, but doesn't know you want to keep
them unless you tell it.

.. code-block:: bash

	> git add content/your_changed_file.rst


If you have changed several things, it's a good idea to ask git what is 
different so that you can add everything and nothign is missed.

.. code-block:: bash

	git status

which prints out the following in my case:

.. code-block:: bash

	On branch kennric/pelican_howto
	Untracked files:
	  (use "git add <file>..." to include in what will be committed)

		source/howtos/updating_pelican_sites.rst

	nothing added to commit but untracked files present (use "git add" to track)


Next, you will need to reassure git that you really want to commit your
changes to the repo:

.. code-block:: bash

	git commit

This will open an editor, because git insists that you add a message describing
your commit. The format for a git commit message is simply a short one-line summary
followed by a blank line and then an optional long description of your commit.

