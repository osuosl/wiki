OSUOSL Public Documentation
===========================

This repo is the home for the previous public documentation hosted on
wiki.osuosl.org.

Updating dependencies
---------------------
Direct dependencies live in ``requirements.in``; ``requirements.txt`` is a
lock file generated from it with `pip-compile
<https://pip-tools.readthedocs.io/>`_. Dependabot updates the lock file
automatically using full dependency resolution. To change or upgrade
dependencies manually::

  pip install pip-tools
  pip-compile --strip-extras requirements.in            # re-lock after editing requirements.in
  pip-compile --strip-extras --upgrade requirements.in  # upgrade everything

Never edit ``requirements.txt`` by hand.
