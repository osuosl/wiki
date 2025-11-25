# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -W -j auto -q
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo
	@echo "OSL specific targets:"
	@echo "lint		Run rstcheck on all files"
	@echo "lint_changed	Run rstcheck only on changed RST files from master branch"

rsync_copy: html
	@echo "Copying files to $(RSYNC_TARGET_DIR)"
	rsync -acq --delete-after --force --cvs-exclude $(BUILDDIR)/html/ $(RSYNC_TARGET_DIR)

lint:
	@echo "Running rstcheck"
	rstcheck -r $(SOURCEDIR)

lint_changed:
	@echo "Running rstcheck on changed files RST from master branch"
	@set -e; \
	git diff origin/master --stat --name-only --diff-filter=d | grep rst$$ | xargs -r rstcheck --log-level INFO

.PHONY: help rsync_copy Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
