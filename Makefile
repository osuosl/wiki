# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -W -j auto -q
# --public: internal details and frozen labels always fail. Style errors only
# warn until the normalization sweep lands; then drop --warn-only.
STYLEOPTS     ?= --warn-only --public
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo
	@echo "OSL specific targets:"
	@echo "lint		Run rstcheck and check_style.py on all files"
	@echo "lint_changed	Run rstcheck and check_style.py on RST files changed from master"
	@echo "linkcheck	Check external links (report in build/linkcheck/output.json)"

rsync_copy: html
	@echo "Copying files to $(RSYNC_TARGET_DIR)"
	rsync -acq --delete-after --force --cvs-exclude $(BUILDDIR)/html/ $(RSYNC_TARGET_DIR)

lint:
	@echo "Running rstcheck"
	rstcheck -r $(SOURCEDIR)
	@echo "Running check_style.py"
	python3 scripts/check_style.py $(STYLEOPTS) $(SOURCEDIR)

# The frozen-label check runs whatever changed: deleting a page can remove a
# label that osuosl/docs links to.
lint_changed:
	@echo "Running rstcheck and check_style.py on changed RST files from master branch"
	@set -e; \
	git diff origin/master --name-only --diff-filter=d | grep 'rst$$' | xargs -r rstcheck --log-level INFO; \
	files=$$(git diff origin/master --name-only --diff-filter=d | grep '^$(SOURCEDIR)/.*rst$$' || true); \
	python3 scripts/check_style.py $(STYLEOPTS) $${files:-/dev/null}

# Without -W: a dead link is a finding to triage, not a build failure.
linkcheck:
	$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" -j auto -q $(O)

.PHONY: help rsync_copy lint lint_changed linkcheck Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
