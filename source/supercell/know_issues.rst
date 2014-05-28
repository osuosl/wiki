Known Issues
============

We are still in the beta phases of Supercell and Ganeti Web Manager, so we are
still under some pretty heavy development. There are a number of known issues at
the moment that we are working to improve. We will try to keep this list up to
date, but you should also check the `Ganeti Web Manager issues list`__ for a
more complete and updated list.

.. __: http://code.osuosl.org/projects/ganeti-webmgr/issues

Renaming a VM does not update DNS pointer
  When you create a VM, it should automatically generate a DNS name in the
  .osuosl.test domain (e.g. jefftest.osuosl.test). This will let you connect to
  the VM through the Supercell jumphost without having to know the internal IP
  address. When you rename a VM, a new pointer does not get created, so you will
  still need to use the old hostname to access it via ssh.

Reinstalling sometimes results in an error
  When you issue a reinstall command sometimes there's an error. Its a known
  issue but a workaround hasn't been figured out yet. As a short term solution,
  you can tend to work 5-10min after the first reinstall try and it usually
  works. Better solution for now is to just remove the VM and create a new one
  in its place if you hit this error.
