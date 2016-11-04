MyGraphite in Docker
====================
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
      Docker 
    """
    docker-compose up

    """
      wanna rebuild ?
    """
    docker-compose up --build

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

