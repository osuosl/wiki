# osuosl/wiki

OSL's public documentation for people who use OSL services: Sphinx and
reStructuredText under `source/`, published to wiki.osuosl.org.

This repository is public, and so are its commit messages and pull requests.
Never add internal hostnames, private addresses, ticket links or numbers,
admin accounts, where credentials are kept, or staff procedures. `make lint`
(`check_style.py --public`) catches most of them.

OSL staff: the documentation skills are kept in the private osuosl/docs
repository, not here. Start Claude Code in a docs checkout with this one
added (`claude --add-dir <this checkout>`), and never copy skill material
into this repository.

Essentials:

- Work on a `<github-user>/<topic>` branch. Never push, open a PR or post a
  comment without an explicit OK.
- Build with `make html SPHINXBUILD=venv/bin/sphinx-build` (`-W`) and check
  with `make lint_changed`. `source/contributing.rst` has the conventions.
- Labels in `scripts/frozen_labels.txt` are linked from osuosl/docs. Don't
  rename or remove them without the matching docs change.
- `scripts/check_style.py` is identical in osuosl/docs. Change it there and
  copy it here.
