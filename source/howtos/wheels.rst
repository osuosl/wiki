Compiling Python Wheels
=======================

Python Wheels are used to distribute pre-compiled versions of Python packages.
This allows deployment of those packages on servers without having to install
``gcc``, ``python-devel``, and various other C headers -- and allows for all
servers deployed using those Wheels to have exactly the same version of the
dependency installed.

.. note:: The requirements for Ganeti Web Manager will be used as an example
    here.

Installing Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Only compile a wheel on a system set up the same as the system the wheel will be
deployed on. For instance, a x64 Debian 8 machine will only ever compile wheels
for other Debian 8 machines.

To compile a wheel, ``pip``, ``gcc``, ``libffi``, the and the Python development
headers are needed. Other dependencies might be needed; for example,
cryptographic wheels will require ``libssl-dev`` or ``openssl-devel``.

Building the Wheels
~~~~~~~~~~~~~~~~~~~

Once ``pip``, ``gcc``, and other dependencies are installed, install ``wheel``
with ``pip``::

    $ pip install wheel

To compile all of the ``wheels`` for a given project, the ``-r`` flag can point
to a requirements file::

    $ pip wheel -r requirements.txt

The finished wheels will be put into ``wheelhouse/``. The wheels can be uploaded
to wherever they are needed; for instance, Ganeti Web Manager's setup script
searches for wheels on ``ftp.osuosl.org``.
