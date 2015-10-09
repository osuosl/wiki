Debugging a Django Application
==============================

There are numerous tools in the world designed to make debugging a Django
application much easier. Whether a template is taking too long to render, or an
API endpoint is crashing on certain input, there are better ways to debug than
inserting ``print`` statements.

Django Debug Toolbar
--------------------

The `Django Debug Toolbar`_ is a very useful tool that allows for viewing lots
of information about how every page was rendered, including debug error pages.
It adds a sidebar to rendered HTML requests that includes things like:

* Django, Python, and toolbar versions
* SQL queries needed to render the page, and their execution time
* Timing information
* Contents of settings
* Page and WSGI headers
* View information, including session data, POST data, view function name, view
  kwargs, etc.
* Static and template files
* Signals called during view
* Logging

To install the toolbar, install it with ``pip``::

    (venv) $ pip install django-debug-toolbar

and then add it to the project's ``INSTALLED_APPS``:

.. code-block:: python
    :emphasize-lines: 5

    # settings.py
    INSTALLED_APPS = (
        'my_project',
        ...
        'debug_toolbar'
    )

Run the app and it's ready to go! Whenever DEBUG is set to ``True``, any
connection matching Django's ``INTERNAL_IPS`` will have the toolbar. For more
information on how to install it, see
their `installation docs`_.

.. note::
    For API calls that error out, Django Debug Toolbar can be used, since it
    shows up on debug error pages. However, you'll need to use something like
    Django PDB to debug pages that don't throw errors.

.. _Django Debug Toolbar: http://django-debug-toolbar.readthedocs.org/en/latest/
.. _installation docs: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html

Django PDB
----------

Python's Debugger is useful for getting information from running processes,
including Django's built-in log of SQL queries ran. Unlike the Django Debug
Toolbar above, PDB can be used for any endpoint, including API endpoints, making
it a much more useful utility (though much harder to use, since it requires
knowledge of Python's debugger). `Django PDB`_ is a tool that can automatically
activate ``pdb`` for any endpoint.

To set up ``django-pdb``, first install it with ``pip``::

    (venv) $ pip install django-pdb

Then add it to the end of the application's ``INSTALLED_APPS``:

.. code-block:: python
    :emphasize-lines: 5

    # settings.py
    INSTALLED_APPS = (
        'my_project',
        ...
        'django_pdb'
    )

Add it to the end of the application's ``MIDDLEWARE_CLASSES``:

.. code-block:: python
    :emphasize-lines: 5

    # settings.py
    MIDDLEWARE_CLASSES = (
         'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
         ...
         'django_pdb.middleware.PdbMiddleware',
    )

Now, run the development server as normal::

    (venv) $ python manage.py runserver

To drop into ``pdb`` for a particular request, add a ``pdb`` parameter to the
request::

    $ curl http://localhost:8000/v1/objects/1?pdb

A ``pdb`` prompt should appear in the terminal where ``manage.py`` is running.
::

    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    October 09, 2015 - 20:56:08
    Django version 1.7.6, using settings 'project.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ()
    GET /v1/objects/1?pdb
    function "myview" in app/views.py:8
    args: ()
    kwargs: {'id': u'1'}
    ()
    > /home/user/projects/project/venv/local/lib/python2.7/site-packages/django/core/handlers/base.py(66)make_view_atomic()
    -> non_atomic_requests = getattr(view, '_non_atomic_requests', set())
    (Pdb)

Normal ``pdb`` commands can be used, including ``n(ext)`` to skip to the next
line of the current function, ``s(tep)`` to step to the next line, or into a
called function, and ``c(ontinue)`` to jump to the next breakpoint.

To view SQL queries run in a certain view, for instance, clear the previous
queries at the beginning of the view, step through the view until the return,
and print Django's queries list::

    (Pdb) from django.db import reset_queries
    (Pdb) n
    ...
    -> def song(request, id=None):
    (Pdb) n
    ..
    -> return HttpResponse(
    (Pdb) from django.db import connection
    (Pdb) connection.queries
    [{u'time': u'0.004', u'sql': u'QUERY = u\'SELECT "words_song"."id", "words_song"."name", "words_song"."video", "words_song"."slug" FROM "words_song" WHERE "words_song"."id" = %s LIMIT 21\' - PARAMS = (1,)'}]
    (Pdb)

For more information on how to use ``pdb``, see the `official debugger
documentation`_.

.. _Django PDB: https://github.com/tomchristie/django-pdb
.. _official debugger documentation: https://docs.python.org/2/library/pdb.html
