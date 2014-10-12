====================================================
YouNeedToSleep - Simple and effective time tracking.
====================================================

.. image:: https://travis-ci.org/sleepy/sleepy.png?branch=master
        :target: https://travis-ci.org/sleepy/sleepy

.. warning::

   Sleepy is under heavy development. Don't use it.

.. figure:: https://sleepy.readthedocs.org/en/latest/_static/logo.jpeg
   :align: right
   :target: http://thenounproject.com/term/safe/1411/


Installation
------------

.. code-block:: bash

    $ Create your virtualenv (recommended, use virtualenvwrapper)
    $ mkvirtualenv sleepy

    $ # Clone repository
    $ git clone git@github.com:YouNeedToSleep/sleepy.git

    $ # Activate Environment and install
    $ workon sleepy
    $ make develop

    $ # run tests
    $ make test


Edit settings
-------------

Create a new file ``src/sleepy/settings.py`` with the following content:

.. code-block:: python

    from sleepy.conf.development import *

Edit and adapt this file to your specific environment.


Setup the database
------------------

.. note::

    Please note that ``sleepy`` was developed with PostgreSQL in mind. It may not be
    performant enough on other datastores or may not even support them.

Create an empty new PostgreSQL database.

.. code-block:: bash

    $ createdb sleepy_dev

.. note::

    You might need to apply a postgresql user (``createdb -U youruser``) e.g ``postgres``
    for proper permissions.


.. code-block:: bash

    $ python manage.py migrate


Superuser & example data
------------------------

.. code-block:: bash

    $ # Create a new super user
    $ python manage.py createsuperuser

Now you can run the webserver and start using the site.

.. code-block:: bash

   $ python manage.py runserver

This starts a local webserver on `localhost:8000 <http://localhost:8000/>`_. To view the administration
interface visit `/admin/ <http://localhost:8000/admin/>`_


Run other services
------------------

Other services being used:

* Grunt, is being used to compile our scss files and the foundation framework.


To start all of them (including the tls-server):

.. code-block:: bash

   $ foreman start

.. note::

   Please make sure you have the ``foreman`` gem installed.

.. note::

    You can find the SSL version on `port 8443 <https://localhost:8443/>`_


Run the test-suite
------------------

.. note::

    The test-suite requires to have access to the ``sleepy.local`` domain.
    You might need to add it to your ``/etc/hosts`` or use a DNS server like
    ``dnsmasq``.

.. code-block:: bash

    $ make test

Resources
---------

* `Documentation <http://youneedtosleep.today/docs/>`_
* `Bug Tracker <https://github.com/YouNeedToSleep/sleepy/issues>`_
* `Code <https://github.com/YouNeedToSleep/sleepy>`_
=======
.. image:: https://travis-ci.org/YouNeedToSleep/sleepy.png?branch=master
        :target: https://travis-ci.org/YouNeedToSleep/sleepy


Time Tracker

* Free software: BSD license
* Documentation: https://sleepy.readthedocs.org.

Features
--------

* TODO
>>>>>>> 718a6fd16077fb2cd8f323cf92355ab9b9ed587b
