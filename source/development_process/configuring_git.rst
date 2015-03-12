Configuring Git
===============
Git's default configuration is very good, but adding a couple lines can make
working with git much easier.

``.gitconfig``
--------------

It is imperative that developers set their email
and user name in their ``~/.gitconfig`` file. Developers may use any email
address they prefer, including their work email. If developers want commits
they make using that email address to show up as part of their github commit
count they should add that email on
`Github <https://github.com/settings/emails>`_.

When editing commits, git
defaults to using the nano editor. Most developers will want to change this to
vim or the editor of their choice. Setting up color configuration can make git
command line output much easier to read. It can also be handy to set up aliases
for commonly used or long git sub-commands. Using the example config, running
``git net`` will run ``git log`` with a series of useful options.

.. code::ini
	[user]
		email = iankronquist@osuosl.org
		name = Ian Kronquist
	[core]
		editor = vim
	[alias]
		net = log --graph --all --decorate
	[color]
		branch = auto
		diff = auto
		status = auto

View the Current Branch in the Prompt
-------------------------------------
It can be very helpful to view the current git branch in the prompt. If using
the bash shell the following can be used to read the current branch and add it
to the prompt.

.. code::bash
	# In .bashrc
	# To get the current git branch, if any
	__git_prompt () 
	{ 
		local b="$(git symbolic-ref HEAD 2>/dev/null)";
		if [ -n "$b" ]; then
			printf "(%s)" "${b##refs/heads/}";
		fi
	}
	# PS1 is the bash variable which defines the formatting of your prompt
	# This example is rather bland, and has no color
	PS1='\u:(\w)$(__git_prompt)$ '

More tricks for styling the prompt can be found on the
`Arch Linux Wiki <https://wiki.archlinux.org/index.php/Color_Bash_Prompt>`_.

Tab Complete Git Commands
-------------------------

Git has a script for bash shells which will autocomplete git sub commands.
Download the script from `Git's GitHub repository
<https://github.com/git/git/blob/master/contrib/completion/git-completion.bash>`_
and source it in the ``.bashrc`` configuration file.

.. code::bash
	# In .bashrc
	source path/to/git-completion.bash

Similar scripts are available for Tcsh and Zsh.
