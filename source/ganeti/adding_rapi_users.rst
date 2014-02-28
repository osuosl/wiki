Adding RAPI users to Ganeti
===========================

To add a user to the RAPI in Ganeti you need to do the following:

- Pick a username and a good password ( usually ganeti-webmgr and ``$ pwgen -s
  -n 20 -1``)
- Create a hash using the example below
- Add to ``/var/lib/ganeti/rapi_users``
- Restart Ganeti

Creating a hash
---------------

On any machine that has the openssl libraries, do the following:

.. code-block:: bash

    # username: john
    # password: p4ssw0rd
    echo -n 'john:Ganeti Remote API:p4ssw0rd' | openssl md5

    # copy the hash into /var/lib/ganeti/rapi/users like the following:
    john {HA1}2f3ef95b86ddfd74c65c695f0efb7077 write

    # for read-only access:
    john {HA1}2f3ef95b86ddfd74c65c695f0efb7077

.. note::

  The location of the file used to be ``/var/lib/ganeti/rapi_users`` prior to
  Ganeti 2.4

References
----------
- `Ganeti RAPI Users documentation
  <http://docs.ganeti.org/ganeti/current/html/rapi.html#users-and-passwords>`_
