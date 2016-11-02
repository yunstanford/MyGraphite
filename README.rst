MyGraphite
==========
.. image:: https://travis-ci.org/yunstanford/MyGraphite.svg?branch=master
    :alt: build status
    :target: https://travis-ci.org/yunstanford/MyGraphite

MyGraphite helps you packaging all Graphite components(Carbon-cache, Carbon-relay, Webapp, etc.) 
and installing all python dependencies for you by utilizing uranium, an assembly tool for python.
With MyGraphite, you can easily set up Graphite on your local machine.


-------------------
OS level dependency
-------------------

Utilize homebrew.

.. code::

    """
      for broken image issue
    """
    brew install cairo
    brew install py2cairo

    """
      If you are using mysql as webapp backend database
    """
    brew install mysql

For more details, please refer
- https://graphite.readthedocs.io/en/latest/install.html#dependencies


-----------
Quick Start
-----------

Let's get started.

.. code::

    """
      Clone the repo
    """
    git clone git@github.com:yunstanford/MyGraphite.git


    """
      Set up uranium
    """
    ./uranium

    """
      Specify the version/branch for graphite-web and carbon.
    """
    vim ./conf_default/version.yaml

    """
      Set up all graphite components in one command line
    """
    ./uranium build

Yeah, we are good to use Graphite now.

.. code::

    """
      activate virtual env
    """
    source ./bin/activate


    """
      Start a single carbon-relay
    """
    python ./bin/carbon-relay.py --instance=a start


    """
      Start a single carbon-cache
    """
    python ./bin/carbon-cache.py --instance=a start


    """
      Start a bunch of carbon-cache and carbon-relay instances once.
    """
    # start all daemons
    ./bin/run

    # shutdown all daemons
    ./bin/shutdown


However, if you are utilizing uranium to exec these tasks (start and shutdown daemons),
you don't need to activate virtual env explictly. Run these command line directly.

.. code::

    """
      start all daemons
    """
    ./uranium daemons


    """
      shutdown all daemons
    """
    ./uranium shutdown


    """
      Start mysql server
    """
    mysqld_safe


    """
      Set up webapp backend database. This helps you create user, password
      and database
    """
    ./uranium db


    """
      Create initial schema, migration.
    """
    PYTHONPATH=$GRAPHITE_ROOT/webapp django-admin.py migrate --settings=graphite.settings --run-syncdb


    """
      Start webapp under Gunicorn
    """
    ./uranium webapp


    """
      Dev Mode: run Graphite under django development server
    """
    ./uranium dev

Then, go to http://0.0.0.0:8080.

Note, if you have any user access operation issue due to backend database, check out your webapp
database configuration. You should also create a user and grant all privileges on a database.

For more details, refer
- https://github.com/yunstanford/GraphiteSetup


-------------
Configuration
-------------

You can put all your configuration file in conf_default folder. when you run ./uranium build, it will
automatically move your configuration file to proper directory.

