Updating CASS Pelican Websites
==============================

This documentation applies to both the CASS main website, the OSL website and
any other sites using the Pelican static site generator with Git and Github.

What is Pelican
---------------

`Pelican`_ is a static site generator. Static Site Generators, a.k.a. SSGs take
structured text files and convert them into websites. In short, it allows us to
create a great website by writing simple text files, without the overhead of
logging into a website to write content.

`This article`_ discusses the advantages and disadvantages of SSGs.

Another advantage of Pelican and other SSGs is that we can use familiar
code-management tools to manage our website content: Git and Github

.. _Pelican: http://docs.getpelican.com
.. _This article: https://davidwalsh.name/introduction-static-site-generators

What is Git
-----------

`Git`_ is a system that tracks changes to files. It allows multiple people to
edit the same set of files and merge their changes together. All the files, and
a history of all the changes made to them, are stored in such a way that you can
retrieve the past state of any file easily, without having many copies of a
file, each with different changes. `This comic`_ neatly illustrates how useful a
revision control system like Git can be.

We store our Pelican site files in Git repositories, and we use `Github`_ to
store and manage those repositories. Github provides an easy to use web
interface to the majority of git's functionality. We use it to review changes,
to merge changes into production, and to track issues.

.. _Git: https://git-scm.com
.. _Github: https://github.com
.. _This comic: http://www.phdcomics.com/comics/archive.php?comicid=1531

Git via GitHub
~~~~~~~~~~~~~~

Many people use Git through the command-line, but this isn't everyone's cup of
tea. Thankfully, you can do most git operations entirely from the Github web UI.
If installing a git client on your personal workstation is problematic, you can
create and edit site content entirely on-line.

Git on the Desktop
~~~~~~~~~~~~~~~~~~

Another alternative to using git on the command-line is a Git Desktop
application.

There are a number of good Git desktop applications, but for working with
GitHub, we recommend `GitHub Desktop`_

When working with the website on your workstation, you will want a good text
editor if you don't already have one, we recommend `Atom`_. Text editors are
different from Word Processors like MS Word or LibreOffice, text editors are
focused only on plain text, they don't do formatting, fonts, colors or other
visual styling or layout, and they save files in a universal format that can be
read by any computer system. Because our Pelican website theme handles all the
formatting for the website, we only want to write plain text files.

.. warning::

  Only edit files in a Text Editor, never use a Word Processor like MS Word.

.. _GitHub Desktop: https://desktop.github.com
.. _Atom: https://atom.io/

Git on the Command Line
~~~~~~~~~~~~~~~~~~~~~~~

If you already are used to working with Git on a command line, you are good to
go, you'll just need to ensure that you have access to the OSL Pelican Git
repositories. See the `official Git web page`_ to install Git on your platform.

.. note::

  The Github Desktop for Windows package comes with a Git Shell program for
  working with git on a command line.

.. _official Git web page: https://git-scm.com

Getting Access
--------------

In order to make updates to the pelican sites, you will need access to the
`OSL Git repositories`_.

First, `create an account on Github`_. Then contact the OSL dev team and they
will add your account to the repositories you need.

If you are working on the command line, you will also need to set up an ssh
key pair and upload the public key to Github. See the `Github SSH Key`_ page
for more information.

.. _create an account on Github: https://github.com/join
.. _Github SSH Key: https://help.github.com/articles/generating-an-ssh-key
.. _OSL Git repositories: https://github.com/osuosl/

The Workflow
------------

**Summary**

#.  Check out the Git repository and create a new branch
#.  Add/edit content
#.  Push your branch up to Github
#.  Make a pull request to the staging branch on Github
#.  Solicit reviews of your changes
#.  Merge your branch with the staging branch
#.  Review changes on the staging site
#.  Merge staging with the production branch
#.  Review changes on the production site

Checking out the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The content for Pelican sites will be in a repository on Github named for the
site it contains:

* OSL website: `osuosl-pelican`_
* CASS website: `cass-pelican`_
* Beaver Barcamp: `beaver-barcamp-pelican`_

You can view and even edit the contents of the repository directly on its Github
page, but it is usually better to 'clone' the repository to your local machine.

**GitHub Desktop**

Open Github Desktop and log in. You will see a + button a the top left, click
that to open the Add menu. Then click on the Clone tab. You should see a list
of Github Organizations on the left, and a list of repositories on the right
(the repository list may be empty if you don't have repositories of your own).

.. image:: /_static/images/github_desktop-add.png

Select the *osuosl* organization on the left, and find the repository you want
to update on the right. Type 'pelican' into the filter box to see all of our
Pelican site repositories.

Click on your repository and then click the checkmark button that appears below.
Github desktop will ask you for a directory to clone to - the default is fine,
but feel free to put it wherever you like.

Your cloned repository now appears in the left sidebar of the Github
application. Once the repository is added, you won't have to add it again,
you'll only  need this step if you want to work on a repository you haven't
already cloned.

.. note::
  Before you start working on new changes to the site, change to
  the **staging** branch; this is the branch from which you should always
  start.

At the top, you will see a pull-down containing the list of branches:

.. image:: /_static/images/github_desktop-branch_select.png

Select *staging*.

Before you edit any of the site content, create a new branch to contain your
own changes. Click the icon just to the left of the branch selection pull-down
and give your branch a name, like ``your_name/a_descriptive_branch_name``.

The string ``your_name/a_descriptive_branch_name`` is the full name of the
branch, you can call it whatever you like, but it is easier to manage if you
prefix them with your own username, followed by a descriptive name that
explains what you are doing.

For example, if I were adding Fred to the staff list, I would probably make a
branch named ``kennric/add_fred_to_staff_list``.

Double check that the 'From branch' says 'staging', and click 'Create new
branch'.

Now you can begin making changes or adding content. Continue to the next step,
Editing Content.

**Command Line**

First, clone the repository you want to work on. Once you have a local clone,
you won't need to do this again.

::

  git clone https://github.com/osu-cass/cass-pelican

Now you have a local copy of the website in the cass-pelican directory. Move
into that directory for the following steps.

First, check out the staging branch. If this is the first time you have cloned
the repository, this will check out staging and make sure your local copy tracks
the changes on Github.

.. note::
  Before you start working on new changes to the site, change to the **staging**
  branch; this is the branch from which you should always start.

::

  git checkout -tb staging origin/staging

If you already have the staging branch checked out from before, you can just
switch to it:

::

  git checkout staging

and pull in any changes that have happened since the last time you worked on the
site:

::

  git pull

Now you are in an up-to-date staging branch.

::

  git checkout -b your_name/a_descriptive_branch_name

The string ``your_name/a_descriptive_branch_name`` is the full name of the
branch, you can call it whatever you like, but it is easier to manage if you
prefix them with your own username, followed by a descriptive name that
explains what you are doing.

For example, if I were adding Fred to the staff list, I would probably make a
branch named ``kennric/add_fred_to_staff_list``.

Now you can begin making changes or adding content.

.. _osuosl-pelican: https://github.com/osuosl/osuosl-pelican
.. _cass-pelican: https://github.com/osu-cass/cass-pelican
.. _beaver-barcamp-pelican: https://github.com/osuosl/beaver-barcamp-pelican

Editing Content
~~~~~~~~~~~~~~~

Take a look at the folder where you cloned the repository. In Github Desktop you
can right-click on the repository name and select 'view in explorer', or open
the folder from the Atom editor, or whatever method you usually use to view
files.

All of the content for the site lives in the ``content`` directory. Content is
organized into directories; in the CASS site, for instance, there are ``blog``,
``pages``, and ``images`` directories. You should become familiar with the
location of the content you will be working with.

Content is written in plain text with easy to read markup, the format is called
ReStructuredText, a.k.a. RST. The files have the extension .rst. Pelican makes
use of some RST declarations to add metadata to a page or blog post, such as
author and date.

Here is a `guide on writing RST`_ for Pelican sites, we recommend reading it
before starting, and bookmarking it for future reference.

When you are ready, simply open the file you want to modify and edit it.

.. warning::

  Only edit files in a Text Editor, never use a Word Processor like MS Word.

Below are described several of the specific kinds of content in our sites and
information about the menu structure.

.. _guide on writing RST: http://docs.getpelican.com/en/3.6.3/content.html


Metadata
++++++++

All Pelican content files have a block of metadata at the top that tells Pelican
how to organize the content.

::

  10 Projects Making a Difference
  ===============================
  :date: 2013-11-25 19:23
  :author: Melissa
  :slug: 10-projects-making-a-difference

The first thing in a file is the title, underlined with =. Always include
the ``:author:``, ``:date:`` and ``:slug:`` metadata.

.. note::

  The *slug* is the name of the page as it will appear in the URL. For instance
  if you set the slug to 'my_fancy_new_page', it will be found at
  http://your_site.org/my_fancy_new_page

Blog Posts
++++++++++

Blog posts are added to ``content/blog/posts/``. They should include the
following metadata:

::

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

::

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

* ``:menu: <parent_name>, <page_name>, <menu_weight>; <parent2>, <name2>,
  <weight2>; ...``

  This metadata is required for pages to be included in the menu. Each menu
  location is delimited by a semicolon (';'). Menu items can have one or
  multiple locations in the menu.

  - ``<parent_name`` is the name of the menu item above the current item
  - ``<page_name>`` is the name of the current item that will be displayed in
    the menu
  - ``<menu_weight>`` is the weight of the menu item. Items with higher weights
    appear lower on the menu.

* ``:slug: path/to/rendered/file``

  - This is used as the link in the ``<a href=''>`` tag.

Example
+++++++

Example page headers and resultant menu structure:

about.rst:

::

  About
  =====
  :slug: about
  :menu: top, About, 0; About, Summary, 10


organization.rst:

::

  Organization
  ============
  :slug: org
  :menu: top, Organization, 5; Organization, Structure, 0


staff.rst:

::

  Staff
  =====
  :slug: org/staff
  :menu: Organization, Staff, 5


This results in this menu structure:

::

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
`examples`_ of forms that can be looked at as well.

.. _Formsender docs: http://formsender.readthedocs.org/en/latest/
.. _examples: https://github.com/osuosl/osuosl-pelican/tree/master/content/forms

Pushing Your Changes
--------------------

Now that you have new or edited content, you'll need to push it up to Github so
that it can be approved and pushed onto the staging site.

First, add the changes to your copy of the repository. Git will see the files
you have added or changed, but doesn't know you want to keep them unless you
tell it.

**GitHub Desktop**

Click the 'Changes' button at the top of Github Desktop.

.. image:: /_static/images/github_desktop-changes_button.png

You should see a list of files you have changed below. If you click on a file,
the application will show you all the changes you have made - additions will be
shaded in green, deletions in red.

If the changes look correct to you, you can commit them to your branch. Simply
add a short description to the 'Summary' box below the file list, and a longer
description in the 'Description' box. This is your *commit message*.

The commit message is very important, it allows people to look a the history of
the git repository and understand what has changed, who changed it, and why.

A typical commit message is structured like this:

::

  Here is my quick summary sentence

  Here is a longer, more detail description of my changes. I don't need to tell
  git what files I changed, or what the changes are, I use this commit message
  to tell my colleagues why I made the changes.

When you have entered your commit message, click the 'Commit to ...' link below.
Your changes are now part of your branch, but only locally; no one can see them
until you push them up to Github.

To publish your changes, simply click the 'Publish' or 'Sync' button at the top
right. If the branch is brand new, you'll see 'Publish', if it already exists on
Github, you'll see 'Sync'.

.. image:: /_static/images/github_desktop-sync_button.png

Your changes are now pushed to Github, continue to the next step Make a Pull
Request.

**Command Line**

::

  git add content/your_changed_file.rst

If you have changed several things, it's a good idea to ask git what is
different so that you can add everything and nothing is missed.

::

  git status

which prints out the following in my case:

::

  On branch kennric/pelican_howto
  Untracked files:
    (use "git add <file>..." to include in what will be committed)

    source/howtos/updating_pelican_sites.rst

  nothing added to commit but untracked files present (use "git add" to track)


Next, you will need to reassure git that you really want to commit your
changes to the repository:

::

  git commit

This will open an editor, because git insists that you add a message describing
your commit. The format for a git commit message is simply a short one-line
summary followed by a blank line and then an optional long description of your
commit.

::

  Here is my quick summary sentence

  Here is a longer, more detail description of my changes. I don't need to tell
  git what files I changed, or what the changes are, I use this commit message
  to tell my colleagues why I made the changes.

  # Please enter the commit message for your changes. Lines starting
  # with '#' will be ignored, and an empty message aborts the commit.
  # On branch kennric/pelican_howto
  # Changes to be committed:
  #       new file:   source/howtos/updating_pelican_sites.rst
  #

Note that git already knows everything I changed, this message is to tell other
humans why I made the changes I made.

Now your local copy of the git repository contains your changes. Next, push
those  changes up to Github so that others can see and review them.

::

  git push origin your_name/a_descriptive_branch_name

Now your branch is on Github. For the next step, we'll need to go to the Github
page for the site you are editing.

Make a Pull Request
-------------------

A pull request, a.k.a. PR, is a request to have your branch merged into another
branch (usually staging or master, but it can be any branch). You can create a
PR from Github Desktop, or on the Github site itself.

**GitHub Desktop**

Click the 'Pull Request' button at the top right. This will open a Pull Request
sidebar with a Title and Description field. These may be filled in for you, but
it's a good idea to double-check the contents. Like the commit message, these
fields allow you to communicate what you are doing and why. If you want your
changes reviewed or noticed by specific people, you can 'tag' them in the
description field. To tag someone, simply put an @ in front of their Github
username. If you don't know their username, just type @ and a menu of possible
people will appear.

You will also see a line above the title that indicates which branch you are
merging, and the target branch. Be sure that the target is **staging** and the
'from' branch is the branch you created.

When you are happy with the title and description, click 'Send pull request'.

**Github**

I'll defer to Github's own `documentation`_ on how to make a PR on the Github
website.

When you make your initial pull request, you'll select your branch (it will be
easy to find if you prefixed it with your name), and request to merge with the
**staging** branch. Be sure to select staging in the "base: " pull-down box.

.. note::

  Always select **staging** as the base branch

.. _documentation: https://help.github.com/articles/using-pull-requests

Solicit Reviews
---------------

The next step is to have your changes approved by the page owner and/or someone
familiar with Pelican and RST.

The review process takes place on the Github website. Once you have created a
pull request, you'll see it listed under the 'pull requests' tab of your
repository on Github. When you select a pull request, you will see tabs for
'Conversation', 'Commits', and 'Files changed'. 'Conversation' is where people
will comment on your changes and approve or ask for further changes.

You can 'tag' individuals or the webdev group in the 'Conversation' tab of the
pull request by adding @username or @webdevs to a comment:

::

  @webdevs, please review

This will notify everyone in the webdevs group (you, OSL developers, and other
CASS content owners) of the comment, according to their own notification
settings. If the change is urgent, it's a good idea to ping a specific person
online or in person to make sure they know that you are waiting on their review.

When you have a thumbs-up (a.k.a. +1) from the page owner or other reviewer, the
content can be merged by the page owner.

Merge Into Staging
------------------

If you are the page owner, please read this `Github page`_
on merging pull requests.

In most cases, merging is a simple click on the "Merge Pull Request" button.

.. _Github page: https://help.github.com/articles/merging-a-pull-request/

Review the Staging Site
-----------------------

When changes are merged into the staging branch, our back-end systems will push
those changes to the staging website. You can see what your changes will look
like in production by visiting the staging site.

* `OSL staging`_: http://osuosl.staging.osuosl.org
* `CASS staging`_: http://cass.staging.osuosl.org


.. _OSL Staging: http://osuosl.staging.osuosl.org
.. _CASS Staging: http://cass.staging.osuosl.org


Merge with Master
-----------------

If things look good, you or the page owner can create another pull request from
the staging branch to the master branch, following the same procedure as
for creating a pull request from your editing branch to staging. When this
is merged into master, the production site will be updated automatically with
your changes.
